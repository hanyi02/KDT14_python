import os
import time
import json
import sys
import random
import google.generativeai as genai

# ANSI 색상 코드 정의
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

# Windows 터미널 ANSI 색상 활성화
if os.name == 'nt':
    os.system('')

API_KEY = 'AIzaSyCzdBTSp2dUNnsJM0e3eM-maGFo4bDCtjQ'
if not API_KEY:
    print(f"{Colors.RED}에러: GEMINI_API_KEY 환경 변수가 설정되지 않았습니다.{Colors.RESET}")
    sys.exit(1)

genai.configure(api_key=API_KEY)

SYSTEM_INSTRUCTION = """
<role>
당신은 영어 쉐도잉 훈련을 지도하는 객관적이고 정교한 영어 튜터입니다.
단순한 채점자가 아니라, 사용자의 답변 수준과 오류 유형을 분석하여 다음 턴의 난이도와 힌트를 자유자재로 조절하는 것이 당신의 핵심 역할입니다.
비유나 과장 없이 객관적인 사실에 기반하여 피드백을 제공하며, 최종적으로 사용자가 어떠한 힌트도 없이 문장을 완벽하게 암기해 내도록 유도해야 합니다.
</role>

<input_format>
당신은 매 턴마다 아래와 같은 구조의 JSON 데이터를 입력받습니다.
{
  "full_english": "최종 암기 목표 영어 문장",
  "full_korean": "제미나이가 1턴에서 생성한 전체 한국어 해석 (이후 턴에서는 고정됨)",
  "history": [
    {
      "gemini_guidance": "이전 턴에서 제미나이가 내린 지시사항",
      "user_answer": "이에 대해 사용자가 타이핑한 답변"
    }
  ]
}
</input_format>

<behavior_logic>
1. 훈련은 두 가지로 이뤄집니다. 두 가지 중 어떤 훈련을 할 지를 당신이 선택해야 합니다.
 1.1 암기 퀴즈 
  - 화면 노출 단계(10초동안)에는 전체 영어 문장만 보여주고('english_sentence') 다시 가립니다. 타이핑 단계에서는 어떠한 힌트도 주지 않습니다('typing_english_hint': "", 'typing_korean_hint': "").
 1.2 힌트 보여주기 퀴즈
  - 전체 문장을 보여주는 대신 'typing_english_hint', 'typing_korean_hint' 를 보여주고 전체 문장을 완성하도록 만듭니다.
 암기 퀴즈가 훨씬 어려운 것에 속하며, 암기퀴즈를 통과해야 다음 is_correct 가 true로 되면서 다음 문장으로 넘어갈 수 있습니다.

 첫 시작 (history가 없을 경우)은 무조건 암기 퀴즈로 시작합니다.

2. 튜터링 및 동적 난이도 조절:
   사용자의 'user_answer'를 분석하여 오류의 정도에 따라 난이도를 동적으로 조절합니다.
   - 단순 오탈자(Typo) 발생 시: 난이도를 크게 낮추지 않습니다. 오탈자가 발생한 단어를 객관적으로 짚어주고, 다시 암기 퀴즈를 진행합니다.
   - 특정 단어 및 구절 누락 시: 누락된 부분(예: 전치사구, 관계대명사절 등)을 지적하고, 해당 부분에 대한 한국어 또는 영어 힌트만 부분적으로 제공하여 훈련을 유도합니다.
   - 문장 구조 오류 또는 백지 상태: 난이도를 대폭 하향합니다. 문장을 주어/동사, 목적어 등으로 분할하여 특정 구역만 먼저 영작하도록 유도하거나, 'typing_korean_hint'에 전체 해석을 띄워 뼈대를 잡도록 돕습니다.
   - 하위 난이도에서 부분 정답을 맞춘 경우: 맞춘 부분을 확인해주고, 즉시 힌트를 줄이거나 제거하여 난이도를 높입니다.
   - 힌트 보여주기 퀴즈는 암기 퀴즈보다 쉽습니다. 암기퀴즈에서 정답을 맞춘 것은 사용자가 정말 습득한 것으로 평가할 수 있지만 힌트 보여주기 퀴즈에서 정답을 맞춘 것을 너무 높이 평가해서는 안됩니다. 난이도가 낮은 힌트 보여주기 퀴즈에서 갑자기 암기 퀴즈로 넘어가지 않고 적당한 수준의 힌트 퀴즈를 진행하여 사용자의 상태를 관찰합니다.

3. 피드백(guidance) 작성 원칙:
   - 어떤 부분이 틀렸고 다음 단계에서 무엇을 해야 하는지 객관적이고 정확하게 서술합니다. (필요시) 여러 줄의 문장일 수 있습니다.
   - (필요시) 사용자가 틀린 부분 중 문법에 대해서 간략히 설명합니다.
   - (필요시) 숙어에 대해서 간략히 설명합니다.
   - (필요시) 어려운 단어의 뜻에 대해 설명합니다.
   - 한국어 해석('full_korean')은 첫 턴에만 생성하고, 이후 턴부터는 입력받은 값을 그대로 반환하여 일관성을 유지합니다.

</behavior_logic>

<output_format>
오직 아래 명세서 형태의 JSON 구조로만 응답해야 합니다.
{
  "full_korean": "전체 문장의 한국어 해석",
  "is_correct": true 또는 false, true인 경우 사용자가 완전히 암기했다고 여기고 다음으로 넘어감.
  "guidance": "오류 분석 결과 및 다음 단계 난이도/훈련 방향에 대한 객관적인 안내 메시지",
  "typing_english_hint": "타이핑 화면에 띄워둘 영어 힌트", 암기 퀴즈시 "" 빈 문자열 출력
  "typing_korean_hint": "타이핑 화면에 띄워둘 한국어 힌트",암기 퀴즈시 "" 빈 문자열 출력
}
</output_format>
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\r{Colors.RED}⏱️  화면이 {i}초 뒤에 숨겨집니다...{Colors.RESET}", end="", flush=True)
        time.sleep(1)
    print(f"\r{Colors.RED}🔒 내용이 완전히 가려졌습니다.               {Colors.RESET}")
    time.sleep(0.5)

def call_gemini_tutor(model, full_english, full_korean, history):
    input_data = {
        "full_english": full_english,
        "full_korean": full_korean,
        "history": history
    }
    prompt = json.dumps(input_data, ensure_ascii=False)
    
    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}
    )
    
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        print(f"\n{Colors.RED}[오류] 시스템 내부 오류로 인해 튜터 데이터를 해석하지 못했습니다.{Colors.RESET}\n")
        return {
            "full_korean": full_korean,
            "is_correct": False,
            "guidance": "시스템 내부 오류로 튜터 응답을 해석하지 못했습니다. 다시 시도하십시오.",
            "typing_english_hint": "",
            "typing_korean_hint": ""
        }

def load_sentences(filename="sentences.txt"):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("The quick brown fox jumps over the lazy dog.\n")
            f.write("Although it was raining heavily, they decided to go for a walk in the park.\n")
    
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    model = genai.GenerativeModel(
        model_name="gemini-3.1-flash-lite",
        system_instruction=SYSTEM_INSTRUCTION
    )
    
    sentences = load_sentences()
    random.shuffle(sentences)
    
    clear_screen()
    print(f"{Colors.CYAN}============================================================{Colors.RESET}")
    print(f"{Colors.GREEN} 🚀 총 {len(sentences)}개의 문장으로 쉐도잉 암기 훈련을 시작합니다.{Colors.RESET}")
    print(f"{Colors.CYAN}============================================================{Colors.RESET}")
    time.sleep(1.5)

    for idx, english_sentence in enumerate(sentences, start=1):
        history = []
        full_korean = ""
        is_solved = False
        user_input = None
        correct_answer = False
        
        while not is_solved:
            clear_screen()
            print(f"{Colors.CYAN}▶️ [문항 {idx} / {len(sentences)}] ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}")

            if user_input is not None:
                print(f"\n{Colors.WHITE}[이전 시도 결과]{Colors.RESET}")
                print(f" ㆍ 유저 입력 : {Colors.RED}{user_input}{Colors.RESET}")
                print(f" ㆍ 전체 해석 : {Colors.WHITE}{full_korean}{Colors.RESET}")
                print(f" ㆍ 실제 정답 : {Colors.GREEN}{english_sentence}{Colors.RESET}")
                print(f"{Colors.CYAN}" + "-" * 60 + f"{Colors.RESET}")
            
            # API 호출
            tutor_response = call_gemini_tutor(model, english_sentence, full_korean, history)
            
            if not full_korean:
                full_korean = tutor_response.get("full_korean", "")

            # 튜터 피드백
            print(f"\n{Colors.YELLOW}[👨‍🏫 튜터 피드백]")
            print(tutor_response.get('guidance'))
            print(f"{Colors.RESET}")
            print(f"{Colors.CYAN}" + "─" * 60 + f"{Colors.RESET}")
            
            if tutor_response.get("is_correct") and correct_answer:
                is_solved = True
                print(f"\n{Colors.GREEN}🎉 축하합니다! 이 문장을 완벽히 마스터하셨습니다.{Colors.RESET}")
                input(f"\n{Colors.WHITE}[엔터키]를 누르면 다음 문제로 이동합니다...{Colors.RESET}")
                break

            type_eng_hint = tutor_response.get("typing_english_hint", "")
            type_kor_hint = tutor_response.get("typing_korean_hint", "")

            if type_eng_hint or type_kor_hint:
                disp_time = 0
                print(f"\n{Colors.MAGENTA}📢 [모드: 힌트 연습]{Colors.RESET}")
                print(f"{Colors.WHITE} 제공되는 부분 힌트를 바탕으로 문장을 다시 교정해보세요.{Colors.RESET}")
                input(f"{Colors.WHITE} 진행하려면 [엔터키 ⏎]를 누르십시오...{Colors.RESET}")
            else:
                disp_time = 10
                print(f"\n{Colors.RED}📢 [모드: 암기 퀴즈 - 최고 난이도]{Colors.RESET}")
                print(f"{Colors.WHITE} 10초 동안 전체 문장이 화면에 노출된 후 완전히 가려집니다.{Colors.RESET}")
                input(f"{Colors.WHITE} 준비가 완료되면 [엔터키 ⏎]를 누르십시오...{Colors.RESET}")

            if disp_time:
                clear_screen()
                print(f"{Colors.CYAN}▶️ [문항 {idx} / {len(sentences)}] 암기 단계 ━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}")
                print(f"\n{Colors.GREEN}[📝 제시 문장]\n▶ {english_sentence}{Colors.RESET}\n")
                print(f"{Colors.CYAN}" + "─" * 60 + f"{Colors.RESET}")
                countdown(int(disp_time))
                
                clear_screen()
                print(f"{Colors.CYAN}▶️ [문항 {idx} / {len(sentences)}] 타이핑 검증 ━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}")
                print(f"\n{Colors.RED}[최고 난이도 훈련 중 - 힌트 없음]{Colors.RESET}")
                print(f"{Colors.CYAN}" + "─" * 60 + f"{Colors.RESET}")
            else:
                clear_screen()
                print(f"{Colors.CYAN}▶️ [문항 {idx} / {len(sentences)}] 타이핑 검증 ━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}")
                print(f"\n{Colors.MAGENTA}[힌트 기반 재작성]{Colors.RESET}")
                print(f"{Colors.CYAN}" + "─" * 60 + f"{Colors.RESET}")
                if type_eng_hint:
                    print(f"{Colors.MAGENTA}🔤 영어 힌트   : {type_eng_hint}{Colors.RESET}")
                if type_kor_hint:
                    print(f"{Colors.MAGENTA}🇰🇷 한국어 힌트 : {type_kor_hint}{Colors.RESET}")
                print(f"{Colors.CYAN}" + "─" * 60 + f"{Colors.RESET}")
            
            user_input = input(f"\n{Colors.WHITE}✍️  문장 입력: {Colors.RESET}").strip()
            
            history.append({
                "gemini_guidance": tutor_response.get("guidance"),
                "user_answer": user_input
            })

            if user_input == english_sentence and not bool(type_eng_hint) and not bool(type_kor_hint):
                correct_answer = True

    clear_screen()
    print(f"{Colors.CYAN}============================================================{Colors.RESET}")
    print(f"{Colors.GREEN} 🎉 모든 훈련이 성공적으로 종료되었습니다! 고생하셨습니다. {Colors.RESET}")
    print(f"{Colors.CYAN}============================================================{Colors.RESET}")

if __name__ == "__main__":
    main()
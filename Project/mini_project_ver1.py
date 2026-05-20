import os
import random
import time


# 기본 설정
SYMBOLS= ["●", "■", "▲", "◆", "★"]
WIDTH= 100   #산점도 보드 가로
HEIGHT= 20   #산점도 보드 세로
total_score= 0  #합산 점수
N_BACK= 2  #2-back
SCORE_PER_HIT= 2  #턴당 점수
score1= 0  # 1번 게임 점수 저장
score2= 0  # 2번 게임 점수 저장

def clear():
    os.system("cls") # 윈도우는 nt, 리눅스는 posix

# =========================
# 1번 게임: 2-back 특수기호
# =========================
def N_back():
    global total_score

    clear()
    print("1. 2-back 게임")
    print(f"특수기호가 한 번씩 표시됩니다.")
    print(f"기호가 사라진 후, 지금 기호가 {N_BACK}턴 전 기호와 같으면 S, 다르면 D")
    print(f"(처음 {N_BACK}턴은 비교 대상이 없으므로 입력하지 않습니다.)")
    print(f"\n점수: 맞은 개수 × {SCORE_PER_HIT}점 (최대 {(10 - N_BACK) * SCORE_PER_HIT}점)")
    input("\n엔터 누르세요")

    sequence= []   # 지금까지 나온 기호 순서 기록
    correct= 0     # 맞힌 횟수
    total_judged= 0  # 판정된 총 횟수

    for turn in range(1, 11):  # 1턴부터 10턴까지
        symbol= random.choice(SYMBOLS)  #기호 무작위 선택
        sequence.append(symbol)  # 기록에 추가

        # 기호 표시
        clear()
        print(f"1. 특수기호 2-back 게임   턴: {turn}/{10}\n")
        print("\n" * 4)
        print(" " * 30 + symbol)
        time.sleep(0.35)  # 0.35초 동안 기호 표시

        # 깜빡임 효과
        clear()
        print(f"1. 특수기호 2-back 게임   턴: {turn}/{10}\n")
        print("\n" * 5)
        time.sleep(0.12)  #0.12초 동안 빈 화면

        # 처음 N_BACK(2)턴은 비교 대상이 없으므로 입력 없이 넘어감
        if turn <= N_BACK:
            clear()
            print(f"1. 특수기호 2-back 게임   턴: {turn}/{10}\n")
            print(f"\n  다음 턴을 기다리세요\n")
            time.sleep(1.0)
            continue

        target= sequence[turn- 1- N_BACK]  #2턴 전 기호 (리스트는 0-index라 -1 추가)
        is_same= (symbol== target)  #현재 기호와 N_BACK턴 전 기호가 같으면 True

        clear()
        print(f"1. 특수기호 2-back 게임   턴: {turn}/{10}\n")
        print(f"  지금 기호와 {N_BACK}턴 전 기호가 같은가")
        print(f"  S = 같다   D = 다르다\n")
        user= input("  입력: ").strip().upper()  #대소문자 구분 없이 처리

        # 정답 판별
        if (user== "S" and is_same) or (user== "D" and not is_same):
            print("정답!")
            correct+= 1
        else:
            answer= "S" if is_same else "D"
            print(f"  오답 ({N_BACK}턴 전 기호: {target})")
        total_judged+= 1
        time.sleep(1.0)  #대기

    # 최종 점수 계산
    score= correct* SCORE_PER_HIT  # 맞은 개수 × 2점
    total_score+= score

    clear()
    print("1번 게임 종료\n")
    print(f"  점수: {correct} × {SCORE_PER_HIT} = {score}점")
    print(f"\n현재 총점: {total_score}점")
    input("\n엔터를 누르면 계속합니다...")
    return score

# 산점도 
def make_dot_board(left_count, right_count, width=WIDTH, height=HEIGHT):
    board= [[" " for _ in range(width)] for _ in range(height)]  # height행 × width열 크기의 2차원 리스트를 공백으로 초기화
    mid= width // 2  # 보드 정중앙 x좌표 (구분선 위치)

    # 중앙에 세로 구분선 삽입
    for y in range(height):  # 0부터 height-1까지 반복하며 모든 행의 mid 위치에 "|" 삽입
        board[y][mid]= "|"

    used = set()  # 이미 점이 배치된 (x, y) 좌표를 저장하는 집합 (중복 배치 방지)

    # 왼쪽 점
    placed= 0
    while placed < left_count:  # 목표 개수(left_count)만큼 점이 배치될 때까지 반복
        x= random.randint(1, mid - 3)       # 왼쪽 영역 안에서 x 무작위 선택
        y= random.randint(0, height - 1)    # 보드 높이 안에서 y 무작위 선택
        if (x, y) not in used:  # 해당 좌표에 아직 점이 없으면 배치
            board[y][x] = "•"
            used.add((x, y))  # 사용한 좌표를 집합에 추가
            placed+= 1  # 배치 완료 카운트 증가

    # 오른쪽 점
    placed= 0
    while placed < right_count:  # 목표 개수(right_count)만큼 점이 배치될 때까지 반복
        x= random.randint(mid + 2, width - 2)  # 오른쪽 영역 안에서 x 무작위 선택
        y= random.randint(0, height - 1)
        if (x, y) not in used:  # 해당 좌표에 아직 점이 없으면 배치
            board[y][x]= "•"
            used.add((x, y))
            placed+= 1
    return board

def print_board(board):
    print("-" * WIDTH)  # 가로 구분선 출력
    for row in board:  # 2차원 리스트를 한 행씩 순회
        print("".join(row))  # 행의 문자들을 이어붙여 한 줄로 출력
    print("-" * WIDTH)

# =========================
# 2번 게임: 좌우 점 개수 비교
# =========================
def dot_game():
    global total_score
    score= 0

    for round_num in range(1, 6):  # 1부터 5까지 반복
        clear()
        print(f"2. 좌우 산점도 개수 비교  {round_num}/{5}")
        print("더 많은 쪽을 고르세요.\n")

        base= 12+ round_num* 2  #난이도 상승
        diff= random.randint(2, 5)  # 좌우 점 개수 차이 (2~5개)

        # 무작위로 어느 쪽을 더 많게 할지 결정
        if random.choice([True, False]):
            left_count= base+ diff   #왼쪽
            right_count= base
            answer= "a"
        else:
            left_count= base          #오른쪽
            right_count= base+ diff
            answer= "d"
        board = make_dot_board(left_count, right_count)  # 좌우 점 개수 넘겨 보드 생성
        print_board(board)
        time.sleep(0.5)

        # 화면 지우고 입력 프롬프트만 표시 (산점도 숨김)
        clear()
        print(f"2. 좌우 산점도 개수 비교  {round_num}/{5}")
        print()
        print("어느쪽이 더 많게")
        print()
        user = input("  선택 (A=왼쪽 / D=오른쪽): ").strip().lower()  # 입력을 소문자로 통일해서 A/a 구분 없이 처리

        # 정답 판별 및 점수 처리
        if user== answer:
            print("\n  정답!")
            score+= 10       # 이번 게임 점수에 10점 추가
            total_score+= 10  # 전역 합산 점수에도 10점 추가
        else:
            correct_side = "왼쪽 (A)" if answer == "a" else "오른쪽 (D)"  # answer가 "a"면 왼쪽, 아니면 오른쪽
            print(f"\n  오답 — 정답: {correct_side}")
            print(f"     실제 개수 → 왼쪽 {left_count}개, 오른쪽 {right_count}개")

        time.sleep(1.5)  #결과 확인 후 다음 라운드로 넘어가기 전 대기

    return score

# 결과 화면
def result():
    clear()
    print("게임 종료\n")
    print(f"1. 특수기호 2-back: {score1}점 / {(10 - N_BACK) * SCORE_PER_HIT}점")
    print(f"2. 좌우 산점도 개수 비교: {score2}점 / 50점")
    print(f"\n총점: {score1 + score2}점 / {(10 - N_BACK) * SCORE_PER_HIT + 50}점")
    print()

# =======================
# 메인 메뉴
# =========================
def main():
    global total_score, score1, score2

    while True:  # 종료를 선택하기 전까지 메뉴를 계속 반복
        clear()
        print("역량검사")
        print("1. 특수기호 2-back")
        print("2. 좌우 산점도 개수 비교")
        print("3. 종료\n")
        print(f"현재 점수 → 1번: {score1}점  2번: {score2}점  합계: {score1 + score2}점\n")

        menu = input("메뉴 선택: ").strip()

        if menu== "1":
            score1= N_back()  # 1번 게임 실행 후 점수 갱신
            total_score= score1 + score2
            result()
            input("\n엔터를 누르면 계속합니다...")

        elif menu== "2":
            score2= dot_game()  # 2번 게임 실행 후 점수 갱신
            total_score= score1 + score2
            result()
            input("\n엔터를 누르면 계속합니다...")

        elif menu== "3":
            clear()
            print("프로그램 종료")
            break  # while True 루프 탈출→ 프로그램 종료

        else:
            print("잘못된 입력입니다.")
            time.sleep(1)


if __name__== "__main__": 
    main()
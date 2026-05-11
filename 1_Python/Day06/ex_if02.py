## ========================================================
## [예시] 조건 1개인 경우
## => 점수가 60이상이면 합격 출력, 그렇지 않으면 불합격 출력
## -> (1) 입력데이터 좌우 공백 제거 후 저장

jumsu= input("점수를 입력하세요:").strip()
if len(jumsu):
## --(2) str=> int 형변환: int(jumsu)
    if jumsu.isdecimal():
        jumsu= int(jumsu)

    

    ##--(3) 합격& 불합격 검사 및 결과 출력

        if jumsu>=60:
            print(f"{jumsu}점 합격입니다.")
        else:
            print(f"{jumsu}점, 다시 도전 하세요.")
    else:
        print(f"{jumsu}: 숫자 0~9 만 입력해야 합니다")

else:
    print("입력된 데이터가 없습니다")

# =============================================
## 입력된 데이터가 있고, 그리고 그 데이터가 숫자인 경우만 합격/ 불합격
## 입력 내용이 없거나 올바른 데이터가 아닙니다.
## => 연산자: 2개 조건 모두 만족/ True=> and

if len(jumsu) and jumsu.isdecimal():
    # 형변환
    jumsu= int(jumsu)
    # 합격/ 불합격 출력
    if jumsu>= 60: print(f"{jumsu} 합격")
    else: print("다시 도전하세요")
else:
    # 입력 안 했거나 또는 유효하지 않은 데이터
    print(f"{jumsu}: 숫자 0~9 만 입력해야 합니다")
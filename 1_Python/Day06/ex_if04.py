## ========================================================
## [예시] 정수가 60이상이면 합격, 그렇지 않으면 불합격
jumsu= 60

if jumsu>=60:
    print("합격")
else:
    print("불합격")

## [예시] 짝수& 홀수 판별 출력
    # 숫자 %2 나머지----> 2의 배수 0, 2의 배수가 아닌 경우 1

num=4

if num %2:
    print(f"{num}은 홀수")
else:
    print(f"{num}은 짝수")


if not num %2:
    print(f"{num}은 짝수")
else:
    print(f"{num}은 홀수")
## ========================================================
## [예시] 나이가 20살 이상이거나 성별이 여자인 경우 찾아서 왼쪽으로 이동하세요
##        아닌 경우 오른쪽 이동
 
## --(1) input 2개 받아야 함.
info= input("나이와 성별 입력(예: 30 여자):").strip()

## --(2) 입력데이터 존재 여부 체크: len()
if len(info):
    # 나이와 성별 분리: split()=> list에 담아서 보관
    age, gender= info.split()
    if age.isdecimal() and gender.isalpha():
        # 나이와 성별 조건에 따른 출력
        age= int(age)
        if age>=20 or gender=='여자':
            print("왼쪽으로 이동하세요")
        else:
            print("오른쪽으로 이동하세요")
    else:
        print("유효한 데이터가 아닙니다")
    # 조건 검사에 따른 출력
else:
    print("입력된 데이터가 없습니다!")
    
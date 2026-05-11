## ========================================================
## 컴프리헨션(Comprehension) 
## -> 반복문 + 조건문 => 컨테이너 자료형 생성
## ========================================================
## --------------------------------------------------------
## [형식4] 반복문으로 컨테이너 자료형 생성
##        [ 원소 if 조건 else 원소  for 원소 in 반복가능한자료형 if 조건식  ]
##          --- 원소 표현 결정 --   ----- 원소 추출 ---------  -- 필터링--
## --------------------------------------------------------
## orgList의 원소 중에 짝수값 가진 원소만 사용
##                   짝수값이 6이상이면 '큰수'로 저장, 미만이면 그래도 저장
##                   새로운 newList 생성
orgList = [1, 2, 3, 4, 5, 6, 7, 8] 
print(f'orgList => {orgList}')

## ----------------
## => 기본 방식
## ----------------
newList = []
for num in orgList:
    if not num % 2:
        if num>=6:
            newList.append("큰수")
        else:
            newList.append(num)
    
print(f'기본   newList => {newList}')

## ----------------
## => 간결하게 처리 : 컴프리헨션 
## ----------------
newList = [ num for num in orgList if not num%2 ]
print(f'컴프리 newList => {newList}')

newList = [ '큰수' if num>=6 else num for num in orgList if not num%2 ]
print(f'컴프리 newList => {newList}')
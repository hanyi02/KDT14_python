## ===================================================
## 컨테이너 자료형-[1] 순서있는 자료형- LIST
## ==> 다양한 종류의 여러개 데이터 저장 가능함
## ==> 데이터 추가/삭제/ 변경 가능
## ==> 생성 문법: 변수명= [데이터1, 데이터2, 데이터3,...]
#                변수명= list([데이터1, 데이터2, 데이터3,...])
## ===================================================

# 5과목 점수 저장
sub1= 90
sub2= 89
sub3= 95
sub4= 88
sub5= 92

## 리스트로 저장
scores= [90, 89, 95, 88, 92]

scores2= list([90, 89, 95, 88, 92])  
print(scores)
print(scores2)

print(type(scores)) #<class 'list'>
print(type(scores2)) #<class 'list'>

datas1=[]
datas2=["홍길동", 20, 175.5, True, [1, 2, 3], (4, 5), {"a":1, "b":2} ]

print(f'type(datas1): {type(datas1)}, {datas1}')
print(f'type(datas2): {type(datas2)}, {datas2}')

print(f"len(datas1): {len(datas1)}개, {datas1}") 
print(f"len(datas2): {len(datas2)}개, {datas2}")

## ==================================================
## 내장함수: max(), min()
# ★ str 데이터는 문자 1개 1개의 코드값을 비교함
##==================================================

datas3=[2, -4, 5, 0, 3, -1]
datas4=["apple", "banana", "cherry", "date", "fig", "grape"]

print(f"max(datas3): {max(datas3)}, min(datas3): {min(datas3)}")
print(f"max(datas4): {max(datas4)}, min(datas4): {min(datas4)}")



## ==================================================
## 내장함수: sum(변수명)-> 데이터/ 요소들의 합계 반환 함수
# ★ sum함수는 수치 데이터만 가능함
##==================================================
datas3=[2, -4, 5, 0, 3, -1]
datas4=["apple", "banana", "cherry", "date", "fig", "grape"]

print(f"sum(datas3): {sum(datas3)}")


## ==================================================
## 내장함수: sorted(변수명)-> 데이터/ 요소들의 정렬 반환 함수
# ★ sorted함수는 모든 데이터 유형과 사용 가능함
##==================================================

print(f"sorted(datas3): {sorted(datas3, reverse=True)}")
print(f"sorted(datas3): {sorted(datas3)}")


## ==================================================
## 내장함수: range(시작값, 끝값+1, 간격)-> 데이터 범위 생성 후 반환 함수
# ★ range 함수는 정수형 데이터만 사용 가능함
##==================================================

datas1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
datas2= range(1, 11) #range(시작값, 끝값+1)
print(f"datas1: {datas1}, {len(datas1)}개, type(datas1): {type(datas1)}")
print(f"datas2: {datas2}, {len(list(datas2))}개, type(datas2): {type(datas2)}")

datas1=[3, 6, 9, 12, 15]
datas2= range(0,11,3) #range(시작값, 끝값+1, 간격)
datas2= list(range(0,11,3)) #range(시작값, 끝값+1, 간격)
print(f"datas2: {datas2}, {len(list(datas2))}개, type(datas2): {type(datas2)}")

## 퀴즈
#50부터 1까지 1씩 감소하는 데이터 범위를 생성하여 리스트로 반환하세요.
print(list(range(50, 0, -1)))
## ======================================================
## 컨테이너 자료형 - [4] Dict 자료형
##
## 다양한 dict 데이터 생성 방식
## ======================================================
## 유용한 내장함수 zip() : 같은 위치에 있는 데이터를 하나로 묶어주는 기능
names = ["홍", "박", "김"]
jumsu = [98,   100]

##=> 반복가능한 데이터들을 묶음 처리 
result = zip(names, jumsu)         
#result = zip(names, jumsu, range(3))
print(f"result : {result},  {type(result)}")

##=> 보기 방식으로 형변환 필요
result = list(result)
print(f"result : {result},  {type(result)}")

result = tuple(result)
print(f"result : {result},  {type(result)}")

# 단!! dict는 2개까지만 가능. 3개이상은 K:V로 변환 불가!!!
result = dict(result)   
print(f"result : {result},  {type(result)}")
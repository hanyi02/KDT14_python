## ======================================================
## 컨테이너 자료형 - [5] Set 
##
## - 중복 데이터는 저장되지 않음!
## - 원소/요소 식별용 인덱스 없음!
## - 표현방식 : { 원소1, 원소2, ..., 원소n }
## - 빈  집합 : { } => 빈 dict,  set() => 빈 set
## ======================================================
## ------------------------------------------------------
## Set 생성
## ------------------------------------------------------
dataSet = {1,1,1,1,1,1,1,1,1,1}
print(f" dataSet : {len(dataSet)}개,  {type(dataSet)} , {dataSet} ")

dataSet = {1,12, 6, 9, 2, 1,1,1}
print(f" dataSet : {len(dataSet)}개,  {type(dataSet)} , {dataSet} ")


## => 빈 set 객체 생성 
dataSet1 = {}         ## <== empty dict 
dataSet2 = set()      ## <== empty set 

print(f" dataSet1 : {len(dataSet1)}개,  {type(dataSet1)} , {dataSet1} ")
print(f" dataSet2 : {len(dataSet2)}개,  {type(dataSet2)} , {dataSet2} ")
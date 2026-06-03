## ======================================================
## 컨테이너 자료형 - [5] Set 
##
## - Set 자료형 전용 함수 즉, 메서드 
## ======================================================
## -----------------------------------------------------------------
## Set 생성
## -----------------------------------------------------------------
dataSet = {1, 3, 5, 7, 9, 1, 3, 5, 7, 9}
print(f" dataSet : {len(dataSet)}개,  {type(dataSet)} , {dataSet} ")

## -----------------------------------------------------------------
## 원소/요소 1개 추가 메서드 : add(데이터)
## -> 이미 존재하는 데이터이면 추가하지 않음!. 에러 발생 X
## -----------------------------------------------------------------
dataSet.add(3)
print(f" dataSet : {len(dataSet)}개,  {type(dataSet)} , {dataSet} ")

dataSet.add(11)
dataSet.add(8)
dataSet.add(1)
dataSet.add(8)
dataSet.add(11)
print(f" dataSet : {len(dataSet)}개,  {type(dataSet)} , {dataSet} ")

## -----------------------------------------------------------------
## 원소/요소 여러 개 추가 메서드 : update(반복이 가능한 데이터)
## -> 이미 존재하는 데이터이면 추가하지 않음!. 에러 발생 X
## -----------------------------------------------------------------
dataSet.update([1,2,3,4,5,6,7,8,9,10])
print(f" dataSet : {len(dataSet)}개,  {type(dataSet)} , {dataSet} ")

dataSet.update("Gooood")   ## str타입으로 원소가 6개 존재. 중복 요소 제거 추가
print(f" dataSet : {len(dataSet)}개,  {type(dataSet)} , {dataSet} ")

dataSet.update(["Gooood"]) ## list타입으로 원소가 1개 존재.
print(f" dataSet : {len(dataSet)}개,  {type(dataSet)} , {dataSet} ")

## -----------------------------------------------------------------
## 원소/요소 삭제 메서드 : remove(원소/데이터)
## {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'G', 'Gooood', 'd', 'o'} 
## -----------------------------------------------------------------
dataSet.remove(1)
print(f" dataSet : {len(dataSet)}개, {dataSet} ")

dataSet.remove('Gooood')
print(f" dataSet : {len(dataSet)}개, {dataSet} ")

## 없으면 Error 발생
# dataSet.remove('Gooood')
# print(f" dataSet : {len(dataSet)}개, {dataSet} ")


## -----------------------------------------------------------------
## 원소/요소 꺼내서 제거하는 메서드 : pop()
## -----------------------------------------------------------------
data = dataSet.pop()
print(f" dataSet : {len(dataSet)}개, {dataSet}  꺼낸 데이터 : {data}")

data = dataSet.pop()
print(f" dataSet : {len(dataSet)}개, {dataSet}  꺼낸 데이터 : {data}")

data = dataSet.pop()
print(f" dataSet : {len(dataSet)}개, {dataSet}  꺼낸 데이터 : {data}")

data = dataSet.pop()
print(f" dataSet : {len(dataSet)}개, {dataSet}  꺼낸 데이터 : {data}")

data = dataSet.pop()
print(f" dataSet : {len(dataSet)}개, {dataSet}  꺼낸 데이터 : {data}")

data = dataSet.pop()
print(f" dataSet : {len(dataSet)}개, {dataSet}  꺼낸 데이터 : {data}")
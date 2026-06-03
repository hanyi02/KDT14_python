## ========================================================
## 컴프리헨션(Comprehension) 
## -> 반복문 + 조건문 => 컨테이너 자료형 생성
## ========================================================
## --------------------------------------------------------
## Dict 자료형과 컴프리헨션
## -> [키] { 조건부표현식  for 원소 in 반복가능한자료형   필터링 }
## -> [키,값] { 조건부표현식  for 원소 in 반복가능한자료형.items()   필터링 }
## --------------------------------------------------------
orgDict = {'Kor':98, 'Eng':100, 'Art':78, 'Mus':45}
print(f'orgDict => {orgDict}')

## ----------------
## => 간결하게 처리 : 컴프리헨션 
## ----------------
## 과목별 점수를 100으로 나눈 값을 저장하는 dict
newDict = { key:orgDict[key]/100  for key in orgDict }
newDict = { k:v/100               for k, v in orgDict.items() }

print(f'newDict => {newDict}')

## 점수가 80점이상인 과목만 저장하는 dict 
## => 필터링 
newDict = { key:orgDict[key]  for key in orgDict           if orgDict[key]>=80 }
newDict = { k:v               for k, v in orgDict.items()  if v>=80 }

print(f'newDict => {newDict}')


## 점수가 80이상이면 합격, 아니면 불합격이라고 저장하는 dict
newDict = { key:"합격" if orgDict[key] >=80 else "불합격"  for key in orgDict }
newDict = { k:"합격"   if v>=80 else "불합격"              for k, v in orgDict.items() }

print(f'newDict => {newDict}')

## -------------------------------------------
## 점수에따라 학점 A,B,C,D,F로 저장하는 dict
newDict={}
for k, v in orgDict.items():
    if v>=90:       v = "A"
    elif v>=80:     v = "B"
    elif v>=70:     v = "C"
    elif v>=60:     v = "D"
    else:           v = "F"
    newDict[k]=v

print(f'newDict => {newDict}')

## => 다중 조건문 ---> 조건부 표현식
newDict={}
for k, v in orgDict.items():
    v = "A" if v>=90 else 'B' if v>=80 else 'C' if v>=70 else 'D' if v>=60 else 'F'
    newDict[k]=v

print(f'newDict => {newDict}')

newDict = { k:"A" if v>=90 else 'B' if v>=80 else 'C' if v>=70 else 'D' if v>=60 else 'F' for k, v in orgDict.items() }

print(f'newDict => {newDict}')

print=100

print("GOODs")
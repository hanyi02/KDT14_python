## ======================================================
## 컨테이너 자료형 - [4] Dict 자료형
##
## Dict와 추가 메서드들 살펴보기 
## ======================================================
## ------------------------------------------------------
## dict에 원소/요소 읽어오는 메서드  => get()
## ------------------------------------------------------
## 예시 dict 생성
dataDict = {1:100, 2:98, 3:100}
print(f"dataDict : {len(dataDict)}개,  {dataDict}")

## => 키 존재할 경우
value=dataDict.get(2)
print(f"get(2)      : {value} | {dataDict}")
print(f"dataDict[2] : {dataDict[2]} | {dataDict}")

## => 키 존재하지 않을 경우
value=dataDict.get('A' , '존재하지 않는 키 입니다.')
print(f"get('A      : {value} | {dataDict}")
##print(f"dataDict['A'] : {dataDict['A']} | {dataDict}")  #Key ERROR

value=dataDict.get(1, '존재하지 않는 키 입니다.')
print(f"get(1)      : {value} | {dataDict}")

## ------------------------------------------------------
## 키 정보만 가지고 dict 생성 메서드 : fromkeys()
## ------------------------------------------------------
key= range(10, 100,10)
dataDict = dict.fromkeys(key)
print(f"dataDict : {len(dataDict)}개,  {dataDict}")

dataDict = dict.fromkeys(key, 0)
print(f"dataDict : {len(dataDict)}개,  {dataDict}")
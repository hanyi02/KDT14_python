## ======================================================
## 컨테이너 자료형 - [4] Dict 자료형
##
## Dict와 추가 메서드들 살펴보기 
## ======================================================
## ------------------------------------------------------
## dict에 원소/요소 추가 메서드 => 형태: 키와 값 쌍으로 추가
## -> setdefault()메서드
## -> update() 메서드
## ------------------------------------------------------
## 예시 dict 생성
stdDict = { "홍":3.9, "마":4.1, "권":2.7 }

## => 원소 추가하기 (1)
stdDict.setdefault("박")
print(f"원소 : {len(stdDict)}개,  {stdDict} ")

stdDict.setdefault("베", 3.3)
print(f"원소 : {len(stdDict)}개,  {stdDict} ")

## 존재하는 키 추가 시 적용되지 않음/추가되지 않음 !!!
stdDict.setdefault("박", 4.3)
print(f"원소 : {len(stdDict)}개,  {stdDict} ")

## => 원소 추가하기 (2) update() 1개 ~ 여러개 추가 가능 
## 존재하지 않는 키 추가. 
## ★주의: 키가 str 타입만 가능. str 타입이지만 '', "" 감싸지 않음 => Why? 함수 문법 규칙에 맞춤
stdDict.update(K=2.9, P=3.1, C=4.0)
print(f"원소 : {len(stdDict)}개,  {stdDict} ")

## dict 형식으로 추가 
stdDict.update( {"A":1.3, "Z":3.9} )
print(f"원소 : {len(stdDict)}개,  {stdDict} ")


## 키와값 묶흠 형식으로 추가 
stdDict.update([ ['김', 3.2], ['이', 4.4] ] )
print(f"원소 : {len(stdDict)}개,  {stdDict} ")


## zip 형식으로 추가 
stdDict.update( zip(['최', '제갈', '남궁'], [3.0, 2.9, 2.8]) )
print(f"원소 : {len(stdDict)}개,  {stdDict} ")


## ------------------------------------------------------
## dict에 원소/요소 값 변경 메서드 => update(키와 값 묶음) 메서드
##                                존재하는 키면 값을 수정해줌
##                                여러개 변경도 가능함!
## ------------------------------------------------------
## '홍': 3.9, '마': 4.1, '권': 2.7, '박': None => 4개 원소 값 변경
stdDict['홍'] = 3.7
stdDict['마'] = 4.4
stdDict['권'] = 3.7
stdDict['박'] = 1.3
print(f"원소 : {len(stdDict)}개,  {stdDict} ")

## => 여러개 한꺼번에 변경/업데이트 
stdDict.update( zip(['홍','마','권','박'],  [2.2, 3.3, 1.1, 4.4]) )
print(f"원소 : {len(stdDict)}개,  {stdDict} ")


## ------------------------------------------------------
## dict에 원소/요소 삭제 메서드 => pop(키)   키에 해당하는 원소 꺼내서 값만 반환
##                              popitem() 마지막 원소를 꺼내서 (키, 값) 형태 반환
## dict에서 원소를 꺼냈기 때문에 제거 되는 것!!!
## ------------------------------------------------------
## (1) 특정 키의 원소 꺼내서 값만 가져오기
value = stdDict.pop('홍')
print(f"원소 : {len(stdDict)}개,  {stdDict}\n꺼낸 원소 값 : {value}")

value = stdDict.pop('마')
value = stdDict.pop('남궁')
value = stdDict.pop('K')
value = stdDict.pop('P')
print(f"원소 : {len(stdDict)}개,  {stdDict}\n꺼낸 원소 값 : {value}")


## (2) 마지막 원소 꺼내서 (키, 값)형태로 가져오기
result = stdDict.popitem()
print(f"원소 : {len(stdDict)}개,  {stdDict}\n꺼낸 요소 : {result}")

result = stdDict.popitem()
print(f"원소 : {len(stdDict)}개,  {stdDict}\n꺼낸 요소 : {result}")

result = stdDict.popitem()
print(f"원소 : {len(stdDict)}개,  {stdDict}\n꺼낸 요소 : {result}")


## (3) 특정 키의 원소 삭제  명령어 : del 변수명[키],  del( 변수명[키] )
del stdDict['권']
del( stdDict['베']) 
print(f"원소 : {len(stdDict)}개,  {stdDict}")


## (4) 모든 원소 삭제  메서드 : clear() => 빈 dict 남음!!
stdDict.clear()
print(f"원소 : {len(stdDict)}개,  {stdDict}")
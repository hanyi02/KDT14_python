## ======================================================
## 컨테이너 자료형 - [1] 순서있는 자료형 List
## 
## -> 다양한 내장함수 활용 
## =======================================================
## list 생성하기 => 다양한 데이터 
## =======================================================
datas1 = [] 
datas2 = ["Hello", 123, 0.98, False] 
datas3 = [ [100, 200, 300],  [ 4, 9, 9, 2, 2, 4], "Good" ]

## ----------------------
## 내장함수: type( 변수명 ) -> 저장 데이터의 타입 확인
## ----------------------
print(f"type(datas1) : {type(datas1)},  {datas1}" )
print(f"type(datas2) : {type(datas2)},  {datas2}" )
print(f"type(datas3) : {type(datas3)},  {datas3}" )

## ----------------------
## 내장함수: len( 변수명 ) -> 데이터/요소 개수 반환 함수
## ----------------------
print(f"len(datas1) : {len(datas1)}개,  {datas1}" )
print(f"len(datas2) : {len(datas2)}개,  {datas2}" )
print(f"len(datas3) : {len(datas3)}개,  {datas3}" )


## ----------------------
## 내장함수: max( 변수명 ) -> 데이터/요소 중 최고값 데이터
##          min( 변수명 ) -> 데이터/요소 중 최소값 데이터
##
## ★str데이터는 문자 1개 1개의 코드값을 비교함!!
## ----------------------
datas2 = [7, 9, -3, 10, 0.002, 99.999]
datas3 = ["Abc", "APPle", "anaconda", "zoo"]

#print(f"max(datas1) : {max(datas1)},  min(datas1) : {min(datas1)}" )
print(f"max(datas2) : {max(datas2)},  min(datas2) : {min(datas2)}" )
print(f"max(datas3) : {max(datas3)},  min(datas3) : {min(datas3)}" )


## ----------------------
## 내장함수: sum( 변수명 ) -> 데이터/요소들의 합계 반환 함수
##
## ★ sum 함수는 수치 데이터만 가능함!!!
## ----------------------
print(f"sum(datas1) : {sum(datas1)},  {datas1}" )

print(f"sum(datas2) : {sum(datas2)},  {datas2}" )
#print(f"sum(datas3) : {sum(datas3)},  {datas3}" )
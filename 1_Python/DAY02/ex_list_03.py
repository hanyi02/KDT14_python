## ======================================================
## 컨테이너 자료형 - [1] 순서있는 자료형 List
## 
## -> 다양한 내장함수 활용 
## =======================================================
## list 생성하기 => 다양한 데이터 
## =======================================================
datas1 = [] 
datas2 = [7, 9, -3, 10, 0.002, 99.999]
datas3 = ["Abc", "APPle", "anaconda", "zoo"]

## ----------------------
## 내장함수: sorted( 변수명 ) -> 데이터/요소들 정렬 후 반환 함수
##
## ★ 항상 list로 반환
## ----------------------
print("[오름차순 정렬 : 작은 값--->큰 값]")
print(f"sorted(datas1) : {sorted(datas1)}, {datas1}" )
print(f"sorted(datas2) : {sorted(datas2)}, {datas2}" )
print(f"sorted(datas3) : {sorted(datas3)}, {datas3}" )

print("[내림차순 정렬 : 큰 값--->작은 값]")
print(f"sorted(datas1) : {sorted(datas1, reverse=True)}, {datas1}" )
print(f"sorted(datas2) : {sorted(datas2, reverse=True)}, {datas2}" )
print(f"sorted(datas3) : {sorted(datas3, reverse=True)}, {datas3}" )

## ----------------------
## 내장함수: range(시작값, 끝값+1, 간격 ) -> 데이터 범위 생성 후 반환 함수
##
## ★ 많은 데이터 생성 시 사용하는 함수
##    -> 데이터 범위 객체/타입 생성
##    -> 데이터 범위 : 시작값 <= ~ < 끝값+1
## 예) 1부터 1000까지  OR 1 ~ 1000  ==> [1,2,3,4,5,6,7,8,9,..... , 1000]  
##                                ==>  range(1,1001)
## ----------------------
## 1~10까지 숫자 데이터 저장
## ----------------------
datas1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
datas2 = range(1, 11)    # 1<= ~ <11

print(f"datas1 : {datas1},  {len(datas1)}개,  {type(datas1)}")
print(f"datas2 : {datas2},  {len(datas2)}개,  {type(datas2)}")

## ----------------------
## 1~1000000000까지 숫자 데이터 저장
## ----------------------
#datas1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, .... , 1000000000]
datas2 = range(1, 1000000001)    # 1<= ~ <1000000001

print(f"datas2 : {datas2},  {len(datas2)}개,  {type(datas2)}")


## ----------------------
## 1~30까지 숫자 중 3의 배수만 데이터 저장
## ----------------------
datas1 = [3,6,9,12,15,18,21,24,27,30]
datas2 = range(3, 31, 3)    # 3<= ~ <31, 간격 3씩

print(f"datas1 : {datas1},  {len(datas1)}개,  {type(datas1)}")
print(f"datas2 : {datas2},  {len(datas2)}개,  {type(datas2)}, {list( datas2 )}")

## ----------------------
## [퀴즈] 50 ~ 1까지 범위의 숫자를 출력하세요.
##       단, range()함수 사용하세요.
## ----------------------
datas2=range(50, 0, -1)
print(f"datas2 : {datas2},  {len(datas2)}개,  {type(datas2)}, {list( datas2 )}")

datas2=range(1, 51)
print(f"datas2 : {datas2},  {len(datas2)}개,  {type(datas2)}, { sorted(list( datas2 ), reverse=True) }")

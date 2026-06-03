## ==================================================
## 컨테이너 자료형 - [1] List
##
## * List 전용 메서드 : List 자료형에서만 사용 가능한 함수
## * 사용 방법/문법   : List객체변수명.메서드명()
## ==================================================
## ----------------
## List 생성
## ----------------
## 1~30 범위에서 7의 배수로만 구성된 데이터 
## 7, 14, 21, 28, 32,.....
datas = range(7, 31, 7)     ## 타입이 range 즉, 범위 객체 
datas = list(datas)         ## range => list 형변환
datas.append(8)
datas.append(7)
datas.append(7)
datas.append(1)
datas.append(7)
print(datas, len(datas))

## -----------------------------------------------
## List 전용 함수 즉, 메서드 사용
## -----------------------------------------------
## (1) 원소/요소 인덱스 찾기 -> 변수명.index(데이터값)
##     * 첫 번째 발견되는 데이터의 인덱스 반환
##     * 존재하지 않으면 Error 반환
## -----------------------------------------------
## 존재하지 않는 데이터의 인덱스 => Error : 멤버 연산자 체크 필요
if 100 in datas:
    datas.index(100)
    print(f"데이터 100의 인덱스 : {datas.index(100)},  {datas}") 
else:
    print("100은 존재하는 원소가 아닙니다.")

## 1개만 존재하는 데이터의 인덱스
idx = datas.index(21)
print(f"데이터 21의 인덱스 : {idx},  {datas}") 


## 여러 개 존재하는 데이터의 인덱스 
## --> 제일 먼저 발견된 데이터의 인덱스만 반환
idx = datas.index(7)
print(f"데이터 첫번째 7의 인덱스 : {idx},  {datas}") 

idx = datas.index(7, idx+1)
print(f"데이터 두번째 7의 인덱스 : {idx},  {datas}") 

idx = datas.index(7, idx+1)
print(f"데이터 세번째 7의 인덱스 : {idx},  {datas}") 

idx = datas.index(7, idx+1)
print(f"데이터 네번째 7의 인덱스 : {idx},  {datas}") 


## -----------------------------------------------
## (2) 원소/요소 데이터 값의 개수 -> 변수명.count(데이터값)
##     * 해당 데이터 값이 list에 없으면 0 반환
## -----------------------------------------------
cnt=datas.count(33)
print(f"데이터 33의 존재 개수 : {cnt}개,  {datas}") 

cnt=datas.count(7)
print(f"데이터 7의 존재 개수 : {cnt}개,  {datas}") 


## -----------------------------------------------
## (3) 원소/요소 개수 증가/확장 -> 변수명.extend(반복타입객체)
##     * List의 원소가 증가 늘어남 => 커짐. 확장
##     * 반복가능타입/Iterable타입 : for ~ in 가능한 타입
##                                 인덱스 있는 타입들 해당됨
## -----------------------------------------------
datas.extend([32])
print(f"datas 원소 개수 : {len(datas)}개,  {datas}")

datas.extend([3, 2, -8, 5, 3, 1, 9, 99])
print(f"datas 원소 개수 : {len(datas)}개,  {datas}")

datas.extend(datas)      ## list
print(f"datas 원소 개수 : {len(datas)}개,  {datas}")

datas.extend((111,222))  ## tuple
print(f"datas 원소 개수 : {len(datas)}개,  {datas}")

datas.extend("Good")      ## str => 추가 원소 개수 4개
print(f"datas 원소 개수 : {len(datas)}개,  {datas}")

datas.extend(["Good"])    ## list => 추가 원소 개수 1개
print(f"datas 원소 개수 : {len(datas)}개,  {datas}")

## ---------------------------------------------------------
##
## 매직코드/매직메서드 : Python에 특수한 기능을 부여해 놓은 것들
## _ _메서드이름_ _( ),  _ _변수이름_ _ 
##
## ---------------------------------------------------------
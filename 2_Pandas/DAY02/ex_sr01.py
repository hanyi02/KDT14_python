## ===========================================
##          Series 인스턴스 생성 
## -------------------------------------------
## * Pandas에서 1줄 데이터를 저장하는 데이터 타입
## * 구성 : 원소식별 인덱스 + 데이터 
## * 함수 : Series(data) 
## ===========================================
## -------------------------------------------
## [1] 모듈 로딩
## -------------------------------------------
import pandas as pd 


## -------------------------------------------
## [2] Seires 인스턴스 생성
## -------------------------------------------
## 데이터 준비
data1 = [11,33,55,77]
data2 = [True, 9.8, "Happy", 2026, 100]

## Series 인스턴스 생성
sr1 = pd.Series(data1)
sr2 = pd.Series(data2) 

## Series 인스턴스 정보 확인 => sr1
print(f"--[Series 속성들]")
print(f'index  : {sr1.index}')      ## 원소 식별 번호
print(f'values : {sr1.values}')     ## 원소에 저장된 데이터들
print(f'shape  : {sr1.shape}')      ## 1줄 시리즈의 형태 모양. 튜플로 표기
print(f'ndim   : {sr1.ndim}')       ## 차원(1,2, ..., N) 정보
print(f'dtype  : {sr1.dtype}')      ## 원소의 데이터 타입 정보
print(f'name   : {sr1.name}')       ## 메타 정보/부가 정보로 이름

print(f"\n--[Series형태 출력]")
print(sr1)  


## Series 인스턴스 정보 확인 => sr2
print(f"--[Series 속성들]")
print(f'index  : {sr2.index}')      ## 원소 식별 번호
print(f'values : {sr2.values}')     ## 원소에 저장된 데이터들
print(f'shape  : {sr2.shape}')      ## 1줄 시리즈의 형태 모양. 튜플로 표기
print(f'ndim   : {sr2.ndim}')       ## 차원(1,2, ..., N) 정보
print(f'dtype  : {sr2.dtype}')      ## 원소의 데이터 타입 정보
print(f'name   : {sr2.name}')       ## 메타 정보/부가 정보로 이름

print(f"\n--[Series형태 출력]")
print(sr2)
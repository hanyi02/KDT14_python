## ===============================================
##              통계 관련 메서드들
## ===============================================
## [1] 모듈 로딩
## ----------------------------------
import sys
sys.path.append(r'D:\KDT\VS_KDT_14\[2]_PANDAS\comm')
import utils
import pandas as pd 

## ----------------------------------
## [2] 데이터 준비
## ----------------------------------
DATA_FILE = '../DATA/iris.csv'

## ----------------------------------
## [3] CSV >>> DataFrame 변환 저장
## ----------------------------------
irisDF = pd.read_csv(DATA_FILE)

## ----------------------------------
## [4] DataFrame 기본 정보 확인
## ----------------------------------
#utils.data_info(irisDF)

## ----------------------------------
## [5] 통계 관련 메서드들
## ----------------------------------
## => DataFrame에 전체 컬럼별 데이터 수 반환 : count()
##    axis=0 : 각각의 행 단위 계산 => 결과 열
##    axis=1 : 각가의 열 단위 계산 => 결과 행
## ----------------------------------
cntSR = irisDF.count(axis=0)
print(f"axis=0 각 컬럼의 NA가 아닌 데이터 수 ===\n{cntSR}")

cntSR = irisDF.count(axis=1)
print(f"axis=1 각 행의 NA가 아닌 데이터 수  ===\n{cntSR}")

## -----------------------------------------------------
## => 행의 모든 값이 동일한 개수 반환 : value_counts()
## -----------------------------------------------------
vcntSR = irisDF.value_counts()
print(f" {vcntSR}")

## => 특정 컬럼의 데이터별 개수 
vcntSR = irisDF.variety.value_counts()
vcntSR = irisDF['variety'].value_counts()
print(f" {vcntSR}")

vcntSR = irisDF['petal.width'].value_counts()
print(f" {vcntSR}")

## -----------------------------------------------------
## => 컬럼별 데이터/값의 종류 개수 즉, 고유값 반환  : unique()
## => DataFrame에는 없음!! Series.unique() 
## -----------------------------------------------------
## variety 컬럼의 데이터/값의 종류 => 고유값
ret = irisDF['variety'].unique()
print(f"variety 컬럼의 고유값 : { ret }, 원소 개수 : {len(irisDF['variety'])}개")

print(f"variety 컬럼의 고유값별 원소 개수 :\n{irisDF['variety'].value_counts()}")


ret = irisDF['petal.width'].unique()
print(f"petal.width 컬럼의 고유값 : { ret }, 원소 개수 : {len(irisDF['petal.width'])}개")

print(f"petal.width 컬럼의 고유값별 원소 개수 :\n{irisDF['petal.width'].value_counts()}")
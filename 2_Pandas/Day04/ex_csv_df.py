## ===============================================
## CSV 데이터 파일 >>> DataFrame 변환 로딩
## ===============================================
## [1] 모듈 로딩
## ----------------------------------
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
## => 요약정보 출력
print("\n-> 요약정보")
irisDF.info()   

## => 실제 데이터 확인
print("\n-> 실제 데이터", irisDF.head(2), irisDF.tail(2), sep='\n')


## => 컬럼별 통계 정보 확인
print("\n-> 수치 컬럼별 정보", irisDF.describe(), sep='\n')
print("\n-> 모든 컬럼별 정보", irisDF.describe(include='all'), sep='\n')

## => describe()/ head() / tail() 메서드 결과는 저장 후 활용 가능
descDF = irisDF.describe()
print(type(descDF), descDF.index,  descDF.columns , sep='\n')
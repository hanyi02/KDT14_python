## ========================================================
##      File === > DataFrame으로 변환 로딩
##
## 관련 함수들 : pandas.read_파일포맷()
##     pandas.read_csv() / .read_excel() / .read_json()
## ========================================================
## [기억] DataFrame = 행인덱스 + 열이름인덱스 + 데이터
## [규칙] 파일의 첫번째 줄에 데이터 ==> 열이름/컬럼이름으로 설정 
## ========================================================
## --------------------------------------------------------
## [1] 모듈 로딩 및 데이터 선정
## --------------------------------------------------------
import pandas as pd 
import sys
sys.path.append(r'D:\KDT\VS_KDT_14\[2]_PANDAS\comm')
import utils 

## 데이터 파일
DATA_FILE1 = '../DATA/iris.csv'
DATA_FILE2 = '../DATA/iris_no_columns.csv'
DATA_FILE3 = '../DATA/iris_space.csv'

## --------------------------------------------------------
## [2] CSV >>> DataFrame 로딩 및 기본 형태 확인
## --------------------------------------------------------
## DataFrame으로 로딩
irisDF = pd.read_csv(DATA_FILE1)

## 기본 정보 확인
utils.print_df("첫번째줄 컬럼명 있는 CSV", irisDF)
print("컬럼이름 인덱스 -> ", irisDF.columns)


## --------------------------------------------------------
## [3] CSV >>> DataFrame 로딩 및 기본 형태 확인
## --------------------------------------------------------
## DataFrame으로 로딩
## 첫번째 줄이 데이터 ==> 컬럼명 없는 CSV 파일 
## 설정 필요 : header 매개변수 = None
irisDF = pd.read_csv(DATA_FILE2, header=None)

## 기본 정보 확인
utils.print_df("첫번째줄 데이터 존재 CSV", irisDF)
print("컬럼이름 인덱스 -> ", irisDF.columns)

## 컬럼이름 속성 설정
irisDF.columns =['받침_길이','받침_너비','꽃_길이', '꽃_너비', '품종']
print(irisDF.head(2))


## --------------------------------------------------------
## [4] CSV >>> DataFrame 로딩 및 기본 형태 확인
## --------------------------------------------------------
## DataFrame으로 로딩
## 첫번째 줄이 데이터 ==> 컬럼명 없는 CSV 파일 : header 매개변수 설정
## 데이터 구분 문자   ==> 공백 1개 : sep 매개변수 설정
irisDF = pd.read_csv(DATA_FILE3, header=None, sep=' ')

## 기본 정보 확인
utils.print_df("첫번째줄 데이터 + 구분자 공백 1개 CSV", irisDF)
print("컬럼이름 인덱스 -> ", irisDF.columns)

# 컬럼이름 속성 설정
irisDF.columns =['길이1','너비1','길이2', '너비2', '종류']
print(irisDF.head(2))

## --------------------------------------------------------
## [5] CSV >>> DataFrame 로딩 및 기본 형태 확인
## --------------------------------------------------------
## DataFrame으로 로딩
## 첫번째 줄이 데이터           ==> header    매개변수 설정
## 데이터 구분 문자             ==> sep       매개변수 설정
## 특정 컬럼을 행인덱스 설정 로딩 ==> index_col 매개변수 설정
irisDF = pd.read_csv(DATA_FILE3, header=None, sep=' ', index_col=3)

## 기본 정보 확인
utils.print_df("첫번째줄 데이터 + 구분자 공백 1개 + 컬럼 행인덱스 설정", irisDF)
print("컬럼이름 인덱스 -> ", irisDF.columns)
print("행      인덱스 -> ", irisDF.index)


## --------------------------------------------------------
## [6] CSV >>> DataFrame 로딩 및 기본 형태 확인
## --------------------------------------------------------
## DataFrame으로 로딩
irisDF = pd.read_csv(DATA_FILE1, usecols=[0,1,4])

## 기본 정보 확인
utils.print_df("0, 1, 4번 컬럼만 추출", irisDF)
print("컬럼이름 인덱스 -> ", irisDF.columns)
print("DF 형태 정보   -> ", irisDF.shape)


## --------------------------------------------------------
## [6] CSV >>> DataFrame 로딩 및 기본 형태 확인
## --------------------------------------------------------
## DataFrame으로 로딩
## skipfooter 매개변수 : 아래쪽 지정된 개수 데이터 로딩 X
## skiprows   매개변수 : 앞쪽 지정된 개수 데이터 로딩 X
irisDF = pd.read_csv(DATA_FILE1, skipfooter=30, 
                                 skiprows=10, header=None)

## 기본 정보 확인
utils.print_df("skipfooter 일부 행 제외한 데이터 로딩", irisDF)
print("컬럼이름 인덱스 -> ", irisDF.columns)
print("DF 형태 정보   -> ", irisDF.shape)

## --------------------------------------------------------
## [7] CSV >>> DataFrame 로딩 및 기본 형태 확인
## --------------------------------------------------------
## 날짜/시간 컬럼 존재하는 데이터 파일
DATA_FILE1 = '../DATA/sample_data.csv'

## DataFrame으로 로딩
## 첫번째줄 -> 컬럼이름 데이터 OK
## 구분자   -> 쉼표/콤마      OK
## 날짜/시간 컬럼 ==> datetime64[ns] 형변환 후 로딩 :  parse_dates=[컬럼명] 매개변수
csvDF = pd.read_csv(DATA_FILE1, parse_dates=['date'])

## 기본 정보 확인
utils.print_df("데이터 로딩", csvDF)
print("컬럼이름 인덱스 -> ",   csvDF.columns)
print("DF 형태 정보   -> ",   csvDF.shape)
print("DF 컬럼 타입   -> ",   csvDF.dtypes.to_dict())

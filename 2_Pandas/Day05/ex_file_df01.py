## =============================================================
##      File===> DataFrame으로 변환 로딩
##
## 관련 함수들: pandas.read_파일포맷()
##            pandas.read_csv()/ .read_excel()/ .read_json()
## =============================================================
## [기억] DataFrame = 행인덱스+ 열이름인덱스+ 데이터
## [규칙] 파일의 첫번째 줄에 데이터===> 열이름/ 컬럼이름으로 설정
## =============================================================
# [1] 모듈 로딩 및 데이터 선정
import pandas as pd
import sys 
sys.path.append(r'C:\KDT14\2_Pandas\comm')
import utils


## 데이터 파일
Data_File1='../Data/iris.csv'
Data_File2='../Data/iris_no_columns.csv'
Data_File3='../Data/iris_space.csv'

## =============================================================
## [2] CSV >>> DataFrame 로딩 및 기본 형태 확인
## =============================================================
irisDF= pd.read_csv(Data_File1)
# irisDF2= pd.read_csv(Data_File2)
# irisDF3= pd.read_csv(Data_File3)

utils.print_df("첫번째줄 컬럼명 있는 CSV" ,irisDF)
utils.print_df("컬럼이름 인덱스->" ,irisDF.columns)


## =============================================================
## [3] CSV >>> DataFrame 로딩 및 기본 형태 확인
## =============================================================
## DataFrame으로 로딩
## 첫번째줄이 데이터==> 컬럼명 없는 CSV 파일
## 설정 필요: header 매개변수= None
irisDF= pd.read_csv(Data_File2, header=None)

## 기본정보 확인
utils.print_df("첫번째줄 컬럼명 있는 CSV" ,irisDF)
utils.print_df("컬럼이름 인덱스->" ,irisDF.columns)

## 컬럼이름
irisDF.columns=['받침_길이', '받침_너비', '꽃_길이', '꽃_너비', '품종']
print(irisDF.head(2))

## =============================================================
## [4] CSV >>> DataFrame 로딩 및 기본 형태 확인
## =============================================================
## DataFrame으로 로딩
## 첫번째줄이 데이터==> 컬럼명 없는 CSV 파일: header 설정 해야함
## 데이터 구분 문자==> 공백 1개: sep 매개변수 설정
irisDF= pd.read_csv(Data_File3, header=None, sep=' ')

## 기본정보 확인
utils.print_df("첫번째줄 데이터+ 구분자 공백 1개 CSV" ,irisDF)
utils.print_df("컬럼이름 인덱스->" ,irisDF.columns)

# ## 컬럼이름
# irisDF.columns=['받침_길이', '받침_너비', '꽃_길이', '꽃_너비', '품종']
# print(irisDF.head(2))



## =============================================================
## [5] CSV >>> DataFrame 로딩 및 기본 형태 확인
## =============================================================
## DataFrame으로 로딩
## 첫번째줄이 데이터                ==> 컬럼명 없는 CSV 파일: header 설정 해야함
## 데이터 구분 문자                 ==> 공백 1개: sep 매개변수 설정
## 특정 컬럼을 행인덱스 설정 로딩     ==> index_col 매개변수 설정
irisDF= pd.read_csv(Data_File3, header=None, sep=' ', index_col=3)

## 기본정보 확인
utils.print_df("첫번째줄 데이터+ 구분자 공백 1개+ 컬럼 행인덱스 설정" ,irisDF)
utils.print_df("컬럼이름 인덱스->" ,irisDF.columns)
utils.print_df("행 인덱스->" ,irisDF.columns)
 


## =============================================================
## [6] CSV >>> DataFrame 로딩 및 기본 형태 확인
## =============================================================
irisDF= pd.read_csv(Data_File1, usecols=[0,1,4])
# irisDF2= pd.read_csv(Data_File2)
# irisDF3= pd.read_csv(Data_File3)

utils.print_df("0,1,4번 컬럼만 추출" ,irisDF)
utils.print_df("컬럼이름 인덱스->" ,irisDF.columns)
utils.print_df("DF 형태 정보->" ,irisDF.shape)



## =============================================================
## [7] CSV >>> DataFrame 로딩 및 기본 형태 확인
## =============================================================
## DataFrame으로 로딩
# skipfooter 매개변수: 아래쪽 지정된 개수 데이터 로딩 XX
# skiprows 매개변수: 앞쪽 지정된 개수 데이터 로딩 XX

irisDF= pd.read_csv(Data_File1, skipfooter=30     
                                ,skiprows=10, header=None) # 150개 중 30개 버리겠다는 뜻(footer- 아래쪽 버리겠다)
#                                 위에서부터 10개 날리니까 헤더 없다고 알려줘야 됨
# irisDF2= pd.read_csv(Data_File2)
# irisDF3= pd.read_csv(Data_File3)

utils.print_df("skipfooter=30 제외한 데이터 로딩" ,irisDF)
utils.print_df("컬럼이름 인덱스->" ,irisDF.columns)
utils.print_df("DF 형태 정보->" ,irisDF.shape)



## =============================================================
## [8] CSV >>> DataFrame 로딩 및 기본 형태 확인
## =============================================================
## 날짜/ 시간 컬럼 존재하는 데이터 파일
Data_File1='../Data/sample_data.csv'

## DataFrame으로 로딩
## 첫번째 줄: 컬럼이름 데이터 o
## 구분자: 쉽표/ 콤마 o
## 날짜/ 시간 컬럼==> datetime64[ns] 형변환 후 로딩: parse_dates=[컬럼명] 매개변수
csvDF= pd.read_csv(Data_File1, parse_dates=['date'])

## 기본 정보 확인
utils.print_df("데이터 로딩" ,csvDF)
utils.print_df("컬럼이름 인덱스->" ,csvDF.columns)
utils.print_df("DF 형태 정보->" ,csvDF.shape)
utils.print_df("DF 컬럼 타입->" ,csvDF.dtypes.to_dict) # 원래 시리즈-> to_dict로 자료형 변환
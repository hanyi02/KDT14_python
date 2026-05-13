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
Data_File1='../Data/학생관리부.xlsx'

## =============================================================
## [2] EXCEL >>> DataFrame 로딩 및 기본 형태 확인
## =============================================================
# 컬럼이름 행 설정: header 매개변수 
# excelDF= pd.read_excel(Data_File1)
excelDF= pd.read_excel(Data_File1, header=2) #0, 1번 행 자동 스킵

utils.print_df("첫번째줄 컬럼명 있는 CSV" ,excelDF)
utils.print_df("컬럼이름 인덱스->" ,excelDF.columns)

## =============================================================
## [3] EXCEL >>> DataFrame 로딩 및 기본 형태 확인
## =============================================================
# 컬럼이름 행 설정: header 매개변수 
# 특정 컬럼=> 행 인덱스 설정: index_col 매개변수
excelDF= pd.read_excel(Data_File1, header=2, index_col='이름') #0, 1번 행 자동 스킵

utils.print_df("첫번째줄 컬럼명 있는 CSV" ,excelDF)
utils.print_df("컬럼이름 인덱스->" ,excelDF.columns)



## =============================================================
## [3] EXCEL >>> DataFrame 로딩 및 기본 형태 확인
## =============================================================
# 컬럼이름 행 설정: header 매개변수 
# # 엑셀 파일에서 로딩할 시트 설정: sheet_name= 정수/ 문자열
# # excelDF= pd.read_excel(Data_File1, header=2, sheet_name=1, usecol=[1, 2, 3, 4, 5, 6]) #0, 1번 행 자동 스킵

excelDF= pd.read_excel(Data_File1, header=2, sheet_name=1, usecols=range(1, 3)) #0, 1번 행 자동 스킵
utils.print_df("두번째 시트 설정" ,excelDF)
utils.print_df("컬럼이름 인덱스->" ,excelDF.columns)
utils.print_df("행 인덱스->" ,excelDF.index)
## ==============================================
##              중복 데이터 검사 및 처리
## ----------------------------------------------
## -> 검사 : DataFrame.duplicated()        True/False 반환
## -> 처리 : DataFrame.drop_duplicates() 
## ==============================================
## 모듈 로딩
import pandas as pd 
import numpy as np 
import sys 
sys.path.append(f'D:\KDT\VS_KDT_14\[2]_PANDAS\comm')
import utils 

## DF 생성
df = pd.DataFrame( { 'brand'  : [ 'Yum', 'Yum', 'Indo', 'Indo', 'Indo' ], 
                     'style'  : [ 'cup', 'cup', 'cup', 'pack', 'pack' ], 
                     'rating' : [4, 4, 3.5, 15, 5] })
## DF 출력
utils.data_info(df)

## -----------------------------------------------------
## 중복 데이터 검사
## -----------------------------------------------------
## => 행단위로 중복 여부 검사 후 True/False 
dupDF = df.duplicated()

print(dupDF)

## => 중복 데이터 개수 확인
print(dupDF.sum())

## -----------------------------------------------------
## 중복 데이터 처리 => 삭제
## -----------------------------------------------------
print( f"\n[ 원본 ]----\n{df}\n")
print(  "\n[ 중복데이터 삭제 ]===" )
print(   df.drop_duplicates() )

print( f"\n[ 원본 ]----\n{df}\n")
print(  "\n[ brand 컬럼 중복데이터 삭제 ]===" )
print(   df.drop_duplicates(subset='brand') )
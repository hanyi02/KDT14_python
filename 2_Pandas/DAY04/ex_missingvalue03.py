## ==============================================
##      결측치 처리 - 치환 
## ----------------------------------------------
## -> DataFrame.fillna() 
## -> DataFrame.ffill()
## -> DataFrame.bfill()
## ==============================================
## 모듈 로딩
import pandas as pd 
import numpy as np 
import sys 
sys.path.append(f'D:\KDT\VS_KDT_14\[2]_PANDAS\comm')
import utils 

## DF 생성
df = pd.DataFrame( [ [np.nan, 2, np.nan, 0],
                     [3, 4, np.nan, 1],
                     [np.nan, np.nan, np.nan, np.nan], 
                     [np.nan, 3, np.nan, 4]],
                     columns=list("ABCD"))
## DF 출력
utils.data_info(df)

## -----------------------------------------------------
## 결측치 삭제 : fillna()
## -----------------------------------------------------
## [1] 특정 값으로 결측치 채우기
print( f"\n[ 원본 ]----\n{df}\n")
print(  "\n[ 모든 결측치 0으로 채우기 ]===" )
print(   df.fillna(0) )

## [2] 컬럼마다 특정 값으로 결측치 채우기
print( f"\n[ 원본 ]----\n{df}\n")
print(  "\n[ 컬럼마다 특정 값으로  채우기 ]===" )
print(   df.fillna({'A':7, 'B':0, 'C':99, 'D':-1}) )


## [3] 이전 행의 값으로 결측치 채우기
print( f"\n[ 원본 ]----\n{df}\n")
print(  "\n[ 이전 행의 값으로 채우기 ]===" )
print(   df.ffill() )

## [4] 다음 행의 값으로 결측치 채우기
print( f"\n[ 원본 ]----\n{df}\n")
print(  "\n[ 다음 행의 값으로 채우기 ]===" )
print(   df.bfill(axis=0) )

print( f"\n[ 원본 ]----\n{df}\n")
print(  "\n[ 다음 열의 값으로 채우기 ]===" )
print(   df.bfill(axis=1) )

print( f"\n[ 원본 ]----\n{df}\n")
print(  "\n[ 보간법 값으로 채우기 ]===" )
print(   df.interpolate('linear'))
print(   df.interpolate('linear', limit_direction='both'))
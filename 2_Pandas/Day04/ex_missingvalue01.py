## ==============================================
##      결측치 체크 및 검사  
## ----------------------------------------------
## DataFrame.isnull() / .isna() => True/False
##                                 원소마다 검사
## ==============================================
## 모듈 로딩
import pandas as pd 
import numpy as np 
import sys 
sys.path.append(f'D:\KDT\VS_KDT_14\[2]_PANDAS\comm')
import utils 

## DF 생성
df = pd.DataFrame( dict( age  =[ 5, 6, np.nan ],
                         born =[ pd.NaT, pd.Timestamp('1939-05-27'), pd.Timestamp('1940-04-25')],
                         name =['Alfred', 'Batman', ''], 
                         toy  =[None, 'Batmobile', 'Joker']) )
## DF 출력
utils.data_info(df)

## -----------------------------------------------------
## 결측치 체크
## -----------------------------------------------------
print( f"\ndf.isna()   ===\n{df.isna()}" )
print( f"\ndf.isnull() ===\n{df.isnull()}" )

print( f"\n컬럼별 결측치\n{df.isnull().sum()}" )
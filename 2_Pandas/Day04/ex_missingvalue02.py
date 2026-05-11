## ==============================================
##      결측치 처리 - 삭제  
## ----------------------------------------------
## DataFrame.dropna() [기] 행 단위 /1개라도 결측치 있으면 삭제
## -> axis   = 0      삭제 축 기준
## -> how    = 'any'  삭제 방법
## -> thresh = 숫자    정상 데이터의 최소 개수 설정
## -> subset = 컬럼명  특정 컬럼만 결측치 검사
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
## 결측치 삭제 : dropna()
## -----------------------------------------------------
## [1] 기본 설정값으로 결측치 삭제
print(df)
print( f"\n[행 단위 삭제]df.dropna() ===\n{df.dropna()}" )


## [2] 모든 데이터가 결측치면 삭제 how='all'
print(df)
print( f"\n[행 단위 삭제]df.dropna(how='all') ===\n{df.dropna(how='all')}" )


## [3] 컬럼 방향 삭제
print( f"\n[원본]----\n{df}\n")
print( f"\n[열 단위 삭제]df.dropna(axis=1, how ='all') ===\n{df.dropna(axis=1, how='all')}" )


## [4] 생년월일 결측치인 행 삭제
print( f"\n[원본]----\n{df}\n")
print( f"\n[생년월일 결측치인 행 삭제]df.dropna() ===\n{df.dropna(subset=['born'])}" )

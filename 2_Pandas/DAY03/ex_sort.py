## =========================================
##               정렬(Sort)
## -----------------------------------------
## --> 인덱스 기준 정렬 : sort_index()
## --> 데이터 기준 정렬 : sort_values()
## =========================================
## [1] 모듈 로딩
import pandas as pd 
import numpy as np     ## 결측치/값이 없는 빈칸/Missing Value
                       ## 표현 NaN, NaT, NA, nan, nt,na

## [2] DataFrame 인스턴스 생성 
data ={'Z':[10,np.nan,30],
       'F':[8, 11, 7],
       'A':[9, 5,  8],
       'D':[11, 7, 4],
       'O':[np.nan, np.nan, np.nan]}

df = pd.DataFrame(data) 
print("\ndf===", df, sep='\n')

## [3] DataFrame 인덱스 설정
df.index = ['ㅎ', 'ㄷ','ㄱ']
print("\ndf===", df, sep='\n')

## -----------------------------------------
## [4] 인덱스 정렬
## -----------------------------------------
## => 행 인덱스
## -----------------------------------------
new_df = df.sort_index()
print("\n오름 정렬 new_df===", new_df, sep='\n')

new_df = df.sort_index(ascending=False)
print("\n내림 정렬 new_df===", new_df, sep='\n')


## -----------------------------------------
## => 열이름 인덱스: axis=1 또는 'columns'
## -----------------------------------------
new_df = df.sort_index(axis='columns')
print("\n오름 정렬 new_df===", new_df, sep='\n')

new_df = df.sort_index(axis='columns', ascending=False)
print("\n내림 정렬 new_df===", new_df, sep='\n')

## -----------------------------------------
## [5] 데이터 정렬 : sort_values()
## -----------------------------------------
print("\ndf===", df, sep='\n')

new_df = df.sort_values(by='A')
print("\n오름 정렬 by A : new_df===", new_df, sep='\n')

new_df = df.sort_values(by='Z')
print("\n오름 정렬 by Z : new_df===", new_df, sep='\n')

print("\ndf===", df, sep='\n')

new_df = df.sort_values(by=['A','Z'])
print("\n오름 정렬 by Z : new_df===", new_df, sep='\n')

print("\ndf===", df, sep='\n')
new_df = df.sort_values(by=['Z','A'])
print("\n오름 정렬 by Z : new_df===", new_df, sep='\n')

## ignore_index=True 매개변수 : 정렬 후 기존 인덱스 무시하고
##                             새롭게 정수 위치 인덱싱
new_df = df.sort_values(by=['Z','A'], ignore_index=True)
print("\n오름 정렬 by Z : new_df===", new_df, sep='\n')



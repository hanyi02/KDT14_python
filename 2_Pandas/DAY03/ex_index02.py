## =========================================
##     인덱스 관련 메서드들 (2)reindex()
## -----------------------------------------
## 기존 인덱스 ==> 새롭게 재배치/재배열
##                인덱스 추가 & 삭제 
## =========================================
## [1] 모듈 로딩
import pandas as pd 

## [2] DataFrame 인스턴스 생성 
data ={'A':[10,20,30],
       'B':[8, 11, 7],
       'C':[9, 5,  8],
       'D':[11, 7, 4]}

df = pd.DataFrame(data) 
print("\ndf===", df, sep='\n')

## [3] DataFrame 인덱스 설정
##     3행 4열 ==> one, two, three 
df.index = ['one', 'two','three']
print("\ndf===", df, sep='\n')

## -----------------------------------------
## [4] DataFrame 인덱스 재배치/재배열 
## -----------------------------------------
## => 행 인덱스
## -----------------------------------------
new_df = df.reindex(['one','three','five'])
print("\nnew_df===", new_df, sep='\n')

new_df = df.reindex(['two','five','one'])
print("\nnew_df===", new_df, sep='\n')

## -----------------------------------------
## => 열이름 인덱스 재배치: axis=1 또는 'columns'
## -----------------------------------------
new_df = df.reindex(['A','D'], axis='columns')
print("\nnew_df===", new_df, sep='\n')

new_df = df.reindex(columns=['Z', 'A', 'D','F'])
print("\nnew_df===", new_df, sep='\n')

new_df = df.reindex(columns=['Z', 'A', 'D','F'], 
                    fill_value='no')
print("\nnew_df===", new_df, sep='\n')
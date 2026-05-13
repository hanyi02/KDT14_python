## ==================================================
##         인덱스 관련 매서드들: 초기화 reset_index()
## --------------------------------------------------
## 기존 인덱스 --> 새롭게 재배치/ 재배열
##               인덱스 추가& 삭제
## ==================================================

import pandas as pd

## [2] DataFrame 인스턴스 생성

dataDF = {'A':[10, 20, 30],
          'B': [8, 11, 7],
          'C': [9, 41, 76],
          'D': [1, 31, 77]}

df= pd.DataFrame(dataDF)
print("df===", df, sep='\n')



# [3] 특정 컬럼=> 행 인덱스로 설정
# 3행 4열==> one, two, three
df.index=['one', 'two', 'three']
print("df===", df, sep='\n')


# [4] DataFrame 인덱스 초기화
# ===> 행 인덱스
new_df=df.reset_index()
print("\nnew_df===", new_df, sep='\n')

new_df= new_df.drop(columns='index')
print("\n4new_df===", new_df, sep='\n')

# ===> 행 인덱스
# ==> 매개변수 drop=False [기]
new_df=df.reset_index()
print("\nnew_df===", new_df, sep='\n')

# ==> 매개변수 drop=True : 기존 행 인덱스 삭제
new_df= new_df.drop(columns='index')
print("\n4new_df===", new_df, sep='\n')



## -----------------------------------
## 열이름 인덱스 재배치: axis=1 또는 'columns'
## -----------------------------------
new_df=df.reindex(['A', 'D'], axis=1)
print("\nnew_df===", new_df, sep='\n')


new_df=df.reindex(columns=['Z', 'A', 'D', 'F'], fill_value=0)
print("\nnew_df===", new_df, sep='\n')
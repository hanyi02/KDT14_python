## ==================================================
##                      정렬
## --------------------------------------------------
##  --> 인덱스 기준 정렬: sort_index()
##  --> 데이터 기준 정렬: sort_values()
## ==================================================

import pandas as pd
import numpy as np # 결측치/ 값이 없는 빈칸/Missing value
                    # 표현: NaN, NaT, NN

## [2] DataFrame 인스턴스 생성

data = {'Z':[10, np.nan, 30],
          'B': [8, 11, 7],
          'A': [9, 41, 76],
          'D': [1, 31, 77],
          'O': [np.nan, np.nan, np.nan]}

df= pd.DataFrame(data)
print("df===", df, sep='\n')



# [3] 특정 컬럼=> 행 인덱스로 설정
# 3행 4열==> one, two, three
df.index=['one', 'two', 'five']
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


## -----------------------------------
## [5] 데이터 정렬: sort_values()
## -----------------------------------

new_df= df.sort_values(by='A')
print("\nnew_df===", new_df, sep='\n')
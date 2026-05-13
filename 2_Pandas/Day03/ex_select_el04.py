## ==================================================
##          DataFrame/ Series 행/열/원소 삭제
## ==================================================

import pandas as pd

## [2] 인스턴스 할당

dataDF = pd.DataFrame(
    [[10, 20, 30, 40.],
     [11, 22, 33, 44.]],
    columns=['영', '일', '이', '삼'],
    index=['row0', 'row1']
)

# [3] DataFrame 삭제 -------------------
# 삭제할 인덱스
# 삭제할 방향: 행0 또는 index, 열 1 또는 columns
# > 원본 사용 여부: inplace= True 원본 사용
#                inplace= False 원본X, 복사본 사용
# --------------------------------------
# [3-1] 열 / 컬럼 삭제
dataDF.drop('이', axis=1)

# '삼' 컬럼 삭제+ 원본 유지
c_dataDF= dataDF.drop(columns='삼', inplace=False)
print(c_dataDF)

# '삼' 컬럼 삭제+ 원본 유지
c_dataDF= dataDF.drop(columns='삼', inplace=False)
print(c_dataDF)

# [3-2] 행 삭제
dataDF3 = dataDF.drop(index='row1', inplace=True)
print(dataDF3)  # row0 행 삭제



# [3] Series 삭제 -------------------
# [4-1] 원소 삭제




#       영   일    이   삼
# row0  10   20   30   40.0
# row1  11   22   33   44.0
# => 10, 40.0, 11, 44.0 원소 선택

# elements= dataDF2.iloc[[0,1], [0, 3]]
# print("\n===elements", elements, sep='\n')

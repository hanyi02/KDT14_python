## ==================================================
##          DataFrame에서 행/ 열 선택
## ==================================================

import pandas as pd

## [2] 인스턴스 할당

dataDF1 = pd.DataFrame(
    [[10, 20, 30, 40],
     [20, 30, 40, 50]],
    columns=['영', '일', '이', '삼'],
    index=['row0', 'row1']
)

dataDF2= pd.DataFrame([10, 20, 30, 40.]
                      [11, 22, 33, 44.])




# [3] 행 선택
# [3-1] 1개 행 선택
one_row = dataDF1.loc['row0']
print("\n=== one_row", one_row, sep='\n')

# [3-2] 2개 이상 행 선택 - 인덱스 리스트
two_row = dataDF1.loc[['row0', 'row1']]
print("\n=== two_row", two_row, sep='\n')

# [3-3] 2개 이상 행 선택 - 인덱스 슬라이싱
slice_row = dataDF1.loc['row0':'row1']
print("\n=== slice_row", slice_row, sep='\n')

# 숫자 기본 인덱스 DataFrame에서 행 선택
two_row2 = dataDF2.loc[[0, 1]]
print("\n=== two_row2", two_row2, sep='\n')

slice_row2 = dataDF2.loc[0:]
print("\n=== slice_row2", slice_row2, sep='\n')
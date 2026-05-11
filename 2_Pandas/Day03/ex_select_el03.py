## ==================================================
##          DataFrame에서 행/ 열 선택
## ==================================================

import pandas as pd

## [2] 인스턴스 할당

dataDF2 = pd.DataFrame(
    [[10, 20, 30, 40.],
     [11, 22, 33, 44.]],
    columns=['영', '일', '이', '삼'],
    index=['row0', 'row1']
)

# [3] 원소선택 -------------------
# [3-1] 1개 원소 40.0 선택

one_el= dataDF2.iloc[0, 3]
print("\n===one_el", one_el, sep='\n')

one_el= dataDF2.loc['row0', '삼']
print("\n===one_el", one_el, sep='\n')



# [3-1] 2개 원소선택 -------------------
# [] 인덱스 리스트 => 40.0, 44.0
two_el= dataDF2.iloc[[0,1], 3]
print("\n===two_el", two_el, sep='\n')

two_el= dataDF2.loc[['row0', 'row1'], '삼']
print("\n===two_el", two_el, sep='\n')


#       영   일    이   삼
# row0  10   20   30   40.0
# row1  11   22   33   44.0
# => 10, 40.0, 11, 44.0 원소 선택

elements= dataDF2.iloc[[0,1], [0, 3]]
print("\n===elements", elements, sep='\n')

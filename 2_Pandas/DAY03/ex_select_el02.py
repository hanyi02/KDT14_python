## =======================================================
##                  DataFrame에서 행/열 선택
## =======================================================
## [1] 모듈 로딩
import pandas as pd 

## [2] DataFrame 인스턴스 생성
dataDF1 = pd.DataFrame( [[10,20,30,40.],
                         [11,22,33,44.]])

dataDF2 = pd.DataFrame( [[10,20,30,40.],
                         [11,22,33,44.]],
                         columns=['영','일','이','삼'],
                         index = ['row0','row1'])

## => 생성된 인스턴스 확인
# print("\n=== dataDF1", dataDF1, sep='\n')
# print("\n=== dataDF2", dataDF2, sep='\n')

# === dataDF1
#     0   1   2   3
# 0  10  20  30  40.0
# 1  11  22  33  44.0

# === dataDF2
#       영   일  이   삼
# row0  10  20  30  40.0
# row1  11  22  33  44.0

## [3] 열 선택 ---------------------------------
## [3-1] 1개 열 선택
one_col = dataDF2['일']
print("\n=== one_col", one_col, sep='\n')

one_col = dataDF1[1]
print("\n=== one_col", one_col, sep='\n')


## [3-2] 2개 이상 열 선택 - 인덱스 리스트
two_col = dataDF2[['삼','일']]
print("\n=== two_col", two_col, sep='\n')

#two_col = dataDF2[[3, 1]] <== 지정된 컬럼이름만 가능함!!
two_col = dataDF1[[3, 1]]
print("\n=== two_col", two_col, sep='\n')


## [3-3] 2개 이상 열 선택 - 인덱스 슬라이싱
##       df변수명.loc[행선택, 시작라벨인덱스:끝라벨인덱스 ]
two_col = dataDF2.loc[ : , '일' :'삼' ]     ## '일','이','삼'
print("\n=== two_col", two_col, sep='\n')

two_col = dataDF2.loc[ : , '일' :'삼': 2 ]   ## '일','삼'
print("\n=== two_col", two_col, sep='\n')

##       df변수명.iloc[행선택, 시작 위치 인덱스:끝 위치인덱스 ]
two_col = dataDF2.iloc[ : , 1 :  ]     ##  1<= ~ <4
print("\n=== two_col", two_col, sep='\n')
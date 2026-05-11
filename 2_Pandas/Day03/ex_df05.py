## ====================================================
##     DataFrame 행(로우)과 열(컬럼) 다루기 
## ----------------------------------------------------
## * 여러 행 선택 - (1) 인덱스 리스트
##    -> df변수명.iloc[ [정수 위치인덱스, ...] ]
##    -> df변수명.loc[ [라벨 인덱스,... ] ]
## * 여러 열 선택
##    -> df변수명[ [컬럼이름,....] ]
## ====================================================
## ----------------------------------------------------
## [1] 모듈 로딩
## ----------------------------------------------------
import pandas as pd 

## ----------------------------------------------------
## [2] DataFrame 인스턴스 생성
## ----------------------------------------------------
## 데이터 준비
datas = [ [11,33,55,77], 
          [ 2,22, 4,44] , 
          ['A',10,'B',0] ]

## DataFrame 인스턴스 생성
df = pd.DataFrame(datas, 
                  index  =["1st","2nd", "3th"],
                  columns=['A','B','C','D'])
print(df)

## -------------------------------------------
## [3] DataFrame 인스턴스 속성 읽기
## -------------------------------------------
print('- DataFrame 기본 속성들 -')
print(f'* index   : {df.index}')        ## 표/데이터프레임 행 식별 인덱스
print(f'* columns : {df.columns}')      ## 표/데이터프레임 컬럼 식별


## -------------------------------------------
## [4] 열/컬럼 선택 
##     df변수명[ [컬럼 이름,...] ]  
##     => 컬럼이름 지정 시 위치 인덱스 지원 X
##     => 여러 개 컬럼이 반환으로 DataFrame 타입
## -------------------------------------------
print("\n --- 컬럼 선택 ---")
print("A, B, C 컬럼 선택", type(df[['A','B','C']]))
print( df[['A','B','C']] ) 

print("\n --- 컬럼 선택 ---")
print("C 컬럼 선택", type(df[['C']]))
print( df[['C']] )   
  


# ## -------------------------------------------
# ## [5] 행/로우 선택
# ##    -> df변수명.iloc[ [정수 위치인덱스, ...] ]
# ##    -> df변수명.loc[ [라벨 인덱스,... ] ]
# ##    => 반환값은 DataFrame
# ## -------------------------------------------
# print("\n --- 행 선택 ---")
# print("여러 행 선택 - 위치 인덱스 ", type(df.iloc[ [2,0,1] ]))
# print( df.iloc[[2,0,1]] )

# print("여러 행 선택 - 라벨 인덱스 ", type(df.loc[['3th']]))
# print( df.loc[['3th']] )


## DataFrame 인스턴스 생성 -------------------------------------
dataDF1 = pd.DataFrame( [[10, 20, 30, 40.],
                         [11, 22, 33, 44.]])

dataDF2 = pd.DataFrame( [[10, 20, 30, 40.],[11, 22, 33, 44.]], 
                        columns=['영','일','이','삼'],
                        index=['row0', 'row1'])


print('\n-------행---------\n')
##- 1개 행 선택 ------------------------
one_row = dataDF1.iloc[ 0 ]
print( one_row , type(one_row), sep='\n')

one_row = dataDF2.iloc[ 0 ]
print( one_row , type(one_row), sep='\n')

one_row = dataDF2.loc[ 'row0' ]
print( one_row , type(one_row), sep='\n')


print('\n-------여러개 행---------\n')
##- 여러 개 행 선택 ------------------------
two_row = dataDF1.iloc[ [0, 1] ]
print( two_row , type(two_row), sep='\n')

two_row = dataDF2.iloc[ 0 : 2 ]
print( two_row , type(two_row), sep='\n')


two_row = dataDF2.iloc[ [0, 1] ]
print( two_row , type(two_row), sep='\n')

two_row = dataDF2.loc[ ['row0' ,'row1'] ]
print( two_row , type(two_row), sep='\n')

two_row = dataDF2.loc[ 'row0' : 'row1' ]
print( two_row , type(two_row), sep='\n')


print('\n--------열--------\n')
##- 1개 열 선택 ------------------------
one_col = dataDF1[0]
print( one_col , type(one_col), sep='\n')


one_col = dataDF2['영']
print( one_col , type(one_col), sep='\n')



##- 여러 개 열 선택 ------------------------
two_row = dataDF1[ [0, 1] ]
print(two_row , type(two_row),  sep='\n')

two_row = dataDF1.iloc[:, 0:3:2]
print(two_row , type(two_row),  sep='\n')


two_row = dataDF2[ ['영', '일'] ]
print(two_row , type(two_row),  sep='\n')

two_row = dataDF2.loc[:, '영':'삼':2 ]
print(two_row , type(two_row),  sep='\n')


##- ---------------------------------------
##- 1개 0번행 0번 요소 선택 
##- ---------------------------------------
one_e = dataDF2.iloc[0, 0]
print(one_e, type(one_e))

one_e = dataDF2.loc['row0', '영']
print(one_e, type(one_e))

one_e = dataDF2.loc['row0']['영']
print(one_e, type(one_e))



##- ---------------------------------------
##- 여러 개 0번행 0번열, 0번행 2번열  요소 선택 
##- ---------------------------------------
two_e = dataDF2.iloc[ 0, [0, 2] ]
print(two_e, type(two_e))

two_e = dataDF2.loc['row0', ['영', '이']]
print(two_e, type(two_e))

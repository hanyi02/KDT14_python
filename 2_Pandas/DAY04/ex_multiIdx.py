## ==================================================
##              멀티인덱스   
##
##  => 2개 인상의 데이터로 행/열 인덱스 구성한 것
## ==================================================
## [1] 모듈 로딩
import pandas as pd 

## [2] 데이터 준비
values   = [ [1,2,3], [4,5,6], [7,8,9], 
             [10,11,12],[13,14,15], [16,17,18] ]

index_   = [ ['row1','row1','row2','row2','row3','row3'],
             ['val1','val2','val1','val2','val2','val3'] ]

columns_ = [ [ 'A', 'B','B'], 
             ['col1', 'col1', 'col2'] ] 

## [3] DF 인스턴스 생성
## => DF 생성
df = pd.DataFrame(values, columns=columns_, index=index_) 

##=> MultiIndex 저장
mIndex = df.index 
print(df, mIndex, sep='\n\n')

## => MultiIndex 속성들
print(f'* levshape    속성: {mIndex.levshape}\n') 
print(f'* names       속성: {mIndex.names}\n') 
print(f'* nlevels     속성: {mIndex.nlevels}개\n') 
print(f'* levels      속성: \n{mIndex.levels}\n') 
print(f'* dtypes      속성: \n{mIndex.dtypes}\n')

## ---------------------------------------------
## [4] 행 / 열 선택
## ---------------------------------------------
#              A    B     
#           col1 col1 col2
# row1 val1    1    2    3
#      val2    4    5    6
# row2 val1    7    8    9
#      val2   10   11   12
# row3 val2   13   14   15
#      val3   16   17   18
## => [기본] 행 선택
print( df.loc[('row1','val1')] )

## => [level0만 지정] 행 선택
print( df.loc['row1'] )

## => [level1만 지정] 행 선택
##print( df.loc['val1'] )  <== .loc 속성에서 미지원
print("-------")
print( df.xs(key='val1', level=1, drop_level=False) )
print("-------")


## ---------------------------------------------
## [5] 행 / 열 추가
## ---------------------------------------------
#              A    B     
#           col1 col1 col2
# row1 val1    1    2    3
#      val2    4    5    6
# row2 val1    7    8    9
#      val2   10   11   12
# row3 val2   13   14   15
#      val3   16   17   18

## => 열 추가 --------------------------------
df[('A','col2')] = 0
print(df)

df['C'] = 0      ## ('C', '')로 권장하지 않음
print(df)

# 컬럼 인덱스 정렬
df = df.sort_index(axis=1, level=0)
print("컬럼인덱스 정렬 axis=1, level=0 ----- ", df, sep='\n')

df = df.sort_index(axis=1, level=1)
print("컬럼인덱스 정렬 axis=1, level=1 ----- ", df, sep='\n')


# ## => 행 추가 -------------------------------
df.loc[('row1','val3'), :] = 0
print(df)

df = df.sort_index(axis=0, level=0)
print(df)

df = df.sort_index(axis=0, level=1)
print(df)
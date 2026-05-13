## =======================================================
##                  DataFrame/Series 행/열/원소 삭제
## =======================================================
## [1] 모듈 로딩
import pandas as pd 

## [2] DataFrame 인스턴스 생성
dataDF = pd.DataFrame( [[10,20,30,40.],
                        [11,22,33,44.]],
                        columns=['영','일','이','삼'],
                        index = ['row0','row1'])

## ---------------------------------
## [3] DataFrame 삭제 
## -> 삭제할 인덱스
## -> 삭제할    방향 : axis 행 0 또는 index,  열 1 또는 columns
## -> 원본 사용 여부 : inplace = True  원본 사용
##                   inplace = False 원본 X, 복사본 사용
## ---------------------------------
## [3-1] 열/컬럼 삭제 
print('\n원본----\n', dataDF, sep='\n')

## '이' 컬럼 삭제 + 원본 유지
c_dataDF = dataDF.drop('이', axis=1)
print('\n삭제 후----\n', dataDF, sep='\n')
print(c_dataDF)

## '이' 컬럼 삭제 + 원본 적용 
c_dataDF = dataDF.drop('이', axis=1, inplace=True)
print('\n삭제 후----\n', dataDF, sep='\n')
print(c_dataDF)


## '삼' 컬럼 삭제 + 원본 유지
c_dataDF = dataDF.drop(columns='삼', inplace=False)
print('\n삭제 후----\n', dataDF, sep='\n')
print(c_dataDF)

## '영','삼' 컬럼 삭제 + 원본 유지
c_dataDF = dataDF.drop(columns=['영','삼'], inplace=False)
print('\n삭제 후----\n', dataDF, sep='\n')
print(c_dataDF)


## [3-2] 행 삭제 
## row1 행 삭제 + 원본 유지 
c_dataDF = dataDF.drop('row1', axis='index', inplace=False)
print('\n삭제 후----\n', dataDF, sep='\n')
print(c_dataDF)

## row1 행 삭제 + 원본 삭제 
c_dataDF = dataDF.drop(index='row1', inplace=True)
print('\n삭제 후----\n', dataDF, sep='\n')
print(c_dataDF)


## ---------------------------------
## [4] Series 삭제 
## ---------------------------------
## Series 데이터 추출 
sr = dataDF.iloc[0]    ## dataDF.loc['row0']
print(sr)

## 원소 삭제 + 원본 유지
c_sr = sr.drop(['영','삼'])
print('\n삭제 후----\n', sr, sep='\n')
print(c_sr)
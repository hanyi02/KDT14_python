## =================================================
##          Series 인스턴스 생성 및 이해
## =================================================
## 데이터
import pandas as pd

data = [ 'Google', 1995, 'USA', True ]

## [1] 위 데이터를 Series로 저장하세요.
sr1=pd.Series(data)

## [2] 생성된 Series 객체의 기본 속성 즉, 
##     index, values, dtype, shape, ndim 값을 출력하세요.
print(f'sr1의 인덱스는=> {sr1.index}')
print(f'sr1의 values는=> {sr1.values}')
print(f'sr1의 dtype는=> {sr1.dtype}')
print(f'sr1의 shape는=> {sr1.shape}')
print(f'sr1의 ndim는=> {sr1.ndim}')


## [3] 생성된 Series 객체의 인덱스를 사명, 창립년도, 위치, 대기업여부로
##     변경해주세요.
sr1.index= ['사명', '창립년도', '위치', '대기업여부']

## [4] 생성된 Series 객체에서 1995 데이터만 추출해서 출력하세요.
print(sr1.iloc[1])
print(sr1['창립년도'])

## [5] 생성된 Series 객체에서 사명, 창립년도, 위치를 출력하세요.
## [5-1] 리스트 방식
print(sr1[['사명', '창립년도', '위치']])

## [5-2] 슬라이싱 방식
print(sr1[0:3])
print(sr1['사명':'위치'])

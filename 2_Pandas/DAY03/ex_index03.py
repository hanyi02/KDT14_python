## =========================================
##     인덱스 관련 메서드들 (3)reset_index()
## -----------------------------------------
## 기존 인덱스 ==> 컬럼으로 옮기고
##               정수형 위치 인덱스로 초기화
## =========================================
## [1] 모듈 로딩
import pandas as pd 

## [2] DataFrame 인스턴스 생성 
data ={'A':[10,20,30],
       'B':[8, 11, 7],
       'C':[9, 5,  8],
       'D':[11, 7, 4]}

df = pd.DataFrame(data) 
print("\ndf===", df, sep='\n')

## [3] DataFrame 인덱스 설정
##     3행 4열 ==> one, two, three 
df.index = ['one', 'two','three']
print("\ndf===", df, sep='\n')

## -----------------------------------------
## [4] DataFrame 인덱스 초기화
## -----------------------------------------
## => 행 인덱스
## -----------------------------------------
## => 매개변수 drop = False [기]
new_df = df.reset_index()
print("\nnew_df===", new_df, sep='\n')

new_df = new_df.drop(columns='index')
print("\nnew_df===", new_df, sep='\n')

## => 매개변수 drop = True : 기존 행 인덱스 삭제
new_df = df.reset_index(drop=True)
print("\nnew_df===", new_df, sep='\n')
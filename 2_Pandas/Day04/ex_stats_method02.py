## ===============================================
##              통계 관련 메서드들
## ===============================================
## [1] 모듈 로딩
## ----------------------------------
import sys
sys.path.append(r'D:\KDT\VS_KDT_14\[2]_PANDAS\comm')
import utils
import pandas as pd 

## ----------------------------------
## [2] 데이터 준비
## ----------------------------------
DATA_FILE = '../DATA/iris.csv'

## ----------------------------------
## [3] CSV >>> DataFrame 변환 저장
## ----------------------------------
irisDF = pd.read_csv(DATA_FILE)

## ----------------------------------
## [4] DataFrame 기본 정보 확인
## ----------------------------------
#utils.data_info(irisDF)

## ----------------------------------
## [5] 통계 관련 메서드들
## ----------------------------------
## => 평균, 중앙값, 최빈값, 최소, 최대, 표준편차
## ----------------------------------
meanSR = irisDF.mean(numeric_only=True)
print(f'[평  균] meanSR =>\n{meanSR}')

medianSR = irisDF.median(numeric_only=True)
print(f'[중앙값] medianSR =>\n{medianSR}')

modeSR = irisDF.mode(numeric_only=True)
print(f'[최빈값] modeSR =>\n{modeSR}')

minSR = irisDF.min(numeric_only=True)
print(f'[최소값] minSR =>\n{minSR}')

maxSR = irisDF.max(numeric_only=True)
print(f'[최대값] maxSR =>\n{maxSR}')

stdSR = irisDF.std(numeric_only=True)
print(f'[표준편차] stdSR =>\n{stdSR}')


## ----------------------------------
## => 상관계수 계산 후 DataFrame
## => 
## ----------------------------------
corrDF = irisDF.corr(numeric_only=True)

print(f'[상관계수] corrDF =>\n{corrDF}')
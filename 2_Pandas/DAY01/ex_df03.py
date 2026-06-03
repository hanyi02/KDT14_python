## =====================================================
## JSOM 파일 => 표 형태 즉, DataFrame으로 읽기
## =====================================================
## 사용함수 : read_json( "경로/파일명.xlsx", 옵션들...)
## =====================================================
## [1] 모듈/패키지 로딩
import pandas as pd

## [2] csv 데이터 읽어오기
DATA_FILE = '../DATA/students_records.json'
dataDF = pd.read_json(DATA_FILE)

## [3] 읽어온 데이터 확인
print("CSV => 데이프레임 ======\n", dataDF)

print("속성들 =================\n")
print(f"index   : {dataDF.index}")
print(f"columns : {dataDF.columns}")
print(f"shape   : {dataDF.shape}")
print(f"dtypes  : {dataDF.dtypes}")

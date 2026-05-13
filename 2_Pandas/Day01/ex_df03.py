## ===============================================================
## CSV 파일=> 표 형태 즉, DATAFRAME으로 읽기
## conda install -c conda-forge openpyxl
## ===============================================================
## 사용함수: read_json(" 경로/ 파일명.csv 또는 json ....")

# [1] 모듈/ 패키지 로딩
import pandas as pd

# [2] csv 데이터 읽어오기
DATA_FILE='../2_Pandas/Data/students_records.json'
dataDF= pd.read_json(DATA_FILE)

print(dataDF)

print(f"index: {dataDF.index}")
print(f"columns: {dataDF.columns}")
print(f"shape: {dataDF.shape}")
print(f"dtypes: {dataDF.dtypes}")
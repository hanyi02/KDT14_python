## ========================================================
##      File === > DataFrame으로 변환 로딩
##
## 관련 함수들 : pandas.read_파일포맷()
##     pandas.read_csv() / .read_excel() / .read_json()
## ========================================================
## [기억] DataFrame = 행인덱스 + 열이름인덱스 + 데이터
## [규칙] 파일의 첫번째 줄에 데이터 ==> 열이름/컬럼이름으로 설정 
## ========================================================
## --------------------------------------------------------
## [1] 모듈 로딩 및 데이터 선정
## --------------------------------------------------------
## [1-1] 모듈 로딩
import pandas as pd                     ## 데이터분석용 패키지
import json                             ## json 처리 파이썬 표준 모듈 

import sys  
sys.path.append(r'C:\KDT14\2_Pandas\comm')
import utils                            ## 사용자 정의 모듈

## [1-2] 데이터 파일
DATA_FILE1 = '../DATA/logs_json_lines.jsonl'
DATA_FILE2 = '../DATA/students_columns.json'
DATA_FILE3 = '../DATA/students_records.json'
DATA_FILE4 = '../DATA/students_index.json'
DATA_FILE5 = '../DATA/students_values.json'
DATA_FILE6 = '../DATA/students_split.json'
DATA_FILE7 = '../DATA/students_table.json'
DATA_FILE8 = '../DATA/orders_nested.json'


## --------------------------------------------------------
## [2] JSON >>> DataFrame 로딩 및 기본 형태 확인
## --------------------------------------------------------
## DataFrame으로 로딩
## .jsonl 포맷 : JSON 객체들을 배열 [] 안에 넣지 않고, 
##              한 줄에 JSON 객체 1개씩 저장한 형식
## lines 매개변수 설정 : True
jsonDF = pd.read_json(DATA_FILE1, lines=True)  

## 기본 정보 확인
utils.print_df("jsonl 데이터 로딩", jsonDF)


## --------------------------------------------------------
## [3] JSON >>> DataFrame 로딩 및 기본 형태 확인
## --------------------------------------------------------
## DataFrame으로 로딩
## => json 파일을 열어서 orient 저장 방식을 확인 필요
## => pandas에서는 복잡하지 않은 json은 자동으로 orient 인식
## => JSON 객체 저장 형식 확인 후 저장 방식 설정 : orient 매개변수

## 다양한 orient 방식의 파일들
file_list   = [DATA_FILE2, DATA_FILE3, DATA_FILE4, DATA_FILE5, DATA_FILE6, DATA_FILE7]
orient_list = ['columns', 'records', 'index', 'values', 'split', 'table']

## JSON >>> DataFrame 로딩
for filepath, orient_ in zip(file_list, orient_list):
    jsonDF = pd.read_json(filepath, orient=orient_)  

    ## 기본 정보 확인
    utils.print_df(f"{orient_}방식 저장 json", jsonDF)



## --------------------------------------------------------
## [4] JSON >>> DataFrame 로딩 및 기본 형태 확인
## --------------------------------------------------------
## => ① 파이썬에서 읽기 json.load()
## => ② list 또는 dict 객체 생성
## => ③ pd.json_normalize() 적용
##      중첩 JSON을 평평한 DataFrame으로 펼쳐주는 함수

## [4-1] JSON 파일을 파이썬 객체로 읽기
with open(DATA_FILE8, "r", encoding="utf-8") as f:
    data = json.load(f)

print(data, end='\n\n')

## [4-2] 중첩 JSON을 DataFrame으로 펼치기
jsonDF = pd.json_normalize(data)

utils.print_df(f" nested 저장 json", jsonDF)
print("컬럼이름 인덱스 -> ", jsonDF.columns)
print("행      인덱스 -> ", jsonDF.index)
print("DF 형태 정보   -> ", jsonDF.shape)

## [4-3] 중첩 JSON을 DataFrame으로 펼치기
## => items처럼 리스트 안에 딕셔너리가 있는 구조
## => 행으로 펼칠 대상 리스트를 지정하는 매개변수
## record_path : 행으로 펼칠 대상 리스트를 지정하는 매개변수
## meta        : 로 펼친 데이터 옆에 같이 가져올 상위 정보를 지정
itemDF = pd.json_normalize(
    data,
    record_path="items",
    meta=[
        "order_id",
        "order_date",
        ["customer", "name"],
        ["customer", "city"]
    ]
)

utils.print_df(f" nested 저장 normaliz json", itemDF)
print("컬럼이름 인덱스 -> ", itemDF.columns)
print("행      인덱스 -> ", itemDF.index)
print("DF 형태 정보   -> ", itemDF.shape)






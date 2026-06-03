## ===========================================
##      Series 인스턴스 생성과 데이터 자료형
## -------------------------------------------
## * List/Tuple/Set/Str 데이터  ==> Series
## * Dict 데이터                ==> Series
## ===========================================
## -------------------------------------------
## [1] 모듈 로딩
## -------------------------------------------
import pandas as pd 
import func as fc

## -------------------------------------------
## [2] Seires 인스턴스 생성
## -------------------------------------------
## 데이터 준비
data1 = [11,33,55,77]
data2 = 111,333,222
data3 = {1, 4, 7, 1, 9, 8, 1, 3}
data4 = {'A':90, 'B':80}
data5 = "Good"

## Series 인스턴스 생성
sr1 = pd.Series(data1)
sr2 = pd.Series(data2) 
#sr3 = pd.Series(data3)    ## unsequence type 불가
sr4 = pd.Series(data4)     ## dict => Series 시 key는 인덱스로 설정!!!
sr5 = pd.Series(data5)

## Series 인스턴스 정보 확인
fc.print_info(sr1, 'sr1')
fc.print_info(sr2, 'sr2')
##fc.print_info(sr3, 'sr3')
fc.print_info(sr4, 'sr4')
fc.print_info(sr5, 'sr5')
## ===================================
##          Series 연산
## ===================================
## [1] 모듈 로딩
import pandas as pd 

## [2] Series 인스턴스 생성
sr1 = pd.Series([11,22,33, pd.NA])

## -------------------------------------
## [3] 연산
## -------------------------------------
## [3-1] Seires와 숫자 연산
## -------------------------------------
print(f"\nsr1 + 10 ===>\n{sr1 + 10}")
print(f"\nsr1 * 10 ===>\n{sr1 * 10}")
print(f"\nsr1 % 10 ===>\n{sr1 % 10}")
print(f"\nsr1 >= 20 ===>\n{sr1 >= 20}")

## -------------------------------------
## [3-2] Seires와 Seires 연산
## -------------------------------------
sr2 = pd.Series([3, 11, 2, 4])
print(f"\nsr1 + sr2  ===>\n{sr1 + sr2}")
print(f"\nsr1 * sr2  ===>\n{sr1 * sr2}")
print(f"\nsr1 % sr2  ===>\n{sr1 % sr2}")
print(f"\nsr1 >= sr2 ===>\n{sr1 >= sr2}")

sr2 = pd.Series([3, 11, 2, 4], 
                index=[0,1,3,5])
print(f"\nsr1 + sr2  ===>\n{sr1 + sr2}")
print(f"\nsr1 * sr2  ===>\n{sr1 * sr2}")
print(f"\nsr1 % sr2  ===>\n{sr1 % sr2}")

## -------------------------------------
## [3-3] Seires 연산관련 메서드 활용
##       -> 같은 인덱스가 없는 경우 : NaN
##       -> 데이터가 NaN인 경우    : NaN
##       => 해결 : fill_value 매개변수
## -------------------------------------
print(f"\nsr1.add(sr2) ==>\n{sr1.add(sr2, fill_value=0)}")
print(f"\nsr1.sub(sr2) ==>\n{sr1.sub(sr2, fill_value=0)}")
print(f"\nsr1.mul(sr2) ==>\n{sr1.mul(sr2, fill_value=1)}")
print(f"\nsr1.div(sr2) ==>\n{sr1.div(sr2, fill_value=1)}")
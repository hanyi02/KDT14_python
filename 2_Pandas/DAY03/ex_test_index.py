## ======================================================
## 인덱스 제어 관련
## ======================================================
## 모듈 로딩
import pandas as pd 

## 데이터 준비
data = {'상품코드' : ['P001', 'P002', 'P003', 'P004','P005'],
        '상품명'   : ['노트북','마우스', '의자','책상','키보드'],
        '가격'     : [1200000, 25000, 85000, 150000, 45000],
        '재고'     : [5, 30, 12, 7, 20],
        '카테고리'  : ['전자제품', '전자제품', '가구','가구','전자제품']}


## 사용자 정의 함수
def display(obj, obj_name):
    print(f"\n{obj_name}===\n{obj}")

# ----------------------------
# 문제 01) products DataFrame의 인덱스를 출력하세요. 
# ----------------------------
products = pd.DataFrame(data)
print(f'index => {products.index}')
display(products, 'products')

# ----------------------------
# 문제 02) 상품코드 열을 인덱스로 설정한 products2 DataFrame을 생성하세요. 
# ----------------------------
products2 = products.set_index('상품코드')
display(products2, 'products2')

# ----------------------------
# 문제 03) products2 DataFrame에서 인덱스가 P003인 행을 선택하여 출력하세요. 
# ----------------------------
p003SR = products2.loc['P003']
display(p003SR, 'p003SR')

p003SR = products2.iloc[2]
display(p003SR, 'p003SR')

# ----------------------------
# 문제 04) products2 DataFrame에서 P001, P004, P005 행을 선택하여 출력하세요. 
# ----------------------------
p00145DF = products2.loc[['P001', 'P004', 'P005']]
display(p00145DF, 'p00145DF')

# ----------------------------
# 문제 05) products2 DataFrame에서 P002부터 P004까지 선택하여 출력하세요. 
# ----------------------------
p00234DF = products2.loc['P002': 'P004']
display(p00234DF, 'p00234DF')

# ----------------------------
# 문제 06) products2 DataFrame의 인덱스 이름을 code로 변경하세요. 
# ----------------------------
products2.index.name = 'code'
display(products2, 'products2')

# ----------------------------
# 문제 07) products2 DataFrame의 인덱스를 다시 일반 컬럼으로 되돌리세요. 
# ----------------------------
products2.index.name = '상품코드'
products2.reset_index(inplace=True)
display(products2, 'products2')

# ----------------------------
# 문제 08) 상품명 열을 인덱스로 설정한 products3 DataFrame을 생성하세요. 
# ----------------------------
products3 = products.set_index('상품명')
display(products3, 'products3')

# ----------------------------
# 문제 09) products3 DataFrame에서 인덱스 값 노트북을 고성능노트북으로 변경하세요.
# ----------------------------
#products3.index = ["고성능노트북","마우스","의자","책상","키보드"]
## rename() : 변경해야되는 인덱스만 설정하면됨
## -> index   매개변수 = {이전인덱스:새인덱스}
## -> columns 매개변수 = {이전컬럼이름: 새컬럼이름}
products3 =  products3.rename(index={'노트북':'고성능노트북'})
display(products3, 'products3')

# ----------------------------
# 문제 10) products3 DataFrame의 인덱스를 오름차순으로 정렬하세요. 
# ----------------------------
products3 = products3.sort_index()
display(products3, 'products3')

# ----------------------------
# 문제 11) products3 DataFrame의 인덱스를 내림차순으로 정렬하세요. 
# ----------------------------
products3 = products3.sort_index(ascending=False)
display(products3, 'products3') 

# ----------------------------
# 문제 12) products3 DataFrame의 인덱스를 초기화하여 0, 1, 2, 3, 4 형태의 
#          정수 인덱스로 변경하세요
# ----------------------------
products3 = products3.reset_index()
display(products3, 'products3') 

print("\n---------------------")

# 문제 13) 다음 Series를 생성한 후, 인덱스에 중복 값이 있는지 확인하세요. 
s = pd.Series( [10, 20, 30, 40], index=["A", "B", "A", "C"] )
print( s.index )
print( s.index.duplicated() )
print( s.index.has_duplicates )

# 문제 14) 문제 13의 Series에서 인덱스가 A인 값을 선택하여 출력하세요.
print(s['A'])
print("\n---------------------")
# # ----------------------------
# # 문제 15) 다음 조건을 모두 수행하세요. 
# # ----------------------------
# #       → products DataFrame에서 상품코드를 인덱스로 설정하세요. 
# products = products.set_index('상품코드')
# display(products, "[상품코드를 인덱스로]")

# #       → 인덱스 이름을 product_code로 변경하세요. 
# products.index.name = 'product_code'
# display(products, "[인덱스 이름을 product_code]")

# #       → P002와 P005 행을 선택하세요. 
# display(products.loc[['P002','P005']] , "[P002와 P005 행을 선택]")

# #       → P004 상품의 가격을 170000으로 수정하세요. 
# products.loc['P004', '가격'] = 170000
# display(products, "[P004 상품의 가격을 170000]")

# #       → 인덱스를 다시 일반 컬럼으로 초기화하세요. 
# products.index.name = '상품코드'
# products.reset_index(inplace=True)
# display(products, "[인덱스를 다시 일반 컬럼으로]")

# #       → 최종 DataFrame을 출력하세요.
# display(products, "[최종 DataFrame]")

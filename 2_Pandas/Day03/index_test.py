import pandas as pd

df= pd.DataFrame({'상품코드': ['P001', 'P002', 'P003', 'P004', 'P005'],
                         '상품명': ['노트북', '마우스', '의자', '책상', '키보드'],
                         '가격': [1200000, 25000, 85000, 150000, 45000],
                         '재고': [5, 30, 12,7, 20],
                         '카테고리': ['전자제품', '전자제품', '가구', '가구', '전자제품']           
                         })

print("df===", df, sep='\n')


# 1. product DataFrame 인덱스 출력하세요
print(df.index) # RangeIndex(start=0, stop=5, step=1)

# 2. 상품코드 열을 인덱스로 설정한 product2 DataFrame을 생성하세요.
df2= df.set_index('상품코드')
print("df2===", df2, sep='\n')

# 3. product2 DataFrame에서 인덱스가 P003인 행을 선택하여 출력하세요
print(df2.loc['P003'])

# 4. product2 DataFrame에서 P001, P004, P005 행을 선택하여 출력하세요
print(df2.loc[['P001', 'P004', 'P005']])

# 5. products2 DataFrame에서 P002부터 P004까지 선택하여 출력하세요.
print(df2.loc['P002':'P004'])

# 6. products2 DataFrame의 인덱스 이름을 code로 변경하세요.
df2.index.name = 'code'
print("index.name = 'code' ===", df2, sep='\n')

# 7. products2 DataFrame의 인덱스를 다시 일반 컬럼으로 되돌리세요.
df2= df2.reset_index()
print("reset_index===", df2, sep='\n')




# 8. 상품명 열을 인덱스로 설정한 products3 DataFrame을 생성하세요.
df3= df.set_index('상품명')
print("df3===", df3, sep='\n')

# 9. products3 DataFrame에서 인덱스 값 노트북을 고성능노트북으로 변경하세요.
# 안 해도 됨

# 10. products3 DataFrame의 인덱스를 오름차순으로 정렬하세요.
print("df3===", df3.sort_index(ascending=True), sep='\n')


# 11. products3 DataFrame의 인덱스를 내림차순으로 정렬하세요.
print("df3===", df3.sort_index(ascending=False), sep='\n')

# 12. products3 DataFrame의 인덱스를 초기화하여 0,1,2,3,4 형태로 변경하세요.
df3 = df3.reset_index(drop=True)

'''
문제 15)

→ products DataFrame에서 상품코드를 인덱스로 설정
→ 인덱스 이름을 product_code로 변경
→ P002와 P005 행 선택
→ P004 상품 가격을 170000으로 수정
→ 인덱스를 다시 컬럼으로 복구
→ 최종 출력

'''

products_final = df.set_index('상품코드')
products_final.index.name = 'product_code'

print(products_final.loc[['P002', 'P005']])

products_final.loc['P004', '가격'] = 170000

products_final = products_final.reset_index()

print(products_final)


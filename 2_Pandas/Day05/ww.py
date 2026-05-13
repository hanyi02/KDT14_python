##      Pandas 기초 통계 함수 + 결측치 + 중복값 처리 실습 문제 [1] ---- 이한이


# 문제 1) vgsales.csv 파일을 읽어 DataFrame df를 생성하세요.
print("\n문제 1")
df = pd.read_csv('vgsales.csv')

# 문제 2) df의 앞 5행과 마지막 2행 출력하세요.
print("\n문제 2")
print(df.head(5))
print(df.tail(2))

# 문제 3) df의 행 개수와 열 개수를 확인하세요.
print("\n문제 3")
print(f"행 개수: {df.shape[0]}")
print(f"열 개수: {df.shape[1]}")

# 문제 4) df의 전체 정보를 확인하세요.
print("\n문제 4")
df.info()

# 문제 5) df의 숫자형 컬럼에 대한 기초 통계 정보를 출력하세요.
print("\n문제 5")
print(df.describe())

# 문제 6) Global_Sales 컬럼의 평균값/최소값/최대값/중앙값/전체합계 계산 후 출력하세요.
print("\n문제 6")
print(f"평균값: {df['Global_Sales'].mean()}")
print(f"최소값: {df['Global_Sales'].min()}")
print(f"최대값: {df['Global_Sales'].max()}")
print(f"중앙값: {df['Global_Sales'].median()}")
print(f"전체합계: {df['Global_Sales'].sum()}")

# 문제 7) Global_Sales 컬럼의 데이터 개수를 구하세요.
print("\n문제 7")
print(f"데이터 개수: {df['Global_Sales'].count()}")

# 문제 8) Year 컬럼의 평균값/중앙값/최빈값 구하세요.
print("\n문제 8")
print(f"평균값: {df['Year'].mean()}")
print(f"중앙값: {df['Year'].median()}")
print(f"최빈값: {df['Year'].mode()[0]}")

# 문제 9) Genre 컬럼에 어떤 장르 값들이 있는지 중복 없이 출력하세요.
print("\n문제 9")
print(df['Genre'].unique())

# 문제 10) Genre 컬럼의 고유값 개수를 구하세요.
print("\n문제 10")
print(f"고유값 개수: {df['Genre'].nunique()}")

# 문제 11) 전체 데이터에 결측치가 있는지 True/False 형태로 확인하세요.
print("\n문제 11")
print(df.isnull().any().any())

# 문제 12) 컬럼별 결측치 개수를 출력하세요. 전체 결측치 개수를 구하세요.
print("\n문제 12")
print("컬럼별 결측치:\n", df.isnull().sum())
print(f"전체 결측치 개수: {df.isnull().sum().sum()}")

# 문제 13) 각 컬럼에 결측치가 전혀 없는지 확인하세요.
print("\n문제 13")
print(df.isnull().sum() == 0)

# 문제 14) 결측치가 하나라도 있는 행을 삭제한 후 df_drop 변수에 저장하세요.
print("\n문제 14")
df_drop = df.dropna()

# 문제 15) 결측치 삭제 전과 삭제 후의 행 개수를 비교하세요.
print("\n문제 15")
print(f"삭제 전 행 개수: {len(df)}")
print(f"삭제 후 행 개수: {len(df_drop)}")
print(f"삭제된 행 개수: {len(df) - len(df_drop)}")

# 문제 16) Publisher 컬럼의 결측치를 "Unknown"으로 채운 후 df_fill_pub 변수에 저장하세요.
print("\n문제 16")
df_fill_pub = df.copy()
df_fill_pub['Publisher'] = df_fill_pub['Publisher'].fillna("Unknown")

# 문제 17) Publisher 컬럼의 결측치가 제대로 처리되었는지 확인하세요.
print("\n문제 17")
print(f"처리 전 Publisher 결측치 개수: {df['Publisher'].isnull().sum()}")
print(f"처리 후 Publisher 결측치 개수: {df_fill_pub['Publisher'].isnull().sum()}")

# 문제 18) Year 컬럼의 결측치를 Year 컬럼의 평균값으로 채우세요. [조건] 평균값은 정수로 변환해서 사용하세요.
print("\n문제 18")
avg_year = int(df['Year'].mean())
df_year_mean = df.copy()
df_year_mean['Year'] = df_year_mean['Year'].fillna(avg_year)

# 문제 19) Year 컬럼의 결측치를 Year 컬럼의 중앙값으로 채우세요. [조건] 중앙값은 정수로 변환해서 사용하세요.
print("\n문제 19")
med_year = int(df['Year'].median())
df_year_median = df.copy()
df_year_median['Year'] = df_year_median['Year'].fillna(med_year)

# 문제 20) Year 컬럼의 결측치를 Year 컬럼의 최빈값으로 채우세요.
print("\n문제 20")
mode_year = df['Year'].mode()[0]
df_year_mode = df.copy()
df_year_mode['Year'] = df_year_mode['Year'].fillna(mode_year)

# 문제 21) Year와 Publisher 컬럼의 결측치를 모두 처리한 df_fill 변수 만들기
print("\n문제 21")
df_fill = df.copy()
df_fill['Publisher'] = df_fill['Publisher'].fillna("Unknown")
df_fill['Year'] = df_fill['Year'].fillna(df['Year'].mode()[0])

# 문제 22) 전체 행 기준으로 중복 데이터가 있는지 확인하세요. 전체 행 기준 중복 데이터 개수를 구하세요.
print("\n문제 22")
print(f"중복 존재 여부: {df.duplicated().any()}")
print(f"중복 데이터 개수: {df.duplicated().sum()}")

# 문제 23) Name 컬럼 기준으로 중복된 데이터가 있는지 확인하세요. Name 컬럼 기준으로 중복된 데이터 개수를 구하세요.
print("\n문제 23")
print(f"Name 기준 중복 개수: {df.duplicated(['Name']).sum()}")

# 문제 24) Name, Platform, Year 컬럼을 기준으로 중복 여부를 확인하세요. Name, Platform, Year 기준으로 중복된 데이터 개수를 구하세요.
print("\n문제 24")
print(f"3개 컬럼 기준 중복 개수: {df.duplicated(['Name', 'Platform', 'Year']).sum()}")

# 문제 25) 전체 행 기준으로 중복을 제거한 후 df_no_dup_all 변수에 저장하세요. 전체 행 기준 중복 제거 전후의 행 개수를 비교하세요.
print("\n문제 25")
df_no_dup_all = df.drop_duplicates()
print(f"중복 제거 전 행 개수: {len(df)}")
print(f"중복 제거 후 행 개수: {len(df_no_dup_all)}")
print(f"제거된 행 개수: {len(df) - len(df_no_dup_all)}")

# 문제 26) Name 컬럼 기준으로 중복을 제거한 후 df_no_dup_name 변수에 저장하세요. 
#          Name, Platform, Year 기준으로 중복을 제거한 후 df_no_dup_game 변수에 저장하세요.
print("\n문제 26")
df_no_dup_name = df.drop_duplicates(['Name'])
df_no_dup_game = df.drop_duplicates(['Name', 'Platform', 'Year'])

# 문제 27) Name, Platform, Year 기준으로 중복 제거 후 인덱스를 0부터 다시 설정하세요.
print("\n문제 27")
df_no_dup_game_reset = df_no_dup_game.reset_index(drop=True)

# 문제 28) 중복 제거 전후의 인덱스 차이를 확인하세요.
print("\n문제 28")
print(f"제거 전 마지막 인덱스: {df.index[-1]}")
print(f"제거 후 마지막 인덱스: {df_no_dup_game_reset.index[-1]}")


## ==================================================================
##         Pandas 기초 통계 함수 + 결측치 + 중복값 처리 실습 문제 [2]
## ==================================================================

# [문제 1] 남북한발전전력량.xlsx 파일을 읽어서 df 변수에 저장하세요. 그 후 전체 데이터를 출력하세요.
print("\n문제 1")
df = pd.read_excel('남북한발전전력량.xlsx')

# [문제 2] df의 기본 정보를 확인하세요. (행/열 개수, 컬럼명, 인덱스, 자료형, 앞부분 5행)
print("\n문제 2")
print(f"1. 행과 열의 개수: {df.shape}")
print(f"2. 컬럼명: {df.columns.tolist()}")
print(f"3. 인덱스 정보: {df.index}")
print(f"4. 각 컬럼의 자료형:\n{df.dtypes}")
print(f"5. 앞부분 5행:\n{df.head()}")

# [문제 3] 현재 df의 컬럼명을 출력하세요. 그 후 첫 번째 컬럼명을 "구분"으로 변경하세요.
print("\n문제 3")
df.columns.values[0] = "구분"
print(f"변경 후 첫 번째 컬럼명: {df.columns[0]}")

# [문제 4] df에 결측치가 있는지 확인하세요. (컬럼별 개수, 전체 개수)
print("\n문제 4")
print(f"1. 컬럼별 결측치 개수:\n{df.isnull().sum()}")
print(f"2. 전체 결측치 개수: {df.isnull().sum().sum()}")

# [문제 5] 구분 컬럼의 결측치를 바로 위의 값으로 채우세요. 처리 전과 처리 후의 결측치 개수를 비교하세요.
print("\n문제 5")
print(f"처리 전 '구분' 결측치: {df['구분'].isnull().sum()}")
df['구분'] = df['구분'].ffill()
print(f"처리 후 '구분' 결측치: {df['구분'].isnull().sum()}")

# [문제 6] df에 완전히 동일한 행이 중복되어 있는지 확인하세요. (중복 여부 및 개수 출력)
print("\n문제 6")
print(f"중복 여부: {df.duplicated().any()}")
print(f"중복 행 개수: {df.duplicated().sum()}")

# [문제 7] 특정 컬럼(구분, 발전 전력별, 1990, 2000, 2010, 2016)만 선택하여 새로운 DataFrame df_basic을 만드세요.
print("\n문제 7")
df_basic = df[["구분", "발전 전력별", "1990", "2000", "2010", "2016"]]

# [문제 8] df에서 앞쪽 5개 행, 마지막 3개 행만 선택하여 출력하세요.
print("\n문제 8")
print("앞쪽 5행:", df.head(5))
print("마지막 3행:", df.tail(3))

# [문제 9] 0번부터 3번 행까지 선택하고, "구분", "발전 전력별", "1990", "2016" 컬럼만 출력하세요. [조건] 조건식은 사용하지 마세요.
print("\n문제 9")
print(df.loc[0:3, ["구분", "발전 전력별", "1990", "2016"]])

# [문제 11] "발전 전력별" 컬럼을 인덱스로 설정한 df_power를 만드세요. (원본 유지, 변경된 인덱스 출력)
print("\n문제 11")
df_power = df.set_index("발전 전력별")
print(df_power.index)

# [문제 12] 문제 11에서 만든 df_power의 인덱스를 다시 컬럼으로 되돌리세요.
print("\n문제 12")
df_reset = df_power.reset_index()

# [문제 13] 1990년부터 2016년까지의 연도 컬럼만 선택하여 df_years 변수에 저장하세요.
print("\n문제 13")
df_years = df.drop(['구분', '발전 전력별'], axis=1)
df_years = df_years.apply(pd.to_numeric, errors='coerce')

# [문제 14] df_years의 기초 통계 정보를 확인하세요.
print("\n문제 14")
print(df_years.describe())

# [문제 15] df_years에서 각 연도별 평균값을 구하세요.
print("\n문제 15")
print(df_years.mean())

# [문제 16] df_years에서 각 행의 평균 발전 전력량을 구하여 df에 "평균" 컬럼으로 추가하세요.
print("\n문제 16")
df['평균'] = df_years.mean(axis=1)

# [문제 17] 각 행에서 연도별 발전 전력량의 최대값과 최소값을 구하여 최대값, 최소값 컬럼을 추가하세요.
print("\n문제 17")
df['최대값'] = df_years.max(axis=1)
df['최소값'] = df_years.min(axis=1)

# [문제 18] 각 행에 대해 2016년 발전 전력량에서 1990년 발전 전력량을 뺀 값을 구하여 "1990_2016_변화량" 컬럼을 추가하세요.
print("\n문제 18")
df['1990_2016_변화량'] = df_years['2016'] - df_years['1990']

# [문제 19] 각 행에 대해 1990년 대비 2016년 변화율을 계산하여 "1990_2016_변화율" 컬럼을 추가하세요.
print("\n문제 19")
df['1990_2016_변화율'] = (df_years['2016'] - df_years['1990']) / df_years['1990'] * 100

# [문제 20] 2016년 컬럼에서 가장 큰 값을 구하세요.
print("\n문제 20")
print(f"2016년 최대값: {df_years['2016'].max()}")

# [문제 21] 1990년 컬럼에서 가장 작은 값을 구하세요.
print("\n문제 21")
print(f"1990년 최소값: {df_years['1990'].min()}")

# [문제 22] 2000년부터 2010년까지의 컬럼만 선택하여 출력하세요.
print("\n문제 22")
print(df.loc[:, "2000":"2010"])

# [문제 23] df를 복사하여 df_copy를 만드세요. df_copy에서 "평균", "최대값", "최소값" 컬럼을 삭제하세요.
print("\n문제 23")
df_copy = df.copy()
df_copy = df_copy.drop(["평균", "최대값", "최소값"], axis=1)

# [문제 24] "1990_2016_변화량" 컬럼을 기준으로 큰 값부터 정렬하세요.
print("\n문제 24")
df_sorted = df.sort_values(by="1990_2016_변화량", ascending=False)
print(df_sorted[["구분", "발전 전력별", "1990_2016_변화량"]].head())

# [문제 25] "구분" 컬럼을 기준으로 다음 값을 가지는 "구분코드" 컬럼을 추가하세요.
print("\n문제 25")
df['구분코드'] = df['구분'].apply(lambda x: 0 if '남한' in str(x) else 1)
print(df[['구분', '구분코드']])
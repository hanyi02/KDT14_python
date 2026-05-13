
import pandas as pd
import numpy as np
import sys
import seaborn as sns

# 3장------------------------------------------------------------

# ============================================================
# 1. 데이터 불러오기
# ============================================================

file_path = "../2_Pandas/Data/auto_mpg.csv"

car_df = pd.read_csv(file_path)

car_df.columns = [
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "model_year",
    "origin",
    "car_name"
]


# ============================================================
# 2. 데이터 앞부분 / 뒷부분 확인
# ============================================================

print("\n[데이터 앞 5행]")
print(car_df.head())

print("\n[데이터 뒤 5행]")
print(car_df.tail())


# ============================================================
# 3. 데이터프레임 구조 확인
# ============================================================

print("\n[행과 열 개수]")
print(car_df.shape)

print("\n[데이터프레임 기본 정보]")
car_df.info()

print("\n[열별 자료형]")
print(car_df.dtypes)

print("\n[mpg 열의 자료형]")
print(car_df["mpg"].dtype)


print("\n[숫자형 데이터 통계 요약]")
print(car_df.describe())

print("\n[전체 열 통계 요약]")
print(car_df.describe(include="all"))

print("\n[숫자형 열만 통계 요약]")
print(car_df.describe(include="number"))

print("\n[문자형 열만 통계 요약]")
print(car_df.describe(include="object"))


# ============================================================
# 4. 데이터 개수 및 고유값 확인
# ============================================================

print("\n[열별 유효 데이터 개수]")
print(car_df.count())

print("\n[origin 값별 개수]")
origin_count = car_df["origin"].value_counts()
print(origin_count)

print("\n[origin 값별 비율]")
origin_ratio = car_df["origin"].value_counts(normalize=True)
print(origin_ratio)

print("\n[origin 값별 백분율]")
origin_percent = (origin_ratio * 100).round(1)
print(origin_percent)


# ============================================================
# 5. 주요 통계 함수 적용
# ============================================================

print("\n[숫자형 열 평균]")
print(car_df.mean(numeric_only=True))

print("\n[mpg 평균]")
print(car_df["mpg"].mean())

print("\n[mpg, weight 평균]")
print(car_df[["mpg", "weight"]].mean())

print("\n[숫자형 열 중앙값]")
print(car_df.median(numeric_only=True))

print("\n[mpg 중앙값]")
print(car_df["mpg"].median())

print("\n[숫자형 열 최댓값]")
print(car_df.max(numeric_only=True))

print("\n[mpg 최댓값]")
print(car_df["mpg"].max())

print("\n[숫자형 열 최솟값]")
print(car_df.min(numeric_only=True))

print("\n[mpg 최솟값]")
print(car_df["mpg"].min())

print("\n[숫자형 열 표준편차]")
print(car_df.std(numeric_only=True))

print("\n[mpg 표준편차]")
print(car_df["mpg"].std())


# ============================================================
# 6. 상관계수 확인
# ============================================================

print("\n[숫자형 열 전체 상관계수]")
print(car_df.corr(numeric_only=True))

print("\n[mpg와 weight의 상관계수]")
print(car_df[["mpg", "weight"]].corr())




# 5장------------------------------------------------------------


# ============================================================
# 1. 결측치 제거
# ============================================================

# titanic 데이터 불러오기
titanic = sns.load_dataset("titanic")

# 열별 결측치 개수 확인
missing_data = titanic.isna().sum()
print("\n[열별 결측치 개수]")
print(missing_data)

# 정상 데이터가 500개 이상 있는 열만 남기기
titanic_valid_cols = titanic.dropna(axis=1, thresh=500)

print("\n[결측치가 너무 많은 열 제거 후 컬럼]")
print(titanic_valid_cols.columns)

# age 열에 결측치가 있는 행 제거
titanic_age_clean = titanic.dropna(axis=0, subset=["age"], how="any")

print("\n[age 결측치 제거 후 행 개수]")
print(len(titanic_age_clean))

# age와 deck이 둘 다 결측치인 행 제거
titanic_age_deck_clean = titanic.dropna(
    axis=0,
    subset=["age", "deck"],
    how="all"
)

print("\n[age와 deck이 모두 결측치인 행 제거 후 행 개수]")
print(len(titanic_age_deck_clean))


# ============================================================
# 2. 평균값으로 결측치 대체
# ============================================================

titanic = sns.load_dataset("titanic")

print("\n[age 열 앞 10개 - 변경 전]")
print(titanic["age"].head(10))

# age 평균 계산
age_mean = titanic["age"].mean()

# age 결측치를 평균값으로 대체
titanic["age"] = titanic["age"].fillna(age_mean)

print("\n[age 열 앞 10개 - 평균값으로 변경 후]")
print(titanic["age"].head(10))


# ============================================================
# 3. 최빈값으로 결측치 대체
# ============================================================

titanic = sns.load_dataset("titanic")

print("\n[embark_town 825~829행 - 변경 전]")
print(titanic["embark_town"][825:830])

# 방법 1: value_counts() 사용
top_town = titanic["embark_town"].value_counts(dropna=True).idxmax()
print("\n[가장 많이 나온 승선 도시 - value_counts]")
print(top_town)

# 방법 2: mode() 사용
top_town2 = titanic["embark_town"].mode()[0]
print("\n[가장 많이 나온 승선 도시 - mode]")
print(top_town2)

# 결측치를 최빈값으로 대체
titanic["embark_town"] = titanic["embark_town"].fillna(top_town)

print("\n[embark_town 825~829행 - 최빈값 대체 후]")
print(titanic["embark_town"][825:830])


# ============================================================
# 4. 앞뒤 값으로 결측치 대체
# ============================================================

titanic = sns.load_dataset("titanic")
titanic_back = titanic.copy()

print("\n[embark_town 825~830행 - 원본]")
print(titanic["embark_town"][825:831])

# 앞의 값으로 채우기
titanic["embark_town"] = titanic["embark_town"].ffill()

print("\n[앞의 값으로 결측치 채운 결과]")
print(titanic["embark_town"][825:831])

# 뒤의 값으로 채우기
titanic_back["embark_town"] = titanic_back["embark_town"].bfill()

print("\n[뒤의 값으로 결측치 채운 결과]")
print(titanic_back["embark_town"][825:831])


# ============================================================
# 5. 중복 데이터 확인
# ============================================================

sample_df = pd.DataFrame({
    "c1": ["a", "a", "b", "a", "b"],
    "c2": [1, 1, 1, 2, 2],
    "c3": [1, 1, 2, 2, 2]
})

print("\n[중복 확인용 데이터프레임]")
print(sample_df)

# 전체 행 기준 중복 확인
dup_first = sample_df.duplicated()
print("\n[중복 확인 - keep='first']")
print(dup_first)

dup_last = sample_df.duplicated(keep="last")
print("\n[중복 확인 - keep='last']")
print(dup_last)

dup_all = sample_df.duplicated(keep=False)
print("\n[중복 확인 - keep=False]")
print(dup_all)

# 특정 열 기준 중복 확인
c2_dup = sample_df["c2"].duplicated()
print("\n[c2 열 기준 중복 확인]")
print(c2_dup)

# 데이터프레임에서 특정 열을 기준으로 중복 확인
c2_row_dup = sample_df.duplicated(subset=["c2"])
print("\n[c2 기준 행 중복 확인]")
print(c2_row_dup)


# ============================================================
# 6. 중복 데이터 제거
# ============================================================

sample_df = pd.DataFrame({
    "c1": ["a", "a", "b", "a", "b"],
    "c2": [1, 1, 1, 2, 2],
    "c3": [1, 1, 2, 2, 2]
})

print("\n[원본 데이터프레임]")
print(sample_df)

# 완전히 같은 행 제거
unique_first = sample_df.drop_duplicates()
print("\n[중복 제거 - keep='first']")
print(unique_first)

# 중복 중 마지막 값만 남기기
unique_last = sample_df.drop_duplicates(keep="last")
print("\n[중복 제거 - keep='last']")
print(unique_last)

# 중복되는 행은 모두 제거
unique_none = sample_df.drop_duplicates(keep=False)
print("\n[중복 제거 - keep=False]")
print(unique_none)

# c2, c3 기준으로 중복 제거
unique_c2_c3 = sample_df.drop_duplicates(subset=["c2", "c3"])
print("\n[c2, c3 기준 중복 제거]")
print(unique_c2_c3)

# c2, c3 기준으로 중복되는 행 모두 제거
unique_c2_c3_none = sample_df.drop_duplicates(
    subset=["c2", "c3"],
    keep=False
)

print("\n[c2, c3 기준 중복 행 모두 제거]")
print(unique_c2_c3_none)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 페이지 기본 설정
# =========================
st.set_page_config(
    page_title="2024 전력 사용량 & 날씨 분석",
    layout="wide"
)

st.title("2024 지역별 전력 사용량 & 날씨 상관관계 분석")
st.caption("한국전력거래소 지역별 시간대별 전력거래량 데이터를 기반으로 지역·월·시간대별 전력 사용 패턴을 분석합니다.")

# =========================
# 데이터 불러오기
# =========================
@st.cache_data
def load_power_data():
    df = pd.read_csv(
        r"C:\KDT14\Project\한국전력거래소_지역별 시간대별 전력거래량_2024.csv",
        encoding="cp949"
    )

    # 날짜 / 시간 처리
    df["거래일자"] = pd.to_datetime(df["거래일자"])
    df["거래시간"] = df["거래시간"].astype(int)

    # 거래시간 1 = 00시, 24 = 23시로 처리
    df["거래일시"] = df["거래일자"] + pd.to_timedelta(df["거래시간"] - 1, unit="h")

    # 파생 컬럼 생성
    df["연도"] = df["거래일시"].dt.year
    df["월"] = df["거래일시"].dt.month
    df["일"] = df["거래일시"].dt.day
    df["시간"] = df["거래일시"].dt.hour
    df["요일"] = df["거래일시"].dt.day_name()

    return df


power = load_power_data()

# =========================
# 사이드바 필터
# =========================
st.sidebar.header("필터")

regions = sorted(power["지역"].unique())

selected_region = st.sidebar.selectbox(
    "지역 선택",
    regions
)

month_list = sorted(power["월"].unique())

selected_months = st.sidebar.multiselect(
    "월 선택",
    month_list,
    default=month_list
)

hour_range = st.sidebar.slider(
    "시간대 선택",
    min_value=0,
    max_value=23,
    value=(0, 23)
)

filtered = power[
    (power["지역"] == selected_region) &
    (power["월"].isin(selected_months)) &
    (power["시간"].between(hour_range[0], hour_range[1]))
]

# =========================
# 데이터 비어있는 경우 처리
# =========================
if filtered.empty:
    st.warning("선택한 조건에 해당하는 데이터가 없습니다.")
    st.stop()

# =========================
# KPI 영역
# =========================
st.subheader(f"{selected_region} 전력 사용량 요약")

total_power = filtered["전력거래량(MWh)"].sum()
avg_power = filtered["전력거래량(MWh)"].mean()
max_power = filtered["전력거래량(MWh)"].max()
min_power = filtered["전력거래량(MWh)"].min()

col1, col2, col3, col4 = st.columns(4)

col1.metric("총 전력거래량", f"{total_power:,.0f} MWh")
col2.metric("평균 전력거래량", f"{avg_power:,.2f} MWh")
col3.metric("최대 전력거래량", f"{max_power:,.2f} MWh")
col4.metric("최소 전력거래량", f"{min_power:,.2f} MWh")

st.divider()

# =========================
# 차트 1: 시간대별 평균 전력거래량
# =========================
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("시간대별 평균 전력거래량")

    hourly = (
        filtered
        .groupby("시간")["전력거래량(MWh)"]
        .mean()
        .reset_index()
    )

    st.line_chart(
        hourly,
        x="시간",
        y="전력거래량(MWh)"
    )

with col_right:
    st.subheader("월별 총 전력거래량")

    monthly = (
        filtered
        .groupby("월")["전력거래량(MWh)"]
        .sum()
        .reset_index()
    )

    st.bar_chart(
        monthly,
        x="월",
        y="전력거래량(MWh)"
    )

st.divider()

# =========================
# 차트 2: 요일별 / 일자별 분석
# =========================
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("요일별 평균 전력거래량")

    weekday_order = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    ]

    weekday_kor = {
        "Monday": "월",
        "Tuesday": "화",
        "Wednesday": "수",
        "Thursday": "목",
        "Friday": "금",
        "Saturday": "토",
        "Sunday": "일"
    }

    weekday = (
        filtered
        .groupby("요일")["전력거래량(MWh)"]
        .mean()
        .reindex(weekday_order)
        .reset_index()
    )

    weekday["요일"] = weekday["요일"].map(weekday_kor)

    st.bar_chart(
        weekday,
        x="요일",
        y="전력거래량(MWh)"
    )

with col_right:
    st.subheader("일자별 전력거래량 추이")

    daily = (
        filtered
        .groupby("거래일자")["전력거래량(MWh)"]
        .sum()
        .reset_index()
    )

    st.line_chart(
        daily,
        x="거래일자",
        y="전력거래량(MWh)"
    )

st.divider()

# =========================
# 전체 지역 비교
# =========================
st.subheader("전체 지역별 총 전력거래량 비교")

region_total = (
    power[
        (power["월"].isin(selected_months)) &
        (power["시간"].between(hour_range[0], hour_range[1]))
    ]
    .groupby("지역")["전력거래량(MWh)"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

st.bar_chart(
    region_total,
    x="지역",
    y="전력거래량(MWh)"
)

st.divider()

# =========================
# 피크 시간 분석
# =========================
st.subheader("피크 전력 사용 시간 분석")

peak_row = filtered.loc[filtered["전력거래량(MWh)"].idxmax()]

col1, col2, col3 = st.columns(3)

col1.metric("피크 날짜", peak_row["거래일자"].strftime("%Y-%m-%d"))
col2.metric("피크 시간", f"{int(peak_row['시간'])}시")
col3.metric("피크 전력거래량", f"{peak_row['전력거래량(MWh)']:,.2f} MWh")

st.divider()

# =========================
# 기초 통계
# =========================
st.subheader("전력거래량 기초 통계")

stats = filtered["전력거래량(MWh)"].describe().to_frame()
stats.columns = ["전력거래량(MWh)"]

st.dataframe(stats)

st.divider()

# =========================
# 데이터 미리보기
# =========================
st.subheader("데이터 미리보기")

show_cols = [
    "거래일자",
    "거래시간",
    "거래일시",
    "지역",
    "전력거래량(MWh)",
    "월",
    "시간",
    "요일"
]

st.dataframe(filtered[show_cols].head(100))

# =========================
# 원본 데이터 크기 표시
# =========================
st.caption(f"전체 데이터 크기: {power.shape[0]:,}행 × {power.shape[1]:,}열")
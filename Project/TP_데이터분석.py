import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="2024 전력 사용량 & 날씨 분석",
    layout="wide"
)

st.title("2024 지역별 전력 사용량 & 날씨 상관관계 분석")

@st.cache_data
def load_power_data():
    df = pd.read_csv(
    r"C:\KDT14\Project\한국전력거래소_지역별 시간대별 전력거래량_2024.csv",
    encoding="cp949"
)

    df["거래일자"] = pd.to_datetime(df["거래일자"])
    df["거래시간"] = df["거래시간"].astype(int)
    df["거래일시"] = df["거래일자"] + pd.to_timedelta(df["거래시간"] - 1, unit="h")

    df["월"] = df["거래일시"].dt.month
    df["일"] = df["거래일시"].dt.day
    df["시간"] = df["거래일시"].dt.hour
    df["요일"] = df["거래일시"].dt.day_name()

    return df

power = load_power_data()

st.sidebar.header("필터")

regions = sorted(power["지역"].unique())
selected_region = st.sidebar.selectbox("지역 선택", regions)

filtered = power[power["지역"] == selected_region]

st.subheader(f"{selected_region} 전력 사용량 요약")

col1, col2, col3 = st.columns(3)

col1.metric("총 전력거래량", f"{filtered['전력거래량(MWh)'].sum():,.0f} MWh")
col2.metric("평균 전력거래량", f"{filtered['전력거래량(MWh)'].mean():,.2f} MWh")
col3.metric("최대 전력거래량", f"{filtered['전력거래량(MWh)'].max():,.2f} MWh")

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("시간대별 평균 전력거래량")
    hourly = filtered.groupby("시간")["전력거래량(MWh)"].mean()
    st.line_chart(hourly)

with col_right:
    st.subheader("월별 총 전력거래량")
    monthly = filtered.groupby("월")["전력거래량(MWh)"].sum()
    st.bar_chart(monthly)

st.divider()

st.subheader("데이터 미리보기")
st.dataframe(filtered.head(100))
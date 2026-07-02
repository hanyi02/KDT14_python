import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path

# =========================================================
# 0. 페이지 설정
# =========================================================
st.set_page_config(
    page_title="2024 지역별 전력 사용량 & 기상 분석",
    layout="wide"
)

st.title("2024 지역별 전력 사용량 & 기상 데이터 분석")
st.caption(
    "지역별 전력 사용량을 기온, 강수량, 습도, 산업/주거 특성과 함께 비교 분석합니다."
)

# =========================================================
# 1. 파일 경로 설정
# =========================================================
POWER_FILE = r"한국전력거래소_지역별 시간대별 전력거래량_2024.csv"
WEATHER_FILE = r"weather_data.csv"
SECTOR_FILE = r"HOME_발전·판매_판매전력량_시도별용도별.csv"


# =========================================================
# 2. 공통 함수
# =========================================================
def find_file(file_path):
    candidates = [
        Path(file_path),
        Path(file_path).name,
        Path("dataset") / Path(file_path).name,
        Path("Project") / "dataset" / Path(file_path).name,
        Path.cwd() / Path(file_path).name,
        Path.cwd() / "dataset" / Path(file_path).name,
        Path.cwd() / "Project" / "dataset" / Path(file_path).name,
    ]

    for path in candidates:
        if Path(path).exists():
            return str(path)

    raise FileNotFoundError(f"파일을 찾을 수 없습니다: {Path(file_path).name}")


def safe_read_csv(file_path):
    real_path = find_file(file_path)

    for enc in ["utf-8-sig", "cp949", "euc-kr", "utf-8"]:
        try:
            return pd.read_csv(real_path, encoding=enc)
        except UnicodeDecodeError:
            continue

    raise UnicodeDecodeError("encoding", b"", 0, 1, f"인코딩 실패: {file_path}")


def normalize_region(name):
    if not isinstance(name, str):
        return name

    name = name.strip()

    mapping = {
        "서울": "서울특별시",
        "부산": "부산광역시",
        "대구": "대구광역시",
        "인천": "인천광역시",
        "광주": "광주광역시",
        "대전": "대전광역시",
        "울산": "울산광역시",
        "세종": "세종특별자치시",
        "경기": "경기도",
        "강원": "강원도",
        "충북": "충청북도",
        "충남": "충청남도",
        "전북": "전라북도",
        "전남": "전라남도",
        "경북": "경상북도",
        "경남": "경상남도",
        "제주": "제주특별자치도",
    }

    city_to_prov = {
        "수원": "경기도",
        "양평": "경기도",
        "파주": "경기도",
        "이천": "경기도",
        "춘천": "강원도",
        "강릉": "강원도",
        "원주": "강원도",
        "청주": "충청북도",
        "홍성": "충청남도",
        "전주": "전라북도",
        "군산": "전라북도",
        "목포": "전라남도",
        "여수": "전라남도",
        "창원": "경상남도",
        "진주": "경상남도",
        "안동": "경상북도",
        "포항": "경상북도",
        "구미": "경상북도",
        "서귀포": "제주특별자치도",
    }

    if name in city_to_prov:
        return city_to_prov[name]

    for short, full in mapping.items():
        if short in name:
            return full

    return name


def to_number(series):
    return pd.to_numeric(
        series.astype(str).str.replace(",", "", regex=False),
        errors="coerce"
    )


# =========================================================
# 3. 데이터 로드 및 전처리
# =========================================================
@st.cache_data
def load_all_data():
    # -----------------------------
    # 전력 데이터
    # -----------------------------
    power = safe_read_csv(POWER_FILE)

    power["지역"] = power["지역"].apply(normalize_region)
    power["거래일자"] = pd.to_datetime(power["거래일자"])
    power["거래시간"] = power["거래시간"].astype(int)

    # 거래시간 1 = 00시, 24 = 23시
    power["거래일시"] = power["거래일자"] + pd.to_timedelta(power["거래시간"] - 1, unit="h")

    power["연도"] = power["거래일시"].dt.year
    power["월"] = power["거래일시"].dt.month
    power["일"] = power["거래일시"].dt.day
    power["시간"] = power["거래일시"].dt.hour
    power["요일번호"] = power["거래일시"].dt.dayofweek

    weekday_kor = {
        0: "월",
        1: "화",
        2: "수",
        3: "목",
        4: "금",
        5: "토",
        6: "일",
    }

    power["요일"] = power["요일번호"].map(weekday_kor)
    power["주말여부"] = np.where(power["요일번호"] >= 5, "주말", "평일")

    season_map = {
        12: "겨울", 1: "겨울", 2: "겨울",
        3: "봄", 4: "봄", 5: "봄",
        6: "여름", 7: "여름", 8: "여름",
        9: "가을", 10: "가을", 11: "가을",
    }

    power["계절"] = power["월"].map(season_map)

    power_daily = (
        power
        .groupby(["지역", "거래일자"], as_index=False)["전력거래량(MWh)"]
        .sum()
        .rename(columns={
            "거래일자": "date",
            "전력거래량(MWh)": "power_usage"
        })
    )

    # -----------------------------
    # 기상 데이터
    # -----------------------------
    weather = safe_read_csv(WEATHER_FILE)

    # 기상 파일 컬럼이 정확히 6개일 때 자동 정리
    if len(weather.columns) >= 6:
        weather = weather.iloc[:, :6]
        weather.columns = ["지점코드", "지점명", "일시", "temp", "강수량", "습도"]

    weather["지역"] = weather["지점명"].apply(normalize_region)
    weather["date"] = pd.to_datetime(weather["일시"]).dt.normalize()

    weather["temp"] = to_number(weather["temp"])
    weather["강수량"] = to_number(weather["강수량"]).fillna(0)
    weather["습도"] = to_number(weather["습도"])

    weather_daily = (
        weather
        .groupby(["지역", "date"], as_index=False)
        .agg({
            "temp": "mean",
            "강수량": "sum",
            "습도": "mean"
        })
    )

    # -----------------------------
    # 전력 + 기상 병합
    # -----------------------------
    daily = pd.merge(
        power_daily,
        weather_daily,
        on=["지역", "date"],
        how="inner"
    )

    daily["월"] = daily["date"].dt.month
    daily["요일번호"] = daily["date"].dt.dayofweek
    daily["주말여부"] = np.where(daily["요일번호"] >= 5, "주말", "평일")
    daily["계절"] = daily["월"].map(season_map)

    # 냉방도일, 난방도일
    daily["CDD"] = np.maximum(daily["temp"] - 24, 0)
    daily["HDD"] = np.maximum(18 - daily["temp"], 0)

    daily = daily.sort_values(["지역", "date"])
    daily["rolling_mean_7"] = (
        daily
        .groupby("지역")["power_usage"]
        .rolling(window=7, min_periods=1)
        .mean()
        .reset_index(level=0, drop=True)
    )

    # -----------------------------
    # 용도별 데이터
    # -----------------------------
    sector_raw = safe_read_csv(SECTOR_FILE)

    sector_clean = sector_raw.iloc[2:].copy()

    sector = pd.DataFrame({
        "지역": sector_clean.iloc[:, 0].apply(normalize_region),
        "주거용": to_number(sector_clean.iloc[:, 1]),
        "서비스업": to_number(sector_clean.iloc[:, 3]),
        "산업용": to_number(sector_clean.iloc[:, 33]),
        "합계": to_number(sector_clean.iloc[:, 34]),
    })

    sector = sector.dropna(subset=["지역", "합계"])
    sector = sector[sector["합계"] > 0]

    sector["기타"] = sector["합계"] - (
        sector["주거용"] + sector["서비스업"] + sector["산업용"]
    )

    sector["산업비중(%)"] = sector["산업용"] / sector["합계"] * 100
    sector["주거비중(%)"] = sector["주거용"] / sector["합계"] * 100

    sector["지역유형"] = np.where(
        sector["산업비중(%)"] >= 50,
        "공업도시형",
        "주거/상업도시형"
    )

    return power, daily, sector


try:
    power, daily, sector = load_all_data()
except Exception as e:
    st.error(f"데이터 로드 중 오류가 발생했습니다: {e}")
    st.stop()


# =========================================================
# 4. 사이드바 필터
# =========================================================
st.sidebar.header("필터")

regions = sorted(power["지역"].dropna().unique())
month_list = sorted(power["월"].dropna().unique())

selected_region = st.sidebar.selectbox(
    "상세 분석 지역 선택",
    regions
)

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

min_date = daily["date"].min().date()
max_date = daily["date"].max().date()

selected_dates = st.sidebar.date_input(
    "날짜 범위 선택",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(selected_dates) != 2:
    st.warning("날짜 범위를 시작일과 종료일 모두 선택해 주세요.")
    st.stop()

start_date = pd.to_datetime(selected_dates[0])
end_date = pd.to_datetime(selected_dates[1])


# =========================================================
# 5. 필터링
# =========================================================
filtered_hourly = power[
    (power["지역"] == selected_region) &
    (power["월"].isin(selected_months)) &
    (power["시간"].between(hour_range[0], hour_range[1])) &
    (power["거래일자"].between(start_date, end_date))
].copy()

filtered_daily = daily[
    (daily["지역"] == selected_region) &
    (daily["월"].isin(selected_months)) &
    (daily["date"].between(start_date, end_date))
].copy()

all_region_hourly = power[
    (power["월"].isin(selected_months)) &
    (power["시간"].between(hour_range[0], hour_range[1])) &
    (power["거래일자"].between(start_date, end_date))
].copy()

all_region_daily = daily[
    (daily["월"].isin(selected_months)) &
    (daily["date"].between(start_date, end_date))
].copy()

if filtered_hourly.empty or filtered_daily.empty:
    st.warning("선택한 조건에 해당하는 데이터가 없습니다.")
    st.stop()


# =========================================================
# 6. KPI 영역
# =========================================================
st.subheader(f"{selected_region} 전력 사용량 요약")

total_power = filtered_hourly["전력거래량(MWh)"].sum()
avg_power = filtered_hourly["전력거래량(MWh)"].mean()
max_power = filtered_hourly["전력거래량(MWh)"].max()
min_power = filtered_hourly["전력거래량(MWh)"].min()

avg_temp = filtered_daily["temp"].mean()
total_rain = filtered_daily["강수량"].sum()
avg_humidity = filtered_daily["습도"].mean()

region_sector = sector[sector["지역"] == selected_region]

col1, col2, col3, col4 = st.columns(4)

col1.metric("총 전력거래량", f"{total_power:,.0f} MWh")
col2.metric("평균 전력거래량", f"{avg_power:,.2f} MWh")
col3.metric("최대 전력거래량", f"{max_power:,.2f} MWh")
col4.metric("최소 전력거래량", f"{min_power:,.2f} MWh")

col5, col6, col7, col8 = st.columns(4)

col5.metric("평균 기온", f"{avg_temp:.1f} ℃")
col6.metric("총 강수량", f"{total_rain:.1f} mm")
col7.metric("평균 습도", f"{avg_humidity:.1f} %")

if not region_sector.empty:
    ind_ratio = region_sector["산업비중(%)"].iloc[0]
    city_type = region_sector["지역유형"].iloc[0]
    col8.metric("지역 유형", city_type, f"산업비중 {ind_ratio:.1f}%")
else:
    col8.metric("지역 유형", "용도별 데이터 없음")

st.divider()


# =========================================================
# 7. 기존 그래프 유지: 시간대, 월별, 요일별, 일자별
# =========================================================
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("시간대별 평균 전력거래량")

    hourly = (
        filtered_hourly
        .groupby("시간", as_index=False)["전력거래량(MWh)"]
        .mean()
    )

    fig_hourly = px.line(
        hourly,
        x="시간",
        y="전력거래량(MWh)",
        markers=True,
        title="시간대별 평균 전력 사용 패턴"
    )

    st.plotly_chart(fig_hourly, use_container_width=True)

with col_right:
    st.subheader("월별 총 전력거래량")

    monthly = (
        filtered_hourly
        .groupby("월", as_index=False)["전력거래량(MWh)"]
        .sum()
    )

    fig_monthly = px.bar(
        monthly,
        x="월",
        y="전력거래량(MWh)",
        title="월별 총 전력거래량"
    )

    st.plotly_chart(fig_monthly, use_container_width=True)

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("요일별 평균 전력거래량")

    weekday_order = ["월", "화", "수", "목", "금", "토", "일"]

    weekday = (
        filtered_hourly
        .groupby("요일", as_index=False)["전력거래량(MWh)"]
        .mean()
    )

    weekday["요일"] = pd.Categorical(
        weekday["요일"],
        categories=weekday_order,
        ordered=True
    )

    weekday = weekday.sort_values("요일")

    fig_weekday = px.bar(
        weekday,
        x="요일",
        y="전력거래량(MWh)",
        title="요일별 평균 전력거래량"
    )

    st.plotly_chart(fig_weekday, use_container_width=True)

with col_right:
    st.subheader("일자별 전력거래량 추이")

    daily_power = (
        filtered_hourly
        .groupby("거래일자", as_index=False)["전력거래량(MWh)"]
        .sum()
    )

    fig_daily = px.line(
        daily_power,
        x="거래일자",
        y="전력거래량(MWh)",
        title="일자별 전력거래량 추이"
    )

    st.plotly_chart(fig_daily, use_container_width=True)

st.divider()


# =========================================================
# 8. 날짜별 전력 + 기상 통합 그래프
# =========================================================
st.subheader("날짜별 전력 사용량과 기상 데이터 비교")

weather_option = st.selectbox(
    "비교할 기상 요소 선택",
    ["temp", "강수량", "습도"],
    format_func=lambda x: {
        "temp": "기온",
        "강수량": "강수량",
        "습도": "습도"
    }[x]
)

weather_label = {
    "temp": "기온(℃)",
    "강수량": "강수량(mm)",
    "습도": "습도(%)"
}[weather_option]

fig_weather = make_subplots(specs=[[{"secondary_y": True}]])

fig_weather.add_trace(
    go.Bar(
        x=filtered_daily["date"],
        y=filtered_daily["power_usage"],
        name="일별 전력 사용량",
        opacity=0.65,
        hovertemplate="전력 사용량: %{y:,.0f} MWh<extra></extra>"
    ),
    secondary_y=False
)

fig_weather.add_trace(
    go.Scatter(
        x=filtered_daily["date"],
        y=filtered_daily["rolling_mean_7"],
        name="7일 이동평균",
        mode="lines",
        hovertemplate="7일 이동평균: %{y:,.0f} MWh<extra></extra>"
    ),
    secondary_y=False
)

fig_weather.add_trace(
    go.Scatter(
        x=filtered_daily["date"],
        y=filtered_daily[weather_option],
        name=weather_label,
        mode="lines+markers",
        hovertemplate=f"{weather_label}: " + "%{y:.2f}<extra></extra>"
    ),
    secondary_y=True
)

fig_weather.update_layout(
    hovermode="x unified",
    legend=dict(orientation="h", y=1.1),
    height=520
)

fig_weather.update_yaxes(title_text="전력 사용량(MWh)", secondary_y=False)
fig_weather.update_yaxes(title_text=weather_label, secondary_y=True)

st.plotly_chart(fig_weather, use_container_width=True)

st.divider()


# =========================================================
# 9. 기온, 강수량, 습도별 산점도
# =========================================================
st.subheader("기상 요소별 전력 사용량 관계")

col1, col2, col3 = st.columns(3)

with col1:
    fig_temp = px.scatter(
        filtered_daily,
        x="temp",
        y="power_usage",
        color="계절",
        trendline="ols",
        title="기온 vs 전력 사용량",
        labels={
            "temp": "기온(℃)",
            "power_usage": "전력 사용량(MWh)"
        }
    )
    st.plotly_chart(fig_temp, use_container_width=True)

with col2:
    fig_rain = px.scatter(
        filtered_daily,
        x="강수량",
        y="power_usage",
        color="계절",
        trendline="ols",
        title="강수량 vs 전력 사용량",
        labels={
            "강수량": "강수량(mm)",
            "power_usage": "전력 사용량(MWh)"
        }
    )
    st.plotly_chart(fig_rain, use_container_width=True)

with col3:
    fig_humidity = px.scatter(
        filtered_daily,
        x="습도",
        y="power_usage",
        color="계절",
        trendline="ols",
        title="습도 vs 전력 사용량",
        labels={
            "습도": "습도(%)",
            "power_usage": "전력 사용량(MWh)"
        }
    )
    st.plotly_chart(fig_humidity, use_container_width=True)

st.divider()


# =========================================================
# 10. 전체 지역별 전력 사용량 비교
# =========================================================
st.subheader("전체 지역별 총 전력거래량 비교")

region_total = (
    all_region_hourly
    .groupby("지역", as_index=False)["전력거래량(MWh)"]
    .sum()
    .sort_values("전력거래량(MWh)", ascending=False)
)

region_total = pd.merge(
    region_total,
    sector[["지역", "산업비중(%)", "주거비중(%)", "지역유형"]],
    on="지역",
    how="left"
)

fig_region = px.bar(
    region_total,
    x="지역",
    y="전력거래량(MWh)",
    color="지역유형",
    title="지역별 총 전력거래량 비교",
    hover_data={
        "산업비중(%)": ":.1f",
        "주거비중(%)": ":.1f",
        "전력거래량(MWh)": ":,.0f"
    }
)

st.plotly_chart(fig_region, use_container_width=True)

st.divider()


# =========================================================
# 11. 대한민국 지도 버블차트
# =========================================================
st.subheader("대한민국 지도 기반 지역별 전력 사용량 버블차트")

region_center = {
    "서울특별시": [37.5665, 126.9780],
    "부산광역시": [35.1796, 129.0756],
    "대구광역시": [35.8714, 128.6014],
    "인천광역시": [37.4563, 126.7052],
    "광주광역시": [35.1595, 126.8526],
    "대전광역시": [36.3504, 127.3845],
    "울산광역시": [35.5384, 129.3114],
    "세종특별자치시": [36.4800, 127.2890],
    "경기도": [37.4138, 127.5183],
    "강원도": [37.8228, 128.1555],
    "충청북도": [36.8000, 127.7000],
    "충청남도": [36.5184, 126.8000],
    "전라북도": [35.7175, 127.1530],
    "전라남도": [34.8679, 126.9910],
    "경상북도": [36.4919, 128.8889],
    "경상남도": [35.4606, 128.2132],
    "제주특별자치도": [33.4996, 126.5312],
}

map_df = region_total.copy()
map_df["lat"] = map_df["지역"].map(lambda x: region_center.get(x, [np.nan, np.nan])[0])
map_df["lon"] = map_df["지역"].map(lambda x: region_center.get(x, [np.nan, np.nan])[1])
map_df = map_df.dropna(subset=["lat", "lon"])

fig_map = px.scatter_mapbox(
    map_df,
    lat="lat",
    lon="lon",
    size="전력거래량(MWh)",
    color="전력거래량(MWh)",
    hover_name="지역",
    hover_data={
        "전력거래량(MWh)": ":,.0f",
        "산업비중(%)": ":.1f",
        "주거비중(%)": ":.1f",
        "지역유형": True,
        "lat": False,
        "lon": False,
    },
    size_max=55,
    zoom=5.4,
    center={"lat": 36.3, "lon": 127.8},
    mapbox_style="carto-positron",
    title="전력 사용량이 클수록 원이 크고 색이 진하게 표시됩니다."
)

fig_map.update_layout(height=650, margin={"r": 0, "t": 50, "l": 0, "b": 0})

st.plotly_chart(fig_map, use_container_width=True)

st.divider()


# =========================================================
# 12. 공업도시형 vs 주거/상업도시형 비교
# =========================================================
st.subheader("공업도시형 vs 주거/상업도시형 전력 사용 패턴 비교")

city_compare = pd.merge(
    all_region_daily,
    sector[["지역", "산업비중(%)", "주거비중(%)", "지역유형"]],
    on="지역",
    how="left"
)

city_compare = city_compare.dropna(subset=["지역유형"])

type_summary = (
    city_compare
    .groupby("지역유형", as_index=False)
    .agg({
        "power_usage": "mean",
        "temp": "mean",
        "강수량": "mean",
        "습도": "mean",
        "산업비중(%)": "mean",
        "주거비중(%)": "mean"
    })
)

col1, col2 = st.columns(2)

with col1:
    fig_type_power = px.bar(
        type_summary,
        x="지역유형",
        y="power_usage",
        title="도시 유형별 평균 일일 전력 사용량",
        labels={
            "power_usage": "평균 일일 전력 사용량(MWh)"
        },
        hover_data={
            "산업비중(%)": ":.1f",
            "주거비중(%)": ":.1f"
        }
    )
    st.plotly_chart(fig_type_power, use_container_width=True)

with col2:
    fig_type_weather = px.scatter(
        city_compare,
        x="temp",
        y="power_usage",
        color="지역유형",
        hover_name="지역",
        trendline="ols",
        title="도시 유형별 기온-전력 관계",
        labels={
            "temp": "기온(℃)",
            "power_usage": "전력 사용량(MWh)"
        }
    )
    st.plotly_chart(fig_type_weather, use_container_width=True)

st.divider()


# =========================================================
# 13. 기온 민감도 랭킹
# =========================================================
st.subheader("지역별 기온 민감도 랭킹")

corr_data = []

for region in all_region_daily["지역"].dropna().unique():
    tmp = all_region_daily[all_region_daily["지역"] == region]

    if len(tmp) < 5:
        continue

    temp_corr = tmp["power_usage"].corr(tmp["temp"])
    rain_corr = tmp["power_usage"].corr(tmp["강수량"])
    humidity_corr = tmp["power_usage"].corr(tmp["습도"])

    s_tmp = sector[sector["지역"] == region]

    if not s_tmp.empty:
        ind_ratio = s_tmp["산업비중(%)"].iloc[0]
        res_ratio = s_tmp["주거비중(%)"].iloc[0]
        region_type = s_tmp["지역유형"].iloc[0]
    else:
        ind_ratio = np.nan
        res_ratio = np.nan
        region_type = "용도별 데이터 없음"

    corr_data.append({
        "지역": region,
        "기온상관계수": temp_corr,
        "강수량상관계수": rain_corr,
        "습도상관계수": humidity_corr,
        "기온상관계수_절대값": abs(temp_corr),
        "산업비중(%)": ind_ratio,
        "주거비중(%)": res_ratio,
        "지역유형": region_type
    })

corr_df = pd.DataFrame(corr_data)
corr_df = corr_df.sort_values("기온상관계수_절대값", ascending=True)

st.caption(
    "기온상관계수의 절대값이 0에 가까울수록 기온 변화와 전력 사용량의 관계가 약합니다. "
    "일반적으로 산업용 기저부하가 큰 지역은 기온 영향이 상대적으로 작게 나올 수 있습니다."
)

fig_corr = px.bar(
    corr_df,
    x="기온상관계수",
    y="지역",
    color="지역유형",
    orientation="h",
    title="지역별 기온-전력 상관계수",
    hover_data={
        "기온상관계수": ":.3f",
        "강수량상관계수": ":.3f",
        "습도상관계수": ":.3f",
        "산업비중(%)": ":.1f",
        "주거비중(%)": ":.1f",
        "기온상관계수_절대값": False
    }
)

fig_corr.update_layout(height=650)
fig_corr.update_yaxes(categoryorder="array", categoryarray=corr_df["지역"].tolist())

st.plotly_chart(fig_corr, use_container_width=True)

st.dataframe(corr_df, use_container_width=True)

st.divider()


# =========================================================
# 14. 피크 시간 분석
# =========================================================
st.subheader("피크 전력 사용 시간 분석")

peak_row = filtered_hourly.loc[filtered_hourly["전력거래량(MWh)"].idxmax()]

col1, col2, col3, col4 = st.columns(4)

col1.metric("피크 날짜", peak_row["거래일자"].strftime("%Y-%m-%d"))
col2.metric("피크 시간", f"{int(peak_row['시간'])}시")
col3.metric("피크 전력거래량", f"{peak_row['전력거래량(MWh)']:,.2f} MWh")
col4.metric("피크 요일", peak_row["요일"])

st.divider()


# =========================================================
# 15. 데이터 미리보기
# =========================================================
st.subheader("데이터 미리보기")

tab1, tab2, tab3 = st.tabs(["시간대별 전력 데이터", "일별 전력+기상 데이터", "용도별 전력 데이터"])

with tab1:
    show_cols = [
        "거래일자",
        "거래시간",
        "거래일시",
        "지역",
        "전력거래량(MWh)",
        "월",
        "시간",
        "요일",
        "주말여부",
        "계절"
    ]

    st.dataframe(filtered_hourly[show_cols].head(200), use_container_width=True)

with tab2:
    st.dataframe(filtered_daily.head(200), use_container_width=True)

with tab3:
    st.dataframe(sector, use_container_width=True)

st.caption(
    f"전력 원본 데이터: {power.shape[0]:,}행 × {power.shape[1]:,}열 / "
    f"일별 병합 데이터: {daily.shape[0]:,}행 × {daily.shape[1]:,}열 / "
    f"용도별 데이터: {sector.shape[0]:,}행 × {sector.shape[1]:,}열"
)
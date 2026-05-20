"""
<웹 크롤링- 공정 현장 센서 데이터 수집 및 고장 예측 시스템>
- 공정 현장 데이터는 웹에서 수집할 수 없기 때문에, 기상청 대구시 데이터 사용
-> 기온: 모터 온도, 습도: 공정 습도, 풍속: 팬 회전수

<전체 구조>
- 기상청 데이터를 공정 센서 데이터인 것처럼 사용 -> 웹 크롤링을 통해 수집
- 센서 데이터는 보통 노이즈가 많이 섞임. 적절한 전처리를 통해 고장 범위 선정
- 고장 범위: 모터 온도가 3분 연속 상승하거나, Threshold를 넘으면 고장 징후로 간주
"""


import urllib.request # 웹페이지 내용 불러오기(HTML)
import random
import time
import re #HTML 안에서 <td>...</td>같은 값 뽑을 때 사용
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'Malgun Gothic'

# 1.크롤링
def get_weather_data(city):
    try: #예외처리(와이파이 연결 오류 등) 로직 구현
        url= 'https://www.weather.go.kr/w/weather/land/city-obs.do'
        page= urllib.request.urlopen(url) #페이지 열기
        text= page.read().decode('utf-8') #read()에서 끝나면 바이트형태라 사람이 읽을 수 없음-> utf 변환으로 문자열 변환

        city_pos= text.find(f'>{city}</a>')
        if city_pos== -1: #대구 못찾으면 -1 반환-> 예외처리 즉시 종료
            raise ValueError(f'{city} 데이터를 찾을 수 없습니다.')

        text = text[city_pos:] #직접 HTML 까보면 여러 도시 나오고 부산~~~, 대구~~~~, 대전~~~ 구조라 대구부터 슬라이싱 해줌
        td_list=re.findall(r'<td[^>]*>(.*?)</td>', text) #<td> 값 전부추출

        # HTML 태그 제거
        clean_td= [re.sub(r'<.*?>', '', td).strip() for td in td_list]

        # 기온, 습도, 풍속
        temp = float(clean_td[6]) #크롤링하면 clean_td속 인덱스 6, 9, 12 자리가 시온습도풍속자리임
        humid = float(clean_td[9])
        wind = float(clean_td[12])

        return temp, humid, wind

    except Exception as e:
        print(f"데이터 수집 오류: {e}")
        return None, None, None


# 2.이상 판정
def check_abnormal(temp_hist, humid_hist, wind_hist):
    if len(temp_hist)< 3:
        return False #데이터 3개 미만이면 분석 못해서 종료

    #최근 3샘플 동안 온도 상승폭 확인
    temp_rise= temp_hist[-1]- temp_hist[-3]

    if temp_rise >= 3 and humid_hist[-1] >= 30 and wind_hist[-1] >= 10:
        return True #공정 멈춤
    # 조건:
    # 1) 온도 3도 이상 급상승
    # 2) 습도 임계치 이상
    # 3) 풍속 임계치 이상

    return False #정상


# 3. 초기 설정
city_name = '대구'
SAMPLE_COUNT= 20

real_temp_history= [] #실제 기온
real_humid_history= []
real_wind_history= []

noise_temp_history= []
noise_humid_history= []
noise_wind_history= []

# 그래프 설정
plt.ion() #실시간 그래프
fig, axes= plt.subplots(3, 1, figsize=(12, 10)) #서브 플롯써서 그래프 3개 생성

print(f"{city_name} 스마트 공정 모니터링 시스템 가동 중...")


try:
    for i in range(SAMPLE_COUNT):
        temp, humid, wind =get_weather_data(city_name)

        if temp is not None and humid is not None and wind is not None:
            #실제값 저장
            real_temp_history.append(temp)
            real_humid_history.append(humid)
            real_wind_history.append(wind)

            #노이즈 데이터 생성
            noise_temp= temp+ random.uniform(-1.0, 1.0)
            noise_humid= humid+ random.uniform(-5.0, 5.0)
            noise_wind= wind+ random.uniform(-2.0, 2.0)

            #비정상 상태 일부러 만들기(노이즈 추가로는 (매일 날씨가 어떨지 모르니까) 비정상 잘 안 나옴)
            if i >= 10: #샘플링 10부터 급상승로직
                noise_temp +=(i-9) * 1.6
                noise_humid+=30
                noise_wind+= 6

            noise_temp_history.append(round(noise_temp, 2))
            noise_humid_history.append(round(noise_humid, 2))
            noise_wind_history.append(round(noise_wind, 2))

            # 이상 판정
            abnormal= check_abnormal(
                noise_temp_history,noise_humid_history,noise_wind_history
            )

            status = "정상"
            if abnormal:
                status = "비정상 상태 감지 -> 공정 즉시 멈춤"

            # 4. 그래프 업데이트
            for ax in axes:
                ax.clear()

            x = range(1, len(noise_temp_history) + 1)

            # 온도 그래프
            axes[0].plot(x, real_temp_history, label='Ground Truth', linestyle=':')
            axes[0].plot(x, noise_temp_history, label='온도 센서(노이즈 추가)', linewidth=2)
            axes[0].set_title(f"온도 추세 / 상태: {status}")
            axes[0].set_ylabel("온도 (°C)")
            axes[0].legend(loc='upper left')
            axes[0].grid(True, alpha=0.3)

            # 습도 그래프
            axes[1].plot(x, real_humid_history, label='Ground Truth', linestyle=':')
            axes[1].plot(x, noise_humid_history, label='습도 센서(노이즈 추가)', linewidth=2)
            axes[1].axhline(y=30, linestyle='--', alpha=0.7, label='습도 Threshold')
            axes[1].set_title("습도 추세")
            axes[1].set_ylabel("습도 (%)")
            axes[1].legend(loc='upper left')
            axes[1].grid(True, alpha=0.3)

            # 풍속 그래프
            axes[2].plot(x, real_wind_history, label='Ground Truth', linestyle=':')
            axes[2].plot(x, noise_wind_history, label='풍속 센서(노이즈 추가)', linewidth=2)
            axes[2].axhline(y=10, linestyle='--', alpha=0.7, label='풍속 Threshold')
            axes[2].set_title("풍속 추세")
            axes[2].set_xlabel("샘플링 단위")
            axes[2].set_ylabel("풍속 (m/s)")
            axes[2].legend(loc='upper left')
            axes[2].grid(True, alpha=0.3)

            plt.tight_layout()
            plt.pause(1)

            print(
                f"[{i+1}/{SAMPLE_COUNT}] "
                f"온도={noise_temp_history[-1]:.2f}°C, "
                f"습도={noise_humid_history[-1]:.2f}%, "
                f"풍속={noise_wind_history[-1]:.2f}m/s, "
                f"상태={status}"
            )

            # 비정상 상태면 즉시 공정 멈춤
            if abnormal:
                print("\n비정상 상태 감지. 공정을 즉시 멈춥니다.")
                break

        time.sleep(1)

except KeyboardInterrupt:
    print("\n시스템을 종료합니다.")

plt.ioff()
print("\n공정 데이터 분석 종료")
plt.show()
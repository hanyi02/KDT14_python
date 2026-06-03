## ====================================================
## 패키지(Package) : 관련된 모듈을 하나로 묶은 것
## -> 사용법 :  import 패키지명.모듈명
## ====================================================
## urllib 표준 패키지 
## -> 웹 url주소를 가지고 다양한 기능의 함수, 클래스 제공 모듈들
## -> 요청 관련 모듈    urllib.request 
## -> url 분석 모듈     urllib.parse
## -> url 에러 모듈     urllib.error
## -> 크롤링 분석 모듈   urllib.robotparser
## -----------------------------------------------------
## 모듈/패키지 로딩
import urllib.request as req            ## urllib.request 모듈 모두 가져오기
from urllib.request import urlopen      ## urlopen 함수만 가져오기

## ---------------------------------
## [예시] URL에 해당하는 데이터를 저장 - 1
## ---------------------------------
IMG_URL = 'https://mml.pstatic.net/www/mobile/edit/20260415_1095/upload_1776219728004Dd0i4.gif'

## 모듈 내의 변수, 함수, 클래스 사용
## => 모듈명.변수명, 모듈명.함수명(),  모듈명.클래스명
ret1, ret2 = req.urlretrieve(IMG_URL, "../DAY09/naver.jpg")

print(f'생성 파일 경로 ret1 => {ret1}')
print(f'웹의 응답 결과 ret2 => {ret2}')

## ---------------------------------
## [예시] URL에 해당하는 데이터를 저장 - 2
## ---------------------------------
retObj = urlopen(IMG_URL) 
print(f'웹의 응답 결과 retObj => {retObj}')
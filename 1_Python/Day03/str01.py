## ========================================================
## 기본+ 컨테이너 자료형- [3] str 타입
##
## * 다른 프로그래밍 언어=> 문자 1개, 문자 여러 개=> 타입 분리 (char(문자 1개), string(문자 여러 개))
## * Python=> 문자 1개, 문자 여러 개=> str 타입으로 통합
## * 형식
##    -> '문자', '문자'
##    -> "문자 여러 개", "문자 여러 개"
## ========================================================

'''
여러 줄 주석
* 다른 프로그래밍 언어=> 문자 1개, 문자 여러 개=> 타입 분리 (char(문자 1개), string(문자 여러 개))
* Python=> 문자 1개, 문자 여러 개=> str 타입으로 통합
'''

"""문자열 여러 줄 주석"""

## 여러 줄 문자열 저장==> 변수에 할당하기

msg= ''' 오늘은 좋은 날
         내일도 좋은 날
         
         계속 좋은 날'''

print(msg)



print("나는" + "21"+ "살입니다.") # 나는21살입니다. => 문자열 연결 연산자 + 사용

## =========================================
## 이스케이프 문자와 raw string
## => 문자열 안에서 특수한 의미를 가지는 문자


##   '\n'=> 줄바꿈
##   '\t'=> 탭
##   '\\'=> 역슬래시
##   '\''=> 작은 따옴표
##   '\"'=> 큰 따옴표
##   '\a'=> 벨 소리
##   '\b'=> 백스페이스
##   '\f'=> 폼 피드
##   '\Uxxxx'=> 유니코드 문자 (xxxx는 16진수 코드)
## => raw string: r"문자열" => 이스케이프 문자를 무시하고 그대로 출력
## r'문자열' 또는 R"문자열" 또는 R'문자열' 모두 가능

## =========================================

data1= "Good\nluck\t!!"
data2= r"Good\nluck\t!!"

print(data1) # Good
print(data2) # Good\nluck\t!!



## [2] 활용 및 적용=> 경로(path) 관련
data_path= r"C:\Users\KDT30\msg.txt"    # 앞에 r안 써주면 경로 안에 이스케이프문 \U 때문에 에러남

print("txt 파일 경로: ", data_path)

## ========================================================
## 기본+ 컨테이너 자료형- [3] str 타입
##
## * 산술 연산자
##  *: str* int만 가능===> str 을 int 횟수만큼 반복
##  +: str+ str만 가능===> str 연결
##   
## ========================================================


msg="good luck!!"
year=str('2026!!')


## =========================================
## * 멤버 연산자
## 데이터 in str => 존재하면 True, 존재하지 않으면 False 반환
## 데이터 not in str => 존재하지 않으면 True, 존재하면 False 반환
## =========================================

msg= "good luck!!"

print(f" 'h' in msg: {'h' in msg}") # 'h' in msg: False
print(f" 'h' not in msg: {'h' not in msg}") # 'h' not in msg: True


## =========================================
## 기본+ 컨테이너 자료형- [3] str 타입
##
## * str 전용 함수 즉, 메서드=> 다른 타입에 비해 아주 많음
## * 많이 알수록 문자열 처리에 유용하게 활용할 수 있음
## =========================================

msg= "good luck!!"

## ----------------------------------------------
## [1] 원소/ 요소의 인덱스 반환-> find(문자/문자열) => 존재하면 인덱스 반환, 존재하지 않으면 -1 반환 !!!!!!!!!!!!!!!!!!!!!!! 인덱스랑 다르게 에러 안 내고 -1 반환
## * 대/소문자 일치해야 함
## -----------------------------------------------
## => l의 인덱스 출력
print(msg.find('l'))
print(msg.find('L')) # 5 => l이 msg 문자열의 5번 인덱스에 위치함
## => ck의 인덱스 출력
print(msg.find('ck'))






## =========================================
## 기본+ 컨테이너 자료형- [3] str 타입
##
## * str 전용 함수 즉, 메서드=> 다른 타입에 비해 아주 많음
## * 많이 알수록 문자열 처리에 유용하게 활용할 수 있음
## =========================================


print(msg.lower()) # 'good luck!!' => 모든 문자를 소문자로 변환한 새로운 문자열 반환--> 원래 문자열은 변하지 않음
print(msg.upper()) # 'GOOD LUCK!!' => 모든 문자를 대문자로 변환한 새로운 문자열 반환
print(msg.title()) # 'Good Luck!!' => 각 단어의 첫 글자를 대문자로 변환한 새로운 문자열 반환
print(msg.swapcase()) # 'GOOD LUCK!!' => 대문자는 소문자로, 소문자는 대문자로 변환한 새로운 문자열 반환

## ------------------------------------------
## [3] 원소/ 요소 검사관련 메서드: isxxxxxx()
## => 결과: True/ False
## * 숫자만으로 된 str인지: isdecimal() 0~9
## * 숫자, 알파벳으로만 된 str인지: isalnum()

ret= msg.isalpha()
print(ret) # False => 공백과 느낌표가 있어서 False




msg="Happy"
phone= "01011112222"
userid= "k1234"

print(f"{msg}.isalpha(): {msg.isalpha()}")
print(f"{phone}.isalpha(): {phone.isalpha()}")
print(f"{userid}.isalpha(): {userid.isalpha()}")


print(f"\n{msg}.isdecimal(): {msg.isdecimal()}")
print(f"{phone}.isdecimal(): {phone.isdecimal()}")
print(f"{userid}.isdecimal(): {userid.isdecimal()}")


print(f"\n{msg}.isalnum(): {msg.isalnum()}")
print(f"{phone}.isalnum(): {phone.isalnum()}")
print(f"{userid}.isalnum(): {userid.isalnum()}")





## ------------------------------------------
## [3] 원소/ 요소 검사관련 메서드: isxxxxxx()
## => 결과: True/ False
## * 모든 원소가 대문자: isupper()
## * 모든 원소가 소문자: islower()
## * 공백인지: isspace()
## * 첫글자만 대문자, 나머지 소문자: istitle()
## ------------------------------------------

msg1="Good"
msg2="HAPPY"
msg3="   "


print(f"{msg1}.isupper(): {msg1.isupper()}")
print(f"{msg2}.isupper(): {msg2.isupper()}")
print(f"{msg3}.isupper(): {msg3.isupper()}")

print(f"\n{msg1}.isupper(): {msg1.islower()}")
print(f"{msg2}.islower(): {msg2.islower()}")
print(f"{msg3}.islower(): {msg3.islower()}")

print(f"\n{msg1}.isspace(): {msg1.isspace()}")
print(f"{msg2}.isspace(): {msg2.isspace()}")
print(f"{msg3}.isspace(): {msg3.isspace()}")

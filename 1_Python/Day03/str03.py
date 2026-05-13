## ========================================================
## 기본+컨테이너자료형 - [3] str 타입
##
## * str 전용 함수 즉, 메서드 => 다른 타입에 비해 아~주 많음!!
## * str 메서드를 많이 알 수록 편해짐!!
## ========================================================
## --------------------------
## str 생성
## --------------------------
msg  = "Good Luck"
#       012345678
## --------------------------
## [1] 원소/요소의 인덱스 반환 => find(문자/문자열)
##         * 대소문자 일치해야 함!
##         * 존재하지않으면 -1 반환
##         * 존재하면      0이상 인덱스 반환 
## --------------------------
## => L의 인덱스 출력
idx=msg.find("L")
print(f"L의 인덱스 : {idx}번")

## =>  Lu의 인덱스 출력
idx=msg.find(" Lu")
print(f" Lu의 인덱스 : {idx}번")


## =>  lu의 인덱스 출력
idx=msg.find(" lu")
print(f" lu의 인덱스 : {idx}번")


## --------------------------
## [2] 원소/요소의 대소문자 변환 => 반환
##         * lower()  : 모두 소문자
##         * uppper() : 모두 대문자
##         * swapcase() : 소->대, 대->소문자
## --------------------------
new_msg = msg.lower()
print(f"msg : {msg},  new_msg : {new_msg}")

new_msg = msg.upper()
print(f"msg : {msg},  new_msg : {new_msg}")

new_msg = msg.swapcase()
print(f"msg : {msg},  new_msg : {new_msg}")


## --------------------------
## [3] 원소/요소 검사관련 메서드 : isXXXX()
##         * 결과 : True/False
##         * 알파벳만으로 된 str인지   : isalpha()
##         * 숫자만으로 된  str인지    : isdecimal() 0~9
##         * 숫자, 알파벳만된 str인지  : isalnum()
## --------------------------
msg    = "Happy"
phone  = "01011112222"
userid = "k1234"

print(f"{msg}.isalpha()    : {msg.isalpha()}")
print(f"{phone}.isalpha()  : {phone.isalpha()}")
print(f"{userid}.isalpha() : {userid.isalpha()}")

print(f"\n{msg}.isdecimal()  : {msg.isdecimal()}")
print(f"{phone}.isdecimal()  : {phone.isdecimal()}")
print(f"{userid}.isdecimal() : {userid.isdecimal()}")

print(f"\n{msg}.isalnum()  : {msg.isalnum()}")
print(f"{phone}.isalnum()  : {phone.isalnum()}")
print(f"{userid}.isalnum() : {userid.isalnum()}")


## --------------------------
## [3] 원소/요소 검사관련 메서드 : isXXXX()
##         * 결과 : True/False
##         * 모든 원소가 대문자 여부       : isupper()
##         * 모든 원소가 소문자 여부       : islower() 
##         * 공백인지                    : isspace()
##         * 첫글자만 대문자, 나머지 소문자 : istitle()
## --------------------------
msg1 = "Good"
msg2 = "HAPPY" 
msg3 = "    "

print(f"{msg1}.isupper() : {msg1.isupper()}")
print(f"{msg2}.isupper() : {msg2.isupper()}")
print(f"{msg3}.isupper() : {msg3.isupper()}")

print(f"\n{msg1}.islower() : {msg1.islower()}")
print(f"{msg2}.islower()   : {msg2.islower()}")
print(f"{msg3}.islower()   : {msg3.islower()}")

print(f"\n{msg1}.isspace() : {msg1.isspace()}")
print(f"{msg2}.isspace()   : {msg2.isspace()}")
print(f"{msg3}.isspace()   : {msg3.isspace()}")

print(f"\n{msg1}.istitle() : {msg1.istitle()}")
print(f"{msg2}.istitle()   : {msg2.istitle()}")
print(f"{msg3}.istitle()   : {msg3.istitle()}")
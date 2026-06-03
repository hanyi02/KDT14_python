## =============================================================
## 컨테이너 자료형 - [3] str타입
##
## - str 전용 함수 즉, 메서드 이해
## =============================================================
## -------------------------------------------------------------
## [10] 특정 문자열/문자로 시작하는지 또는 끝나는지 검사하는 메서드
##  -> startswith(문자열/문자) : 시작 검사 => True/False 반환
##  -> endswith(문자열/문자)   : 끝 검사   => True/False 반환
## -------------------------------------------------------------
filename1 = "data.csv"
filename2 = "image.jpg"
filename3 = "image.png"

## Unpacking 언팩킹 : 원소 개수만큼 변수명을 선언해서 저장하는 것 
##                   컨데이터 자료형에서 1개의 변수명으로 관리하던 데이터를
##                   여러개의 변수명으로 나누어서 저장 
filename1, filename2, filename3 = "data.csv", "image.jpg", "image.png"

## 특정 문자열/문자로 시작하는지 검사 진행 : startswith()
ret = filename1.startswith("i")
print(f"{filename1} => {ret}")

ret = filename1.startswith("ima")
print(f"{filename1} => {ret}")

ret = filename1.startswith("d")
print(f"{filename1} => {ret}")

## 특정 문자열/문자로 끝나는지 검사 진행 : endswith()
ret = filename1.endswith(".csv")
print(f"{filename1} : .csv? => {ret}")

ret = filename2.endswith(".csv")
print(f"{filename2} : .csv? => {ret}")

ret = filename2.endswith((".csv", ".jpg", ".png", ".gif"))
print(f"{filename2} : .csv or .jpg ? => {ret}")
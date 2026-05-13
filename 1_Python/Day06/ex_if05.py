## ==========================================================
## 제어문(조건문/ 반복문) 연산자
## ----------------------------------------------------------
## -> 조건에 따라 특정 코드 실행 여부 결정 문법: 조건문
## -> 조건에 따라 특정 코드 반복 실행 여부 결정 문법: 반복문
## ==========================================================
## [예시] 파일 확장자에 따라서 파일을 분류하고자 합니다.
##          - 이미지 파일: jpg, png, jpeg, bmp
##          - 텍스트 파일: hwp, txt, word
##          - 기타 파일: 이미지, 텍스트 확장자 제외한 나머지
filename='cat.jpg'


## (1) 파일이름에서 확장자만 찾기
ext= filename.split('.')[1] # 패킹으로 인덱스 접근

_, ext= filename.split('.') # 언패킹으로 접근

print(f"이름: {_}, 확장자: {ext}")

## (2) 확장자에 따른 파일 종류 출력
if ext=='jpg' or ext=='jpeg' or ext=='png' or ext=='bmp':
    print(f"{filename}: 이미지 파일")

if ext=='hwp' or ext=='txt' or ext=='word':
    print(f"{filename}: 텍스트 파일")


if ext!='jpg' and ext!='jpeg' and ext!='png' and ext!='bmp' and ext!='hwp' and ext!='txt' and ext!='word':
    print(f"{filename}: 기타 파일")


#  너무 복잡하니까 멤버 연산자 쓰면 간단해짐 (in, not in)
if ext in ['jpg', 'png', 'jpeg', 'bmp']:
    print(f"{filename}: 이미지 파일")

if ext in ['hwp', 'txt', 'word']:
    print(f"{filename}: 텍스트 파일")

if ext not in ['jpg', 'png', 'jpeg', 'bmp', 'hwp', 'txt', 'word']:
    print(f"{filename}: 기타 파일")



## =============================================================
## 다중 조건문: 조건이 2개 이상인 경우

if ext in ['jpg', 'png', 'jpeg', 'bmp']:
    print(f"{filename}: 이미지 파일")
elif ext in ['hwp', 'txt', 'word']:
    print(f"{filename}: 텍스트 파일")
else:
    print(f"{filename}: 기타 파일")
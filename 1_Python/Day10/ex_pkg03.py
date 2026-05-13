## ====================================================
##              파이썬 표준 모듈 및 패키지 
## ====================================================
## OS 모듈 :  파일, 폴더, 경로 모듈 
## ====================================================
## ----------------------------------------------------
## 모듈 로딩
## ----------------------------------------------------
import os

## ----------------------------------------------------
## 모듈 사용
## ----------------------------------------------------
## os.mkdir()
## => 1개 폴더 생성
## => 존재하면 Error 발생
#os.mkdir("test")


## os.makedirs()
## => 여러 단계 즉, 모든 경로 폴더 생성
## => exist_ok=True 
##    이미 존재하면 생성하지 않음 => Error안남!
os.makedirs("a/b/c", exist_ok=True)


## os.listdir()
## => 폴더 내의 목록이름 리스트 반환
items = os.listdir("../DAY10")
print(f"폴더 내 항목 : {len(items)}개")
print(items)


## os.join()
## => 경로 만들기
i_path = os.path.join("../DAY10", items[0])
print(i_path)

i_path = os.path.join("../DAY10", items[0], "image.jpg")
print(i_path)


## [실습] DAY10폴더 안에 파일만 화면에 출력하세요.
##       단, 경로정보까지 출력해주세요. (예: ../DAY10/test.py)
items = os.listdir("../DAY10")
for item in items:
    item_path = os.path.join("../DAY10", item)
    
    if os.path.isfile(item_path):
        print(item, item_path)
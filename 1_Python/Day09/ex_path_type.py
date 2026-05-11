## ---------------------------------------------------------------------
## 경로
## - 절대경로 : Window 운영체제에서 드라이브(C, D...) 기준 경로/ 파일 위치 설정
##              linux, macOS 운영체제에서 루트(/) 기준 경로/ 파일 위치 설정 
##              [예] C:\Users\kwon\Desktop\PYTORCH_IMAGE\data\flower.jpg
## - 상대경로 : 현재 파일이 있는 위치를 기준으로 경로/ 파일위치 설정
##              특별한 의미를 가진 ., .. 기호 사용
##              [예] ../data/flower.jpg
## ---------------------------------------------------------------------
## 파일의 경로
## (1) tmp_in.txt는 현재 파이썬 코드 파일과 동일한 폴더에 존재
## (2) tmp_out.txt: 1_Python 폴더 안에 존재
##                  현재 파이썬 코드 파일과 다른 위치에 있음
## ------------------------------------------------------------------
## 파일 및 경로 관련 함수, 클래스 존재하는 파일: 모듈
## 모듈을 코드에 포함하기 문법=> improt 모듈파일명


import os

## 전역변수 파일경로 저장
file_path_abs1= r"C:\KDT14\1_Python\Day09\ex_path_type.py"

## 코드와 같은 위치에 존재, 즉 현재위치를 의미=> 기호 ./
file_path_re1= r"./tmp_in.txt"



file_path_abs2= r"C:\KDT14\1_Python\Day09\tmp_in.txt"
# 현재 코드 파일보다 한 단계 상위 폴더에 존재, 즉 현재위치보다 한 단계 위를 의미=> 기호 ../
file_path_re2= '../tmp_in.txt'

## ==============================================================
##                         파일 존재 여부
## ==============================================================

## os 모듈 사용
os.path.exists(file_path_abs1) # True
os.path.exists(file_path_re1) # True

os.path.exists(file_path_abs2) # True
os.path.exists(file_path_re2) # False

print(f"절대경로 파일 존재 여부: {os.path.exists(file_path_abs1)}")
print(f"상대경로 파일 존재 여부: {os.path.exists(file_path_re1)}")

print(f"절대경로 파일 존재 여부: {os.path.exists(file_path_abs2)}")
print(f"상대경로 파일 존재 여부: {os.path.exists(file_path_re2)}")



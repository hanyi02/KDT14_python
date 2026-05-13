## =======================================================
## 파일 입출력 - 파일 읽기 & 파일 위치 이동
## =======================================================
## ---------------------------------
## 전역 변수
## ---------------------------------
FILE_PATH = 'new_data.txt'

## ---------------------------------
## 파일 읽기
## ---------------------------------
## (1) 열기 - open()
f = open(FILE_PATH, mode='rt', encoding='utf8')

## 파일의 속성들 확인
print(f'closed : {f.closed}')
print(f'name   : {f.name}')
print(f'mode   : {f.mode}')

## (2) 읽기 
## => 처음부터 끝까지 2번 읽고 출력
all_data = f.read()
print(f'1번째 : {all_data}\n')

## => 현재 파일 위치  - tell()
cur_pos = f.tell()
print(f'cur_pos : {cur_pos}')

## 파일 위치를 시작 위치로 이동 - seek()
## 텍스트 일때는 0에서만 동작 
pos=f.seek(0)
print(f'pos : {pos}')

all_data = f.read()
print(f'2번째 : {all_data}\n')


## (3) 닫기 
f.close()
print(f'closed : {f.closed}')
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
print(f'cur_pos : {f.tell()}')

## (2) 읽기 
# while True:
#     # 문자 5개씩 읽고 출력
#     ndata = f.read(5)     
#     print(f'cur_pos : {f.tell()}, {ndata}')
#     if not ndata: break

CNT = 3
while CNT:
    # 문자 5개씩 읽고 출력
    ndata = f.read(5)
    print(f'cur_pos : {f.tell()}, {ndata}')

    # 파일의 끝(EOF)일 경우, 파일의 처음으로 위치 이동
    if not ndata: 
        f.seek(0)
        CNT -= 1
        print(f'[{CNT}]cur_pos : {f.tell()}')

## (3) 닫기 
if not f.closed: f.close()
print(f'closed : {f.closed}')
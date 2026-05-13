# ================================================
# 문제 2. 회원 추가 기능 만들기
# ------------------------------------------------
# 구현 : 회원 관리 프로그램의 회원 등록 기능.
#
# 요구사항
# -> 사용자에게 연락처, 이름, 지역, 직업, 취미 입력 받기.
# -> 입력받은 정보를 users.txt 파일에 추가 저장.
# -> 이미 저장된 회원 정보는 유지되어야 함.
# -> 저장 후 "회원 등록 완료" 출력.
# -> 이미 존재하는 회원이면 "이미 등록되어 있습니다" 출력.
#
# 저장 형식
# -> 연락처      15     이름 10   지역 10    직업  10    취미  10
# -> 010-2222-1111   태권V    대구     운동선수    태권도
# ================================================
## ----------------------------------------------- 
## 모듈 로딩
## ----------------------------------------------- 
import os 

## ----------------------------------------------- 
## 전역변수
## ----------------------------------------------- 
MEMBER_PATH = '../Member'
USER_FILE   = f'{MEMBER_PATH}/users.txt'

# ------------------------------------------------
# 함수이름 : create_dir_file
# 함수기능 : 폴더 또는 파일 생성
# 매개변수 : path    생성할 폴더 또는 파일 경로
#           isfile  생성하는 것이 파일인지 폴더인지
# 함수결과 : 생성 여부 True/False 반환
# ------------------------------------------------
def create_dir_file(path, isfile=False):
    # 존재 여부 체크
    if not os.path.exists(path):
        # 폴더 생성
        if not isfile:
            os.mkdir(path)
        else : 
            # 파일 생성
            with open(USER_FILE, mode='x', encoding='utf8') as F: 
                F.write(f"{'연락처':<15}{'이름':<10}{'지역':<10}{'직업':10}{'취미':<10}\n")
       
        return os.path.exists(path)
    else: 
        return True

# ------------------------------------------------
# 함수이름 : join_user
# 함수기능 : 회원 등록 / 파일 저장 
# 매개변수 : phone, name, loc, job, hobby
#           phone - 중복되지 않는 데이터로써 식별자(id)
#                   전화번호 형식, 숫자 구성 체크
# 함수결과 : 생성 여부 True/False 반환
# ------------------------------------------------
def join_user(phone, name, loc, job, hobby):

    # 연락처 데이터 형식 및 구성 검사
    if phone.replace("-", "").isdecimal():

        # 파일 데이터 추출
        with open(USER_FILE, mode='r', encoding='utf8') as rF:
            allDatas = rF.read()

        # 중복 여부 체크
        if phone in allDatas:
            print(f"{phone} 이미 등록된 회원입니다.")
        else:
            # 새로운 회원으로 추가 
            with open(USER_FILE, mode='a', encoding='utf8') as F:
                wCnt=F.write(f"{phone:<15}{name:<10}{loc:<10}{job:10}{hobby:<10}\n")
                print(f"{wCnt}개 데이터 저장")

    else:
        print("유효한 데이터가 아닙니다.")



## -----------------------------------------
## 기능 테스트
## -----------------------------------------
## 폴더 및 파일 생성
if create_dir_file(MEMBER_PATH) and create_dir_file(USER_FILE, True):
    print("폴더 및 파일 준비 완료")

    ## 등록 요청 메시지
    indata = input("회원등록 연락처, 이름, 지역, 직업, 취미 입력:").strip().split(",")

    ## 등록 정보 체크
    if len(indata)==5:
        join_user(*indata)             #<= 언패킹
        #join_user(indata[0], indata[1], indata[2], indata[3], indata[4]) 
    else:
        print("필수 회원 정보 연락처, 이름, 지역, 직업, 취미가\n모두 입력되었는지 확인바랍니다.")

else:
    print("폴더 및 파일 문제 체크 필요")
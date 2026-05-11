## =================================================
##      메모 관리 프로그램  - MEMO APP
## =================================================
## -> 주요기능 : 메모 저장, 삭제, 보기 
## =================================================
## -------------------------------------------------
## 모듈 로딩
## -------------------------------------------------
import os 


## -------------------------------------------------
## 전역변수
## -------------------------------------------------
MEMO_DIR = '../Memo'
M_VIEW, M_MEMO, M_SAVE, M_DELETE, M_EXIT = list('12345')


## -------------------------------------------------
## 사용자정의 함수 
## -------------------------------------------------
## 함수기능 : 메뉴 출력
## 함수이름 : print_menu
## 매개변수 : 없음
## 함수결과 : 없음
## -------------------------------------------------
def print_menu():
    print("="*30)
    print(f"{'MENU':^30}")
    print("="*30)
    print("1.전제보기")
    print("2.선택보기")
    print("3.메모저장")
    print("4.메모삭제")
    print("5.종료")
    print("="*30)



def print_stat(msg):
    print("="*30)
    print(f"{msg:^30}")
    print("="*30)

## -------------------------------------------------
## 함수기능 : 메모 목록 출력
## 함수이름 : print_meno
## 매개변수 : 없음
## 함수결과 : 없음
## -------------------------------------------------
def print_memo():
    mlist = os.listdir(MEMO_DIR)
    print("="*30)
    print(f"{'-메모목록-':^30}")
    print("="*30)
    for m in mlist:
        print(m)
    print("="*30)


def view_memo():
    ## 메모 선택
    item = input("메모 날짜입력(예:2025_02_11):")
    item = f'memo_{item}.txt'
    ## 선택된 메모 내용 화면에 출력
    mitems = os.listdir(MEMO_DIR)
    if item in mitems:
        filepath=f'{MEMO_DIR}/{item}'
        with open(filepath, mode='r', encoding='utf8') as F:
            print("="*30)
            print(F.read())
            print("="*30)
    else:
        print(f'{item} : 존재하지 않는 메모입니다. ')


def delete_memo():
    ## 메모 선택
    item = input("메모 날짜입력(예:2025_02_11):")
    item = f'memo_{item}.txt'
    ## 선택된 메모 내용 화면에 출력
    mitems = os.listdir(MEMO_DIR)
    if item in mitems:
        filepath=f'{MEMO_DIR}/{item}'
        os.remove(filepath)
    else:
        print(f'{item} : 존재하지 않는 메모입니다. ')

## -------------------------------------------------
## 함수기능 : 메모 저장 
## 함수이름 : save_meno
## 매개변수 : 없음
## 함수결과 : 없음
## -------------------------------------------------
def save_meno():
    pass 


## =================================================
## 프로그램 구동
## =================================================
if __name__ == '__main__':
    print_stat('MEMO APP START')

    while True:
        print_menu()
        choice = input("메뉴 선택(1~4):").strip()

        if choice not in [M_VIEW, M_MEMO, M_SAVE, M_DELETE, M_EXIT]:
            print(f"{choice}는 유효하지 않은 메뉴입니다.")

        elif choice == M_VIEW:
            print_memo()
        elif choice == M_MEMO:
            view_memo()
        elif choice == M_SAVE:
            pass
        elif choice == M_DELETE:
            pass
        else:
            print("사용자 요청으로 종료합니다.")
            break

    print_stat('MEMO APP END')
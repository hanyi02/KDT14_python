import os

# 아이콘 함수
def get_icon(path, name):
    full_path = os.path.join(path, name)

    if os.path.isdir(full_path):
        return "[폴더]"
    elif os.path.isfile(full_path):
        if name.endswith(".py"):
            return "[파이썬]"
        else:
            return "[파일]"
    return "[기타]"


# 목록 출력 함수
def show_list(path):
    print("\n" + "=" * 50)
    print("현재 경로 :", path)
    print("=" * 50)

    try:
        items = os.listdir(path)
        items.sort()
    except Exception as e:
        print("폴더를 열 수 없습니다.")
        print("오류:", e)
        return []

    if not items:
        print("비어 있는 폴더입니다.")
        return []

    for idx, name in enumerate(items, 1):
        icon = get_icon(path, name)
        print(f"{idx}. {icon} {name}")

    return items


# 경로 이동 함수
def move_path(current_path, items, choice):
    if choice == "b":
        parent_path = os.path.dirname(current_path)

        # 더 이상 올라갈 수 없는 경우
        if parent_path == current_path:
            print("이미 최상위 폴더입니다.")
            return current_path

        return parent_path

    elif choice == "q":
        return None

    elif choice.isdigit():
        num = int(choice)

        if 1 <= num <= len(items):
            selected_name = items[num - 1]
            selected_path = os.path.join(current_path, selected_name)

            if os.path.isdir(selected_path):
                return selected_path
            else:
                print("파일은 열 수 없고, 폴더만 이동할 수 있습니다.")
                return current_path
        else:
            print("없는 번호입니다.")
            return current_path

    else:
        print("잘못된 입력입니다.")
        return current_path


# 시작 경로 입력 함수
def input_start_path():
    while True:
        path = input("시작 경로를 입력하세요: ").strip()

        if os.path.exists(path) and os.path.isdir(path):
            return path
        else:
            print("유효한 폴더 경로가 아닙니다. 다시 입력하세요.")


# 메인 함수
def main():
    print("=" * 50)
    print("터미널 폴더 탐색기")
    print("번호 입력 : 해당 폴더로 이동")
    print("b : 상위 폴더로 이동")
    print("q : 종료")
    print("=" * 50)

    current_path = input_start_path()

    while True:
        items = show_list(current_path)

        print("\n[입력 안내]")
        print("번호 : 폴더 들어가기")
        print("b : 상위 폴더")
        print("q : 종료")

        choice = input("입력 >>> ").strip().lower()

        next_path = move_path(current_path, items, choice)

        if next_path is None:
            print("프로그램을 종료합니다.")
            break

        current_path = next_path


# 프로그램 실행
if __name__ == "__main__":
    main()
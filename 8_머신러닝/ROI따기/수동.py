import cv2
import numpy as np
from pathlib import Path


# =====================================================
# 설정
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

# 검수할 ROI 폴더
ROI_ROOT = BASE_DIR / "Images_roi"

# 이미지 확장자
EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

# 화면에 표시할 이미지의 최대 크기
# 창이 여전히 크면 이 값을 더 줄이면 됨
MAX_DISPLAY_WIDTH = 900
MAX_DISPLAY_HEIGHT = 550

# 이미지 아래 안내창 높이
INFO_HEIGHT = 75

WINDOW_NAME = "ROI MANUAL REVIEW"


# =====================================================
# 한글 경로 대응 이미지 읽기
# =====================================================

def imread_unicode(path):
    try:
        data = np.fromfile(str(path), dtype=np.uint8)

        if data.size == 0:
            return None

        return cv2.imdecode(data, cv2.IMREAD_COLOR)

    except Exception:
        return None


# =====================================================
# 한글 경로 대응 이미지 저장
# =====================================================

def imwrite_unicode(path, img):
    try:
        extension = Path(path).suffix.lower()

        success, encoded_img = cv2.imencode(extension, img)

        if not success:
            return False

        encoded_img.tofile(str(path))
        return True

    except Exception:
        return False


# =====================================================
# ROI 폴더 안의 모든 이미지 가져오기
# 하위 폴더까지 전부 검색
# =====================================================

def get_all_image_paths(folder):
    image_paths = []

    for path in folder.rglob("*"):
        if path.is_file() and path.suffix.lower() in EXTS:
            image_paths.append(path)

    return sorted(image_paths)


# =====================================================
# 화면 크기에 맞게 이미지 축소
# =====================================================

def resize_for_display(img):
    height, width = img.shape[:2]

    width_scale = MAX_DISPLAY_WIDTH / width
    height_scale = MAX_DISPLAY_HEIGHT / height

    # 확대하지 않고 축소만 함
    scale = min(width_scale, height_scale, 1.0)

    new_width = max(1, int(width * scale))
    new_height = max(1, int(height * scale))

    if scale == 1.0:
        return img.copy(), scale

    resized = cv2.resize(
        img,
        (new_width, new_height),
        interpolation=cv2.INTER_AREA
    )

    return resized, scale


# =====================================================
# 현재 이미지가 들어 있는 클래스 폴더명 구하기
# =====================================================

def get_class_name(image_path):
    try:
        relative_path = image_path.relative_to(ROI_ROOT)

        # Images_roi/banana/파일.jpg 형태
        if len(relative_path.parts) >= 2:
            return relative_path.parts[0]

        # Images_roi 바로 아래에 이미지가 있는 경우
        return ROI_ROOT.name

    except ValueError:
        return image_path.parent.name


# =====================================================
# 이미지 한 장 검수
# =====================================================

def review_one_image(image_path, current_num, total_num):
    img = imread_unicode(image_path)

    if img is None:
        print(
            f"[{current_num}/{total_num}] "
            f"이미지 읽기 실패: {image_path}"
        )
        return "skip"

    display_img, display_scale = resize_for_display(img)

    display_height, display_width = display_img.shape[:2]

    class_name = get_class_name(image_path)

    roi_state = {
        "drawing": False,
        "start": None,
        "end": None,
        "roi": None
    }

    # =================================================
    # 마우스 이벤트
    # =================================================

    def mouse_callback(event, x, y, flags, param):

        # 이미지 아래 안내 영역에서는 ROI 선택 금지
        if y >= display_height:
            return

        # 이미지 범위를 벗어나지 않도록 제한
        x = min(max(x, 0), display_width - 1)
        y = min(max(y, 0), display_height - 1)

        # 마우스 왼쪽 버튼 누름
        if event == cv2.EVENT_LBUTTONDOWN:
            roi_state["drawing"] = True
            roi_state["start"] = (x, y)
            roi_state["end"] = (x, y)
            roi_state["roi"] = None

        # 마우스 드래그 중
        elif event == cv2.EVENT_MOUSEMOVE:
            if roi_state["drawing"]:
                roi_state["end"] = (x, y)

        # 마우스 왼쪽 버튼 놓음
        elif event == cv2.EVENT_LBUTTONUP:
            if roi_state["start"] is None:
                return

            roi_state["drawing"] = False
            roi_state["end"] = (x, y)

            start_x, start_y = roi_state["start"]
            end_x, end_y = roi_state["end"]

            x1 = max(min(start_x, end_x), 0)
            y1 = max(min(start_y, end_y), 0)

            x2 = min(max(start_x, end_x), display_width)
            y2 = min(max(start_y, end_y), display_height)

            # 너무 작은 ROI는 무시
            if x2 - x1 > 5 and y2 - y1 > 5:
                roi_state["roi"] = (x1, y1, x2, y2)

    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback(WINDOW_NAME, mouse_callback)

    while True:
        # 이미지 + 아래 안내창 크기의 검은 캔버스
        canvas = np.zeros(
            (
                display_height + INFO_HEIGHT,
                display_width,
                3
            ),
            dtype=np.uint8
        )

        # 위쪽에 이미지 전체 표시
        canvas[
            0:display_height,
            0:display_width
        ] = display_img.copy()

        # ---------------------------------------------
        # 마우스로 드래그 중인 박스
        # ---------------------------------------------

        if (
            roi_state["drawing"]
            and roi_state["start"] is not None
            and roi_state["end"] is not None
        ):
            start_x, start_y = roi_state["start"]
            end_x, end_y = roi_state["end"]

            cv2.rectangle(
                canvas,
                (start_x, start_y),
                (end_x, end_y),
                (0, 255, 255),
                2
            )

        # ---------------------------------------------
        # 선택 완료된 ROI 박스
        # ---------------------------------------------

        if roi_state["roi"] is not None:
            x1, y1, x2, y2 = roi_state["roi"]

            cv2.rectangle(
                canvas,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                3
            )

        # ---------------------------------------------
        # 이미지 아래 별도 안내 영역
        # ---------------------------------------------

        cv2.rectangle(
            canvas,
            (0, display_height),
            (
                display_width,
                display_height + INFO_HEIGHT
            ),
            (0, 0, 0),
            -1
        )

        # 진행 상황
        cv2.putText(
            canvas,
            f"{class_name}  {current_num}/{total_num}",
            (12, display_height + 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (0, 255, 0),
            2
        )

        # 키 안내
        cv2.putText(
            canvas,
            "ENTER: PASS | Drag + SPACE: SAVE | R: RESET | ESC/Q: QUIT",
            (12, display_height + 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (0, 255, 255),
            1
        )

        cv2.imshow(WINDOW_NAME, canvas)

        # 창의 X 버튼을 눌렀을 때 종료
        if cv2.getWindowProperty(
            WINDOW_NAME,
            cv2.WND_PROP_VISIBLE
        ) < 1:
            return "quit"

        key = cv2.waitKey(20) & 0xFF

        # =============================================
        # Enter: 현재 이미지 그대로 통과
        # =============================================

        if key in (13, 10):
            print(
                f"[{current_num}/{total_num}] "
                f"통과: {image_path.name}"
            )

            return "pass"

        # =============================================
        # Space: 선택한 ROI로 현재 파일 덮어쓰기
        # =============================================

        elif key == 32:
            if roi_state["roi"] is None:
                print("마우스로 ROI 영역을 먼저 선택하세요.")
                continue

            x1, y1, x2, y2 = roi_state["roi"]

            # 화면 좌표를 실제 이미지 좌표로 복원
            original_x1 = int(x1 / display_scale)
            original_y1 = int(y1 / display_scale)

            original_x2 = int(x2 / display_scale)
            original_y2 = int(y2 / display_scale)

            original_height, original_width = img.shape[:2]

            original_x1 = max(original_x1, 0)
            original_y1 = max(original_y1, 0)

            original_x2 = min(original_x2, original_width)
            original_y2 = min(original_y2, original_height)

            roi = img[
                original_y1:original_y2,
                original_x1:original_x2
            ]

            if roi.size == 0:
                print("선택한 ROI 영역이 올바르지 않습니다.")

                roi_state["drawing"] = False
                roi_state["start"] = None
                roi_state["end"] = None
                roi_state["roi"] = None

                continue

            # 현재 보고 있는 ROI 파일에 덮어쓰기
            success = imwrite_unicode(image_path, roi)

            if success:
                print(
                    f"[{current_num}/{total_num}] "
                    f"ROI 수정 저장: {image_path.name}"
                )

                return "fixed"

            print(f"저장 실패: {image_path}")
            return "skip"

        # =============================================
        # R: 선택한 ROI 박스 초기화
        # =============================================

        elif key in (ord("r"), ord("R")):
            roi_state["drawing"] = False
            roi_state["start"] = None
            roi_state["end"] = None
            roi_state["roi"] = None

            print("ROI 선택 초기화")

        # =============================================
        # ESC 또는 Q: 전체 검수 종료
        # =============================================

        elif key == 27 or key in (ord("q"), ord("Q")):
            print("사용자가 검수를 종료했습니다.")
            return "quit"


# =====================================================
# Images_roi 안의 모든 이미지 전체 검수
# =====================================================

def review_all_roi_images():
    if not ROI_ROOT.exists():
        print(f"ROI 폴더가 없습니다: {ROI_ROOT}")
        return

    image_paths = get_all_image_paths(ROI_ROOT)

    total_num = len(image_paths)

    if total_num == 0:
        print(f"검수할 이미지가 없습니다: {ROI_ROOT}")
        return

    print()
    print("=" * 60)
    print("ROI 이미지 전체 검수 시작")
    print(f"검수 폴더: {ROI_ROOT}")
    print(f"전체 이미지: {total_num}장")
    print("=" * 60)

    pass_count = 0
    fixed_count = 0
    skip_count = 0

    for current_num, image_path in enumerate(
        image_paths,
        start=1
    ):
        result = review_one_image(
            image_path=image_path,
            current_num=current_num,
            total_num=total_num
        )

        if result == "quit":
            print()
            print("=" * 60)
            print("전체 검수 중단")
            print(f"통과: {pass_count}장")
            print(f"수정: {fixed_count}장")
            print(f"스킵: {skip_count}장")
            print("=" * 60)

            return

        elif result == "pass":
            pass_count += 1

        elif result == "fixed":
            fixed_count += 1

        else:
            skip_count += 1

    print()
    print("=" * 60)
    print("ROI 이미지 전체 검수 완료")
    print(f"전체: {total_num}장")
    print(f"통과: {pass_count}장")
    print(f"수정: {fixed_count}장")
    print(f"스킵: {skip_count}장")
    print("=" * 60)


# =====================================================
# 실행
# =====================================================

if __name__ == "__main__":
    try:
        review_all_roi_images()

    except KeyboardInterrupt:
        print()
        print("Ctrl + C로 검수를 중단했습니다.")

    finally:
        cv2.destroyAllWindows()
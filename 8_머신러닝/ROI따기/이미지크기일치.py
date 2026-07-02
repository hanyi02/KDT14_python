import cv2
import numpy as np
from pathlib import Path


# =====================================================
# 설정
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

# 원본 ROI 이미지 폴더
INPUT_ROOT = BASE_DIR / "Images_roi"

# 크기 통일 후 저장할 폴더
OUTPUT_ROOT = BASE_DIR / "Images_roi_224"

# 최종 이미지 크기
TARGET_WIDTH = 224
TARGET_HEIGHT = 224

# 패딩 색상: 흰색
PADDING_COLOR = (255, 255, 255)

# 지원 확장자
EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


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
        path = Path(path)

        # 저장 폴더 자동 생성
        path.parent.mkdir(parents=True, exist_ok=True)

        extension = path.suffix.lower()

        success, encoded_img = cv2.imencode(
            extension,
            img
        )

        if not success:
            return False

        encoded_img.tofile(str(path))

        return True

    except Exception:
        return False


# =====================================================
# 비율 유지 + 패딩으로 지정 크기 맞추기
# =====================================================

def resize_with_padding(
    img,
    target_width,
    target_height,
    padding_color=(255, 255, 255)
):
    original_height, original_width = img.shape[:2]

    if original_width <= 0 or original_height <= 0:
        return None

    # 가로, 세로 중 더 많이 줄여야 하는 쪽을 기준으로 배율 결정
    scale = min(
        target_width / original_width,
        target_height / original_height
    )

    new_width = max(
        1,
        int(round(original_width * scale))
    )

    new_height = max(
        1,
        int(round(original_height * scale))
    )

    # 축소할 때는 INTER_AREA가 적합
    # 확대할 때는 INTER_CUBIC 사용
    if scale < 1:
        interpolation = cv2.INTER_AREA
    else:
        interpolation = cv2.INTER_CUBIC

    resized = cv2.resize(
        img,
        (new_width, new_height),
        interpolation=interpolation
    )

    # 목표 크기의 흰색 배경 생성
    canvas = np.full(
        (
            target_height,
            target_width,
            3
        ),
        padding_color,
        dtype=np.uint8
    )

    # 중앙에 배치할 위치 계산
    start_x = (target_width - new_width) // 2
    start_y = (target_height - new_height) // 2

    end_x = start_x + new_width
    end_y = start_y + new_height

    # 리사이즈된 이미지를 중앙에 삽입
    canvas[
        start_y:end_y,
        start_x:end_x
    ] = resized

    return canvas


# =====================================================
# 폴더 내 이미지 전부 가져오기
# =====================================================

def get_all_image_paths(folder):
    image_paths = []

    for path in folder.rglob("*"):
        if path.is_file() and path.suffix.lower() in EXTS:
            image_paths.append(path)

    return sorted(image_paths)


# =====================================================
# 전체 이미지 크기 통일
# =====================================================

def resize_all_images():
    if not INPUT_ROOT.exists():
        print(f"입력 폴더가 없습니다: {INPUT_ROOT}")
        return

    image_paths = get_all_image_paths(INPUT_ROOT)

    total_count = len(image_paths)

    if total_count == 0:
        print(f"이미지가 없습니다: {INPUT_ROOT}")
        return

    print()
    print("=" * 60)
    print("이미지 크기 통일 시작")
    print(f"입력 폴더: {INPUT_ROOT}")
    print(f"출력 폴더: {OUTPUT_ROOT}")
    print(f"최종 크기: {TARGET_WIDTH} x {TARGET_HEIGHT}")
    print(f"전체 이미지: {total_count}장")
    print("=" * 60)

    success_count = 0
    fail_count = 0

    for index, input_path in enumerate(
        image_paths,
        start=1
    ):
        # Images_roi 기준 상대 경로
        relative_path = input_path.relative_to(INPUT_ROOT)

        # 기존 폴더 구조 유지
        output_path = OUTPUT_ROOT / relative_path

        img = imread_unicode(input_path)

        if img is None:
            print(
                f"[{index}/{total_count}] "
                f"읽기 실패: {relative_path}"
            )

            fail_count += 1
            continue

        result = resize_with_padding(
            img,
            TARGET_WIDTH,
            TARGET_HEIGHT,
            PADDING_COLOR
        )

        if result is None:
            print(
                f"[{index}/{total_count}] "
                f"변환 실패: {relative_path}"
            )

            fail_count += 1
            continue

        success = imwrite_unicode(
            output_path,
            result
        )

        if success:
            print(
                f"[{index}/{total_count}] "
                f"저장 완료: {relative_path}"
            )

            success_count += 1

        else:
            print(
                f"[{index}/{total_count}] "
                f"저장 실패: {relative_path}"
            )

            fail_count += 1

    print()
    print("=" * 60)
    print("이미지 크기 통일 완료")
    print(f"성공: {success_count}장")
    print(f"실패: {fail_count}장")
    print(f"저장 위치: {OUTPUT_ROOT}")
    print("=" * 60)


# =====================================================
# 실행
# =====================================================

if __name__ == "__main__":
    resize_all_images()
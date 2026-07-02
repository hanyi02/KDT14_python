import cv2
import numpy as np
from pathlib import Path

# =====================================================
# 경로 설정
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

RAW_ROOT = BASE_DIR / "Images"
SAVE_ROOT = BASE_DIR / "Images_roi"

CLASS_NAMES = ["apple", "banana", "pear"]
EXTS = [".jpg", ".jpeg", ".png", ".bmp", ".webp"]

SAVE_MODE = "crop"       # "crop" 또는 "png"
MANUAL_ON_FAIL = True    # 자동 실패하면 수동 ROI 실행
SKIP_EXISTING = True
MAX_DISPLAY_SIZE = 900


# =====================================================
# 한글 경로 대응 imread / imwrite
# =====================================================

def imread_unicode(path):
    data = np.fromfile(str(path), dtype=np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    return img


def imwrite_unicode(path, img):
    ext = Path(path).suffix
    success, encoded_img = cv2.imencode(ext, img)

    if success:
        encoded_img.tofile(str(path))

    return success


# =====================================================
# 자동 객체 추출 GrabCut
# =====================================================

def auto_extract_object(img, save_mode="crop"):
    h, w = img.shape[:2]

    if h < 50 or w < 50:
        return None

    # 이미지 가장자리 5%는 배경이라고 보고 시작
    margin_x = int(w * 0.05)
    margin_y = int(h * 0.05)

    rect = (
        margin_x,
        margin_y,
        w - 2 * margin_x,
        h - 2 * margin_y
    )

    mask = np.zeros((h, w), np.uint8)

    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    try:
        cv2.grabCut(
            img,
            mask,
            rect,
            bgd_model,
            fgd_model,
            5,
            cv2.GC_INIT_WITH_RECT
        )
    except:
        return None

    # 객체 영역만 255
    obj_mask = np.where(
        (mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD),
        255,
        0
    ).astype("uint8")

    # 노이즈 제거
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    obj_mask = cv2.morphologyEx(obj_mask, cv2.MORPH_OPEN, kernel, iterations=1)
    obj_mask = cv2.morphologyEx(obj_mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    contours, _ = cv2.findContours(
        obj_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) == 0:
        return None

    # 가장 큰 객체 선택
    c = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(c)

    # 객체가 너무 작으면 실패 처리
    if area < w * h * 0.01:
        return None

    x, y, bw, bh = cv2.boundingRect(c)

    # 여유 공간
    pad = 10
    x1 = max(x - pad, 0)
    y1 = max(y - pad, 0)
    x2 = min(x + bw + pad, w)
    y2 = min(y + bh + pad, h)

    crop_img = img[y1:y2, x1:x2]
    crop_mask = obj_mask[y1:y2, x1:x2]

    if save_mode == "crop":
        return crop_img

    elif save_mode == "png":
        b, g, r = cv2.split(crop_img)
        result = cv2.merge([b, g, r, crop_mask])
        return result

    return crop_img


# =====================================================
# 수동 ROI 선택
# =====================================================

def manual_select_roi(img, window_name="select roi"):
    h, w = img.shape[:2]

    scale = 1.0
    max_side = max(h, w)

    if max_side > MAX_DISPLAY_SIZE:
        scale = MAX_DISPLAY_SIZE / max_side
        display_w = int(w * scale)
        display_h = int(h * scale)
        display_img = cv2.resize(img, (display_w, display_h))
    else:
        display_img = img.copy()

    roi = cv2.selectROI(
        window_name,
        display_img,
        showCrosshair=True,
        fromCenter=False
    )

    cv2.destroyWindow(window_name)

    x, y, rw, rh = roi

    if rw == 0 or rh == 0:
        return None

    # 원본 이미지 좌표로 복구
    x = int(x / scale)
    y = int(y / scale)
    rw = int(rw / scale)
    rh = int(rh / scale)

    x1 = max(x, 0)
    y1 = max(y, 0)
    x2 = min(x + rw, w)
    y2 = min(y + rh, h)

    crop = img[y1:y2, x1:x2]

    return crop


# =====================================================
# 전체 처리
# =====================================================

def process_dataset():
    SAVE_ROOT.mkdir(parents=True, exist_ok=True)

    failed_list = []

    for class_name in CLASS_NAMES:
        raw_dir = RAW_ROOT / class_name
        save_dir = SAVE_ROOT / class_name
        save_dir.mkdir(parents=True, exist_ok=True)

        if not raw_dir.exists():
            print(f"[경고] 폴더 없음: {raw_dir}")
            continue

        img_paths = []

        for ext in EXTS:
            img_paths.extend(raw_dir.glob(f"*{ext}"))
            img_paths.extend(raw_dir.glob(f"*{ext.upper()}"))

        img_paths = sorted(list(set(img_paths)))

        print()
        print("=" * 60)
        print(f"[{class_name}] 총 {len(img_paths)}장 처리 시작")
        print("=" * 60)

        for idx, img_path in enumerate(img_paths, start=1):

            if SAVE_MODE == "png":
                save_path = save_dir / f"{img_path.stem}_object.png"
            else:
                save_path = save_dir / f"{img_path.stem}_crop.jpg"

            if SKIP_EXISTING and save_path.exists():
                print(f"[{idx}/{len(img_paths)}] 이미 존재해서 스킵: {save_path.name}")
                continue

            img = imread_unicode(img_path)

            if img is None:
                print(f"[{idx}/{len(img_paths)}] 읽기 실패: {img_path.name}")
                failed_list.append((class_name, str(img_path), "read_fail"))
                continue

            # 1차 자동 crop
            result = auto_extract_object(img, save_mode=SAVE_MODE)

            # 자동 실패 시 수동 ROI
            if result is None:
                print(f"[{idx}/{len(img_paths)}] 자동 실패 → 수동 ROI: {img_path.name}")

                if MANUAL_ON_FAIL:
                    result = manual_select_roi(
                        img,
                        window_name=f"{class_name} - {img_path.name}"
                    )

                if result is None:
                    print(f"[{idx}/{len(img_paths)}] 스킵: {img_path.name}")
                    failed_list.append((class_name, str(img_path), "manual_skip"))
                    continue

            ok = imwrite_unicode(save_path, result)

            if ok:
                print(f"[{idx}/{len(img_paths)}] 저장 완료: {save_path.name}")
            else:
                print(f"[{idx}/{len(img_paths)}] 저장 실패: {save_path.name}")
                failed_list.append((class_name, str(img_path), "save_fail"))

    # 실패 목록 저장
    failed_txt = SAVE_ROOT / "failed_list.txt"

    with open(failed_txt, "w", encoding="utf-8") as f:
        for class_name, path, reason in failed_list:
            f.write(f"{class_name}\t{reason}\t{path}\n")

    print()
    print("=" * 60)
    print("전체 처리 완료")
    print(f"결과 폴더: {SAVE_ROOT}")
    print(f"실패 목록: {failed_txt}")
    print("=" * 60)


# =====================================================
# 실행
# =====================================================

if __name__ == "__main__":
    process_dataset()
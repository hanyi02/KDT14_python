import cv2
import numpy as np

win_name = 'back_projection'

img = cv2.imread('./img2.png')

if img is None:
    print('이미지를 불러오지 못했습니다. 파일 경로를 확인하세요.')
    exit()

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
draw = img.copy()


def masking(bp, win_name):
    # 1. 부드럽게 필터링
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    bp = cv2.filter2D(bp, -1, disc)

    # 2. threshold로 후보 영역 이진화
    _, mask = cv2.threshold(bp, 50, 255, cv2.THRESH_BINARY)

    # 3. morphology 연산으로 노이즈 제거
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    # 작은 점 제거
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # 끊어진 부분 연결
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # 4. contour 검출
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = img.copy()

    # 5. 면적, 모양 조건으로 필터링
    min_area = 500

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area < min_area:
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        if h == 0:
            continue

        aspect_ratio = w / h

        # 너무 납작하거나 너무 긴 영역 제거
        if aspect_ratio < 0.2 or aspect_ratio > 5.0:
            continue

        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.drawContours(result, [cnt], -1, (0, 0, 255), 2)

    # 6. mask 적용 결과
    masked_result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow(win_name + '_backproj', bp)
    cv2.imshow(win_name + '_mask', mask)
    cv2.imshow(win_name + '_masked_result', masked_result)
    cv2.imshow(win_name + '_contour_result', result)


def backProject_manual(hist_roi):
    # 전체 이미지의 HSV 히스토그램
    hist_img = cv2.calcHist(
        [hsv_img],
        [0, 1],
        None,
        [180, 256],
        [0, 180, 0, 256]
    )

    # ROI 히스토그램 / 전체 이미지 히스토그램
    hist_rate = hist_roi / (hist_img + 1)

    h, s, v = cv2.split(hsv_img)

    # 각 픽셀의 H, S 값을 이용해서 hist_rate에서 값 조회
    bp = hist_rate[h.ravel(), s.ravel()]

    # 1보다 큰 값은 1로 제한
    bp = np.minimum(bp, 1)

    # 원래 이미지 크기로 복원
    bp = bp.reshape(hsv_img.shape[:2])

    # 0~255 범위로 정규화
    cv2.normalize(bp, bp, 0, 255, cv2.NORM_MINMAX)

    bp = bp.astype(np.uint8)

    masking(bp, 'result_manual')


def backProject_cv(hist_roi):
    # OpenCV calcBackProject 사용
    bp = cv2.calcBackProject(
        [hsv_img],
        [0, 1],
        hist_roi,
        [0, 180, 0, 256],
        1
    )

    masking(bp, 'result_cv')


# ROI 선택
x, y, w, h = cv2.selectROI(win_name, img, False)

if w > 0 and h > 0:
    # 여기 중요: x:x+w
    roi = img[y:y+h, x:x+w]

    cv2.rectangle(draw, (x, y), (x+w, y+h), (0, 0, 255), 2)

    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    hist_roi = cv2.calcHist(
        [hsv_roi],
        [0, 1],
        None,
        [180, 256],
        [0, 180, 0, 256]
    )

    # cv2.calcBackProject용으로 히스토그램 정규화
    hist_roi_norm = hist_roi.copy()
    cv2.normalize(hist_roi_norm, hist_roi_norm, 0, 255, cv2.NORM_MINMAX)

    backProject_manual(hist_roi)
    backProject_cv(hist_roi_norm)

cv2.imshow(win_name, draw)
cv2.waitKey(0)
cv2.destroyAllWindows()
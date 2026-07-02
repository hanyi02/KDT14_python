
import base64, json
from io import BytesIO
import cv2
import numpy as np
from PIL import Image

def load_image_from_upload(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    if image_bgr is None:
        raise ValueError('이미지를 읽을 수 없습니다.')
    return image_bgr

def load_labelme_json(json_bytes):
    return json.loads(json_bytes.decode('utf-8-sig'))

def restore_image_from_labelme(data):
    img_data = data.get('imageData')
    if not img_data:
        return None
    raw = base64.b64decode(img_data)
    image = Image.open(BytesIO(raw)).convert('RGB')
    image_rgb = np.array(image)
    return cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

def detect_defect_candidates(image_bgr):
    h, w = image_bgr.shape[:2]
    img_area = h * w
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    kernel = np.ones((5,5), np.uint8)
    morph = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=2)
    morph = cv2.dilate(morph, kernel, iterations=1)
    contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    candidates = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < img_area * 0.0005 or area > img_area * 0.35:
            continue
        x,y,bw,bh = cv2.boundingRect(cnt)
        if bw < 15 or bh < 15:
            continue
        box_area = bw * bh
        if box_area < img_area * 0.001:
            continue
        aspect = bw / max(bh, 1)
        extent = area / max(box_area, 1)
        label = recommend_defect_type(area, bw, bh, aspect, extent)
        candidates.append({'x':int(x),'y':int(y),'w':int(bw),'h':int(bh),'area':float(area),'aspect':float(aspect),'extent':float(extent),'recommend_label':label})
    return sorted(candidates, key=lambda d: d['area'], reverse=True)[:8]

def recommend_defect_type(area, w, h, aspect, extent):
    if aspect >= 3.0 or aspect <= 0.33:
        return 'Scratch'
    if extent < 0.35:
        return 'Paint Defect'
    return 'Dent'

def draw_boxes(image_rgb, candidates):
    out = image_rgb.copy()
    for idx, c in enumerate(candidates, 1):
        x,y,w,h = c['x'], c['y'], c['w'], c['h']
        cv2.rectangle(out, (x,y), (x+w,y+h), (255,80,80), 3)
        cv2.putText(out, f"CV {idx}: {c['recommend_label']}", (x, max(20,y-8)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,80,80), 2)
    return out

def labelme_shapes_to_gt(data):
    items = []
    for shape in data.get('shapes', []):
        label = shape.get('label','')
        points = shape.get('points', [])
        if not points:
            continue
        pts = [(int(round(x)), int(round(y))) for x,y in points]
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        items.append({'label': label, 'points': pts, 'bbox': {'x':min(xs),'y':min(ys),'w':max(xs)-min(xs),'h':max(ys)-min(ys)}, 'best_iou':0.0})
    return items

def draw_labelme_polygons(image_rgb, gt_items):
    out = image_rgb.copy()
    for idx, item in enumerate(gt_items, 1):
        pts = np.array(item['points'], dtype=np.int32)
        cv2.polylines(out, [pts], True, (80,255,80), 3)
        x,y = item['bbox']['x'], item['bbox']['y']
        cv2.putText(out, f"GT {idx}: {item['label']}", (x, max(20,y-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (80,255,80), 2)
    return out

def bbox_iou(a,b):
    ax1, ay1, ax2, ay2 = a['x'], a['y'], a['x']+a['w'], a['y']+a['h']
    bx1, by1, bx2, by2 = b['x'], b['y'], b['x']+b['w'], b['y']+b['h']
    ix1, iy1, ix2, iy2 = max(ax1,bx1), max(ay1,by1), min(ax2,bx2), min(ay2,by2)
    inter = max(0, ix2-ix1) * max(0, iy2-iy1)
    area_a = max(0, ax2-ax1) * max(0, ay2-ay1)
    area_b = max(0, bx2-bx1) * max(0, by2-by1)
    union = area_a + area_b - inter
    return 0.0 if union == 0 else inter / union

def compare_candidates_with_gt(candidates, gt_items):
    for gt in gt_items:
        best = 0.0
        for cand in candidates:
            best = max(best, bbox_iou(cand, gt['bbox']))
        gt['best_iou'] = float(best)
    return gt_items

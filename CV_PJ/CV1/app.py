
import json
from datetime import datetime
from pathlib import Path
import cv2
import streamlit as st
from cv_utils import load_image_from_upload, load_labelme_json, restore_image_from_labelme, detect_defect_candidates, draw_boxes, draw_labelme_polygons, labelme_shapes_to_gt, compare_candidates_with_gt
from db import get_connection, init_db, insert_inspection, fetch_summary

BASE_DIR = Path(__file__).parent
UPLOAD_IMAGE_DIR = BASE_DIR / 'uploads' / 'images'
UPLOAD_JSON_DIR = BASE_DIR / 'uploads' / 'json'
UPLOAD_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
UPLOAD_JSON_DIR.mkdir(parents=True, exist_ok=True)

st.set_page_config(page_title='차체 결함 검사 MVP', layout='wide')
st.title('MariaDB 기반 차체 결함 검사 이력 관리 시스템')
st.caption('OpenCV 후보 검출 + LabelMe 정답좌표 검증 + 검사자 판정 + MariaDB 저장')

with st.sidebar:
    st.header('MariaDB 설정')
    host = st.text_input('Host', 'localhost')
    port = st.number_input('Port', value=3306, step=1)
    user = st.text_input('User', 'root')
    password = st.text_input('Password', type='password')
    database = st.text_input('Database', 'car_quality_db')
    if st.button('DB 초기화 / 테이블 생성'):
        try:
            init_db(host, int(port), user, password, database)
            st.success('DB와 테이블 생성 완료')
        except Exception as e:
            st.error(f'DB 초기화 실패: {e}')

tab1, tab2, tab3 = st.tabs(['검사 등록', '대시보드', '사용 방법'])

with tab1:
    st.subheader('검사 등록')
    input_mode = st.radio('입력 방식 선택', ['일반 이미지 업로드', 'LabelMe JSON 업로드'], horizontal=True)

    image_bgr = None
    image_rgb = None
    gt_items = []
    source_type = None
    saved_image_path = ''
    saved_json_path = ''
    original_filename = ''

    if input_mode == '일반 이미지 업로드':
        uploaded = st.file_uploader('JPG / PNG 이미지를 업로드하세요', type=['jpg','jpeg','png'])
        if uploaded is not None:
            source_type = 'IMAGE'
            original_filename = uploaded.name
            image_bgr = load_image_from_upload(uploaded)
            image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            saved_image_path = str(UPLOAD_IMAGE_DIR / f'{timestamp}_{uploaded.name}')
            cv2.imwrite(saved_image_path, image_bgr)
    else:
        uploaded_json = st.file_uploader('LabelMe JSON 파일을 업로드하세요', type=['json','txt'])
        if uploaded_json is not None:
            source_type = 'JSON'
            original_filename = uploaded_json.name
            json_bytes = uploaded_json.getvalue()
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            saved_json_path = str(UPLOAD_JSON_DIR / f'{timestamp}_{uploaded_json.name}')
            with open(saved_json_path, 'wb') as f:
                f.write(json_bytes)
            data = load_labelme_json(json_bytes)
            image_bgr = restore_image_from_labelme(data)
            if image_bgr is None:
                st.error('이 JSON에는 imageData가 없습니다. 원본 JPG/PNG를 일반 이미지 모드에서 업로드해야 합니다.')
            else:
                image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
                image_name = Path(data.get('imagePath', 'restored.jpg')).name
                if not image_name.lower().endswith(('.jpg','.jpeg','.png')):
                    image_name = 'restored.jpg'
                saved_image_path = str(UPLOAD_IMAGE_DIR / f'{timestamp}_{image_name}')
                cv2.imwrite(saved_image_path, image_bgr)
                gt_items = labelme_shapes_to_gt(data)

    if image_bgr is not None:
        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('#### 원본 이미지')
            st.image(image_rgb, use_container_width=True)
        candidates = detect_defect_candidates(image_bgr)
        if gt_items:
            compare_candidates_with_gt(candidates, gt_items)
        annotated = draw_boxes(image_rgb, candidates)
        if gt_items:
            annotated = draw_labelme_polygons(annotated, gt_items)
        with c2:
            st.markdown('#### OpenCV 후보 검출 결과')
            st.image(annotated, use_container_width=True)
        st.markdown('### 검출 결과 요약')
        if not candidates:
            st.warning('OpenCV 후보 영역이 없습니다. 결함이 약하거나 전처리 조건 조정이 필요합니다.')
        else:
            for i, cand in enumerate(candidates, 1):
                st.write(f"후보 {i}: 추천={cand['recommend_label']} / x={cand['x']}, y={cand['y']}, w={cand['w']}, h={cand['h']}, area={cand['area']:.1f}")
        if gt_items:
            st.markdown('### LabelMe 정답 라벨 비교')
            for i, gt in enumerate(gt_items, 1):
                status = '성공' if gt.get('best_iou', 0) >= 0.1 else '미검출'
                st.write(f"정답 {i}: {gt['label']} / IoU={gt.get('best_iou', 0):.3f} / 판정={status}")
        else:
            st.info('일반 이미지 모드입니다. 정답 라벨이 없으므로 IoU 평가는 하지 않습니다.')
        st.divider()
        st.markdown('### 검사자 최종 판정 입력')
        with st.form('inspection_form'):
            a,b,c = st.columns(3)
            with a:
                car_model = st.text_input('차종', 'Sample Car')
                body_part = st.selectbox('차체 부위', ['door','hood','bumper','fender','roof','trunk','unknown'])
            with b:
                process_name = st.selectbox('공정', ['press','welding','painting','assembly','inspection','unknown'])
                final_label = st.selectbox('최종 결함 유형', ['Dent','Scratch','Paint Defect','Assembly Defect','Normal','Unknown'])
            with c:
                severity = st.selectbox('심각도', ['Low','Medium','High','Critical'])
                inspector = st.text_input('검사자', 'inspector')
            action_taken = st.text_area('조치 내용', '재검사 필요')
            submit = st.form_submit_button('MariaDB 저장')
        if submit:
            try:
                conn = get_connection(host, int(port), user, password, database)
                gt_label, gt_polygon, iou_score = '', '', None
                if gt_items:
                    gt_label = gt_items[0]['label']
                    gt_polygon = json.dumps(gt_items[0]['points'], ensure_ascii=False)
                    iou_score = float(gt_items[0].get('best_iou', 0))
                cv_recommend_label, cv_bbox = '', ''
                if candidates:
                    top = candidates[0]
                    cv_recommend_label = top['recommend_label']
                    cv_bbox = json.dumps({'x':top['x'],'y':top['y'],'w':top['w'],'h':top['h']}, ensure_ascii=False)
                insert_inspection(conn, saved_image_path, saved_json_path, original_filename, source_type, car_model, body_part, process_name, gt_label, gt_polygon, cv_recommend_label, cv_bbox, iou_score, final_label, severity, action_taken, inspector)
                conn.close()
                st.success('MariaDB 저장 완료')
            except Exception as e:
                st.error(f'저장 실패: {e}')
                st.warning('DB 초기화 버튼을 먼저 눌렀는지, MariaDB 비밀번호가 맞는지 확인하세요.')

with tab2:
    st.subheader('대시보드')
    try:
        conn = get_connection(host, int(port), user, password, database)
        summary = fetch_summary(conn)
        conn.close()
        m1,m2,m3,m4 = st.columns(4)
        m1.metric('전체 검사 수', summary['total_count'])
        m2.metric('High 이상', summary['high_count'])
        m3.metric('JSON 라벨 데이터', summary['json_count'])
        m4.metric('일반 이미지 데이터', summary['image_count'])
        st.markdown('### 결함 유형별 건수')
        if summary['by_label']:
            st.bar_chart({r['final_label']: r['cnt'] for r in summary['by_label']})
            st.table(summary['by_label'])
        else:
            st.info('저장된 데이터가 없습니다.')
        st.markdown('### 차체 부위별 건수')
        if summary['by_part']:
            st.bar_chart({r['body_part']: r['cnt'] for r in summary['by_part']})
            st.table(summary['by_part'])
        st.markdown('### 공정별 건수')
        if summary['by_process']:
            st.bar_chart({r['process_name']: r['cnt'] for r in summary['by_process']})
            st.table(summary['by_process'])
        st.markdown('### 최근 검사 이력')
        st.table(summary['recent'])
    except Exception as e:
        st.warning(f'대시보드를 불러오지 못했습니다: {e}')
        st.info('왼쪽 사이드바에서 DB 정보를 입력하고 DB 초기화 / 테이블 생성을 먼저 실행하세요.')

with tab3:
    st.subheader('사용 방법')
    st.write('일반 이미지는 JPG/PNG 업로드 모드, LabelMe 라벨 파일은 JSON 업로드 모드에서 넣습니다.')
    st.write('JSON의 imageData는 이미지 복원용, shapes.points는 정답 좌표 평가용입니다.')
    st.write('OpenCV는 정답 좌표를 보지 않고 이미지만 보고 후보 영역을 검출합니다.')
    st.write('글자/도식 이미지는 글자와 박스를 결함처럼 잡으므로 차체 결함 이미지로 테스트해야 합니다.')

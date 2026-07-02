
import pymysql

def get_connection(host, port, user, password, database):
    return pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=True)

def init_db(host, port, user, password, database):
    conn = pymysql.connect(host=host, port=port, user=user, password=password, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    with conn.cursor() as cur:
        cur.execute(f"CREATE DATABASE IF NOT EXISTS `{database}` DEFAULT CHARACTER SET utf8mb4;")
        cur.execute(f"USE `{database}`;")
        cur.execute('''
        CREATE TABLE IF NOT EXISTS inspections (
            inspection_id INT AUTO_INCREMENT PRIMARY KEY,
            image_path VARCHAR(500), json_path VARCHAR(500), original_filename VARCHAR(255), source_type VARCHAR(20),
            car_model VARCHAR(100), body_part VARCHAR(100), process_name VARCHAR(100),
            gt_label VARCHAR(100), gt_polygon LONGTEXT,
            cv_recommend_label VARCHAR(100), cv_bbox TEXT, iou_score DOUBLE NULL,
            final_label VARCHAR(100), severity VARCHAR(50), action_taken TEXT, inspector VARCHAR(100),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ) CHARACTER SET utf8mb4;
        ''')
    conn.close()

def insert_inspection(conn, image_path, json_path, original_filename, source_type, car_model, body_part, process_name, gt_label, gt_polygon, cv_recommend_label, cv_bbox, iou_score, final_label, severity, action_taken, inspector):
    sql = '''
    INSERT INTO inspections (image_path,json_path,original_filename,source_type,car_model,body_part,process_name,gt_label,gt_polygon,cv_recommend_label,cv_bbox,iou_score,final_label,severity,action_taken,inspector)
    VALUES (%(image_path)s,%(json_path)s,%(original_filename)s,%(source_type)s,%(car_model)s,%(body_part)s,%(process_name)s,%(gt_label)s,%(gt_polygon)s,%(cv_recommend_label)s,%(cv_bbox)s,%(iou_score)s,%(final_label)s,%(severity)s,%(action_taken)s,%(inspector)s)
    '''
    params = dict(image_path=image_path, json_path=json_path, original_filename=original_filename, source_type=source_type, car_model=car_model, body_part=body_part, process_name=process_name, gt_label=gt_label, gt_polygon=gt_polygon, cv_recommend_label=cv_recommend_label, cv_bbox=cv_bbox, iou_score=iou_score, final_label=final_label, severity=severity, action_taken=action_taken, inspector=inspector)
    with conn.cursor() as cur:
        cur.execute(sql, params)

def fetch_summary(conn):
    result = {'total_count':0, 'high_count':0, 'json_count':0, 'image_count':0, 'by_label':[], 'by_part':[], 'by_process':[], 'recent':[]}
    with conn.cursor() as cur:
        cur.execute('SELECT COUNT(*) AS cnt FROM inspections;'); result['total_count'] = cur.fetchone()['cnt']
        cur.execute("SELECT COUNT(*) AS cnt FROM inspections WHERE severity IN ('High','Critical');"); result['high_count'] = cur.fetchone()['cnt']
        cur.execute("SELECT COUNT(*) AS cnt FROM inspections WHERE source_type='JSON';"); result['json_count'] = cur.fetchone()['cnt']
        cur.execute("SELECT COUNT(*) AS cnt FROM inspections WHERE source_type='IMAGE';"); result['image_count'] = cur.fetchone()['cnt']
        cur.execute('SELECT final_label, COUNT(*) AS cnt FROM inspections GROUP BY final_label ORDER BY cnt DESC;'); result['by_label'] = cur.fetchall()
        cur.execute('SELECT body_part, COUNT(*) AS cnt FROM inspections GROUP BY body_part ORDER BY cnt DESC;'); result['by_part'] = cur.fetchall()
        cur.execute('SELECT process_name, COUNT(*) AS cnt FROM inspections GROUP BY process_name ORDER BY cnt DESC;'); result['by_process'] = cur.fetchall()
        cur.execute('SELECT inspection_id, original_filename, source_type, car_model, body_part, process_name, final_label, severity, cv_recommend_label, iou_score, created_at FROM inspections ORDER BY inspection_id DESC LIMIT 20;'); result['recent'] = cur.fetchall()
    return result

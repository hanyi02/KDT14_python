#%%

import pandas as pd
from sqlalchemy import create_engine

# engine = create_engine('mysql+pymysql://[사용자명]:[비밀번호]@[호스트:포트]/[사용할 데이터베이스]')
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/us_stock')
query = """select * from stock 
where date> '2026-04-01' and symbol="NVDA"; """
goods = pd.read_sql(query, con=engine)
engine.dispose()

goods
# %%
goods[['date', 'close']]
# %%

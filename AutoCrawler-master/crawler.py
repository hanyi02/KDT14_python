#%%

from datetime import datetime, timedelta

import pymysql
import pandas as pd
import yfinance as yf

mysql_conn = pymysql.connect(host='localhost', user='root', password='doitmysql', db='us_stock')
#%%
mysql_cur = mysql_conn.cursor()
today = datetime.today() + timedelta(days=1)
query = """select symbol, company_name, ipo_year, last_crawel_date_stock 
from us_stock.nasdaq_company where is_delete is null;"""
mysql_cur.execute(query)
results = mysql_cur.fetchall()
symbols = [row[0]  for row in results]
symbols

#%%

for _symbol in symbols:
    _start_date = '2026-01-01'
    _end_date = '2026-12-31'
    # _symbol = 'AMD'
    print(_symbol)

    query = """
    delete from us_stock.stock
    where date >= %s and date <= %s and symbol = %s;
    """
    mysql_cur.execute(query=query, args=(_start_date, _end_date, _symbol))
    mysql_conn.commit()

    #yf.download already returns a DataFrame.
    stock_price = yf.download(_symbol, start=_start_date, end=_end_date)

    import datetime
    #명시적 형변환...
    d = datetime.datetime.strptime('2026-04-23', '%Y-%m-%d')
    stock_price.loc[d, :]
    #근데 묵시적 형변환 가능
    stock_price.loc['2026-04-23', :]

    # 각 행을 반복문으로 가져오기
    data_list = []
    for index, row in stock_price.iterrows():
        _date = index.strftime("%Y-%m-%d") # datetime -> str
        _open = str(row["Open", _symbol])
        _high = str(row["High", _symbol])
        _low = str(row["Low", _symbol])
        _close = str(row["Close", _symbol])
        _volume = str(row["Volume", _symbol])

        query = """insert into us_stock.stock 
        (date, symbol, open, high, low, close, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s);"""
        
        # mysql_cur.execute(query, (_date, _symbol, _open, _high, _low, _close, _volume))
        data = (_date, _symbol, _open, _high, _low, _close, _volume)
        data_list.append(data)

    # 효율을 생각하면 executemany 를 추천!
    mysql_cur.executemany(query, data_list)
    mysql_conn.commit()
#%%

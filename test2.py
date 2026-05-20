import json
import pandas as pd

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

pd.Series(data['data']['list'][0])

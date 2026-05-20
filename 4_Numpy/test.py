#%%
a=1
b=2
c=a+b

# %%
import numpy as np
a= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
a
# %%
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
f= open('data.txt', 'w')
rows, cols= a.shape
for y in range(rows):
    for x in range(cols):
        f.write(str(a[y, x]))
        f.write(',')
    f.write('\n')
f.close()

# %%
f = open('data.txt', 'r')

data = []

for line in f.readlines():
    row = []   # 한 줄마다 새 리스트 생성

    for num in line.strip().split(','):
        if num == '':
            continue
        row.append(int(num))

    data.append(row)

f.close()

data = np.array(data)
print(data)

# %%
import pandas as pd
pd.read_csv('data.txt')
# %%
# xml, json, yaml, html, ...

# 자바스크립트=> 파이썬 딕셔너리, 리스트를 기본 지원하는데 JSON에도 잘 어울림

import json
# json 은 그대로 저장 못 함(numpy)
f = open('data.txt', 'w')

json.dump(a.tolist(), open('data.json', 'w'))



open('data.json', 'r').readline()
# %%
np.array(json.load(open('data.json')))


# %%
import pickle
pickle.dump(a, open('data.pickle', 'wb'))
# %%
pickle.load(open('data.pickle', 'rb'))
# %%

np.save('asdf.npy', a)
# %%
import json
import pandas as pd

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

pd.Series(data['data']['list'][0])

# %%

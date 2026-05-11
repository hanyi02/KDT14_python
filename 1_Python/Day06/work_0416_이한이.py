 
# ================================================================
#  Python 컨프리헨션 실습 문제집
#  List / Set / Dictionary Comprehension
# ================================================================


# ----------------------------------------------------------------
#  1. 리스트 컨프리헨션 (List Comprehension)
# ----------------------------------------------------------------
# ★ 초급 (Beginner)

# [문제 1-1]
# 1부터 20까지의 정수 중에서 짝수만 골라 리스트를 만드세요.
# 예상 출력: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("문제1-1")
print([i for i in range(21) if i%2==0])

# ----------------------------------------------------------------
# [문제 1-2]
# 문자열 리스트 ["hello", "world", "python", "list"]에서
# 각 단어를 대문자로 변환한 새 리스트를 만드세요.
# 예상 출력: ['HELLO', 'WORLD', 'PYTHON', 'LIST']
print("문제1-2")

### 기본적인 반복문 ###
a= ["hello", "world", "python", "list"]
b= []

for i in a:
    b.append(i.upper())
print(b)

### 리스트 컴프리헨션 ###
a= ["hello", "world", "python", "list"]
b= [i.upper() for i in a]

# ----------------------------------------------------------------
# [문제 1-3]
# numbers = [1, 2, 3, 4, 5]일 때,
# 각 숫자의 제곱값을 담은 리스트를 만드세요.
# 예상 출력: [1, 4, 9, 16, 25]
print("문제1-3")

### 기본적인 반복문 ###
numbers= [1, 2, 3, 4, 5]
b= []
for i in numbers:
    b.append(i**2)
print(b)


### 리스트 컴프리헨션 ###
numbers= [1, 2, 3, 4, 5]
b= [i**2 for i in numbers]
print(b)


# ----------------------------------------------------------------
# [문제 1-4]
# 문자열 "Hello, World!"에서 알파벳 소문자만 추출하여 리스트를 만드세요.
# 예상 출력: ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']
print("문제1-4")
### 기본적인 반복문 ###
a="Hello, World!"
b=[]

for i in a:
    if i.islower():
        b.append(i)
print(b)

### 리스트 컴프리헨션 ###

a="Hello, World!"
b= [i for i in a if i.islower()]
print(b)


# ----------------------------------------------------------------
# [문제 1-5]
# 0부터 9까지의 숫자 중 3의 배수(0 포함)를 담은 리스트를 만드세요.
# 예상 출력: [0, 3, 6, 9]
print("문제1-5")
### 기본적인 반복문 ###
b=[]
for i in range(10):
    if i%3==0:
        b.append(i)
print(b)


### 리스트 컴프리헨션 ###
b= [i for i in range(10) if i%3==0]
print(b)


# ----------------------------------------------------------------

# ★★ 중급 (Intermediate)

# [문제 1-6]
# numbers = [3, -1, 4, -1, 5, -9, 2, -6, 5]에서
# 양수는 그대로, 음수는 0으로 바꾼 리스트를 만드세요.
# 예상 출력: [3, 0, 4, 0, 5, 0, 2, 0, 5]
print("문제1-6")
### 기본적인 반복문 ###
numbers = [3, -1, 4, -1, 5, -9, 2, -6, 5]
b=[]
for i in numbers:
    b.append(i if i>0 else 0)
print(b)

### 리스트 컴프리헨션 ###

a=[i if i>0 else 0 for i in numbers]
print(a)
 
# ----------------------------------------------------------------

# [문제 1-7]
# matrix = [[1,2,3],[4,5,6],[7,8,9]] 인 2차원 리스트를
# 1차원 리스트로 평탄화(flatten)하세요.
# 예상 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("문제1-7")
### 기본적인 반복문 ###
matrix = [[1,2,3],[4,5,6],[7,8,9]]
nums = []
for i in matrix:
    for j in i:
        nums.append(j)
print(nums)



### 리스트 컴프리헨션 ###
nums = [j for i in matrix for j in i]
print(nums)


# ----------------------------------------------------------------

# [문제 1-8]
# words = ["apple", "banana", "cherry", "date", "elderberry"]에서
# 글자 수가 5 이상인 단어들만 대문자로 변환하여 리스트를 만드세요.
# 예상 출력: ['APPLE', 'BANANA', 'CHERRY', 'ELDERBERRY']

print("문제1-8")

### 기본적인 반복문 ###
words = ["apple", "banana", "cherry", "date", "elderberry"]
word=[]
for i in words:
    if len(i)>=5:
        word.append(i.upper())
print(word)


### 리스트 컴프리헨션 ###
word= [i.upper() for i in words if len(i)>=5]

  
# ----------------------------------------------------------------

# [문제 1-9]
# 두 리스트 a = [1,2,3]과 b = [4,5,6]에서
# a의 원소 * b의 원소 조합 중 곱이 10 이상인 경우만 모아
# (a원소, b원소, 곱) 튜플 리스트를 만드세요.
# 예상 출력: [(2, 5, 10), (2, 6, 12), (3, 4, 12), (3, 5, 15), (3, 6, 18)]
print("문제1-9")

### 기본적인 반복문 ###
a = [1,2,3]
b = [4,5,6]
c=[]

for i in a :
    for j in b:
        if i*j>=10:
            c.append((i, j, i*j))    
print(c)


### 리스트 컴프리헨션 ###

c = [(i, j, i*j) for i in a for j in b if i*j >= 10]
print(c)



# ----------------------------------------------------------------

# [문제 1-10]
# sentences = ["I love Python", "Python is fun", "I am learning"]에서
# 각 문장을 단어 단위로 분리하되, "Python"이 포함된 문장의 단어만 모아
# 하나의 리스트로 만드세요.
# 예상 출력: ['I', 'love', 'Python', 'Python', 'is', 'fun']

print("문제1-10")
sentences = ["I love Python", "Python is fun", "I am learning"]
word=[]

### 기본적인 반복문 ###
for i in sentences:
    if "Python" in i :
        for j in i.split():
            word.append(j)
print(word)

### 리스트 컴프리헨션 ###
a = [j for i in sentences if "Python" in i for j in i.split()]
print(a)

# ---


# ----------------------------------------------------------------
#  2. 셋 컨프리헨션 (Set Comprehension)
# ----------------------------------------------------------------

# ★ 초급 (Beginner)

# [문제 2-1]
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]에서
# 중복을 제거한 값들의 집합을 셋 컨프리헨션으로 만드세요.
# 예상 출력: {1, 2, 3, 4}
print("문제2-1")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

### 기본적인 반복문 ###

result = set()
for i in numbers:
    result.add(i)
print(result) 

### 셋 컴프리헨션 ###
a = {i for i in numbers}
print(a)

# ----------------------------------------------------------------


# [문제 2-2]
# 1부터 10까지의 숫자에서 2의 배수 집합을 만드세요.
# 예상 출력: {2, 4, 6, 8, 10}

print("문제2-2")

### 기본적인 반복문 ###
result=set()
for i in range(1,11):
    if i%2==0:
        result.add(i)
print(result)


### 셋 컴프리헨션 ###
a={i for i in range(1, 11) if i%2==0}
print(a)


# ----------------------------------------------------------------


# [문제 2-3]
# 문자열 "mississippi"에서 등장하는 고유 문자들의 집합을 만드세요.
# 예상 출력: {'m', 'i', 's', 'p'}

print("문제2-3")

st="mississippi"


### 기본적인 반복문 ###
result=set()
for i in st:
    result.add(i)
print(result)


### 셋 컴프리헨션 ###
a={i for i in st}
print(a)


# ----------------------------------------------------------------


# [문제 2-4]
# words = ["apple","banana","cherry","apricot","blueberry"]에서
# 첫 글자만 모은 집합을 만드세요. (중복 없음)
# 예상 출력: {'a', 'b', 'c'}
print("문제2-4")
words = ["apple","banana","cherry","apricot","blueberry"]
result=set()

### 기본적인 반복문 ###
for i in words:
    result.add(i[0])
print(result)

### 셋 컴프리헨션 ###
a={i[0] for i in words}
print(a)

# ----------------------------------------------------------------


# [문제 2-5]
# numbers = [1,2,3,4,5,6,7,8,9,10]에서
# 각 숫자를 제곱한 값들의 집합을 만드세요.
# 예상 출력: {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
print("문제2-5")
numbers = [1,2,3,4,5,6,7,8,9,10]
result=set()

### 기본적인 반복문 ###
for i in numbers:
    result.add(i**2)
print(result)


### 셋 컴프리헨션 ###
a={i**2 for i in numbers}
print(a)


# ---

# ★★ 중급 (Intermediate)

# [문제 2-6]
# 문자열 리스트 words = ["Python","python","PYTHON","Java","java","JAVA"]에서
# 모두 소문자로 변환한 뒤 중복을 제거한 집합을 만드세요.
# 예상 출력: {'python', 'java'}
print("문제2-6")
words = ["Python","python","PYTHON","Java","java","JAVA"]
result=set()

### 기본적인 반복문 ###
for i in words:
    result.add(i.lower())
print(result)


### 셋 컴프리헨션 ###
a={i.lower() for i in words}
print(a)


# ----------------------------------------------------------------


# [문제 2-7]
# a = {1,2,3,4,5}, b = {3,4,5,6,7} 일 때,
# 셋 컨프리헨션으로 두 집합 중 하나에만 속하는 원소들의 집합(대칭 차집합)을 만드세요.
# 예상 출력: {1, 2, 6, 7}
print("문제2-7")
a = {1,2,3,4,5}
b = {3,4,5,6,7}
result=set()

### 기본적인 반복문 ###
# a에만 있는 것
for i in a:
    if i not in b:
        result.add(i)

# b에만 있는 것
for i in b:
    if i not in a:
        result.add(i)

print(result)


### 셋 컴프리헨션 ###
result= {j for j in a if j not in b} ^ {j for j in b if j not in a}

print(result)


# ----------------------------------------------------------------



# [문제 2-8]
# sentences = ["I love Python", "Python is great", "I enjoy coding"]에서
# 모든 문장에 등장하는 단어들을 소문자 변환 후 중복 없이 모은 집합을 만드세요.
# 예상 출력: {'i', 'love', 'python', 'is', 'great', 'enjoy', 'coding'}
print("문제2-8")
result=set()

### 기본적인 반복문 ###
for i in sentences:
    for j in i.split():
        result.add(j)
print(result)

### 셋 컴프리헨션 ###
a = {j for i in sentences for j in i.split()}
print(a)


# ----------------------------------------------------------------
 
# [문제 2-9]
# numbers = list(range(1, 21))에서
# 3의 배수이거나 7의 배수인 숫자들의 집합을 만드세요.
# 예상 출력: {3, 6, 7, 9, 12, 14, 15, 18}
print("문제2-9")
numbers = list(range(1, 21))
result=set()


### 기본적인 반복문 ###
for i in numbers:
    if i%3==0 or i%7==0:
        result.add(i)
print(result)


### 셋 컴프리헨션 ###
a={i for i in numbers if i%3==0 or i%7==0}
print(a)

# ----------------------------------------------------------------



# [문제 2-10]
# pairs = [(1,2),(2,3),(3,4),(1,3),(2,4)]에서
# 각 쌍의 합이 짝수인 경우, 그 합 값들로 집합을 만드세요.
# 예상 출력: {4, 6}
print("문제2-10")
pairs = [(1,2),(2,3),(3,4),(1,3),(2,4)]
result=set()


### 기본적인 반복문 ###
for j, k in pairs:
    if (j+k)%2==0:
        result.add(j+k)

print(result)

### 셋 컴프리헨션 ###
a={j+k for j, k in pairs if (j+k)%2==0}
print(a)


# ---


# ----------------------------------------------------------------
#  3. 딕셔너리 컨프리헨션 (Dictionary Comprehension)
# ----------------------------------------------------------------

# ★ 초급 (Beginner)

# [문제 3-1]
# 1부터 5까지의 숫자를 키로, 그 제곱을 값으로 하는 딕셔너리를 만드세요.
# 예상 출력: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("문제3-1")

### 기본적인 반복문 ###
result = {}

for i in range(1, 6):
    result[i] = i**2

print(result)

### 딕셔너리 컴프리헨션 ###
a = {i: i**2 for i in range(1, 6)}
print(a)

# ----------------------------------------------------------------


# [문제 3-2]
# words = ["apple","banana","cherry"]에서
# 단어를 키로, 단어의 길이를 값으로 하는 딕셔너리를 만드세요.
# 예상 출력: {'apple': 5, 'banana': 6, 'cherry': 6}
print("문제3-2")

words = ["apple","banana","cherry"]

### 기본적인 반복문 ###
result = {}

for word in words:
    result[word] = len(word)

print(result)

### 딕셔너리 컴프리헨션 ###
a = {word: len(word) for word in words}
print(a)

# ----------------------------------------------------------------


# [문제 3-3]
# 기존 딕셔너리 d = {'a':1, 'b':2, 'c':3}의 키와 값을 서로 뒤집은 딕셔너리를 만드세요.
# 예상 출력: {1: 'a', 2: 'b', 3: 'c'}
print("문제3-3")

d = {'a':1, 'b':2, 'c':3}

### 기본적인 반복문 ###
result = {}

for key, value in d.items():
    result[value] = key

print(result)

### 딕셔너리 컴프리헨션 ###
a = {value: key for key, value in d.items()}
print(a)

# ----------------------------------------------------------------


# [문제 3-4]
# keys = ['name','age','city'], values = ['Alice', 30, 'Seoul']을
# zip으로 묶어 딕셔너리를 만드세요.
# 예상 출력: {'name': 'Alice', 'age': 30, 'city': 'Seoul'}
print("문제3-4")

keys = ['name','age','city']
values = ['Alice', 30, 'Seoul']

### 기본적인 반복문 ###
result = {}

for k, v in zip(keys, values):
    result[k] = v

print(result)

### 딕셔너리 컴프리헨션 ###
a = {k: v for k, v in zip(keys, values)}
print(a)

# ----------------------------------------------------------------


# [문제 3-5]
# 알파벳 'a'부터 'e'까지를 키로, 해당 알파벳의 ASCII 코드를 값으로 하는
# 딕셔너리를 만드세요.
# 예상 출력: {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101}
print("문제3-5")

### 기본적인 반복문 ###
result = {}

for ch in ['a', 'b', 'c', 'd', 'e']:
    result[ch] = ord(ch)

print(result)

### 딕셔너리 컴프리헨션 ###
a = {ch: ord(ch) for ch in ['a', 'b', 'c', 'd', 'e']}
print(a)

# ----------------------------------------------------------------


# [문제 3-6]
# scores = {'Alice':85, 'Bob':42, 'Carol':91, 'Dave':58, 'Eve':76}에서
# 점수가 60 이상인 학생만 포함하고, 점수에 5점을 더한 딕셔너리를 만드세요.
# 예상 출력: {'Alice': 90, 'Carol': 96, 'Eve': 81}
print("문제3-6")

scores = {'Alice':85, 'Bob':42, 'Carol':91, 'Dave':58, 'Eve':76}

### 기본적인 반복문 ###
result = {}

for name, score in scores.items():
    if score >= 60:
        result[name] = score + 5

print(result)

### 딕셔너리 컴프리헨션 ###
a = {name: score+5 for name, score in scores.items() if score >= 60}
print(a)

# ----------------------------------------------------------------


# [문제 3-7]
# text = "hello world"에서 각 문자를 키로, 등장 횟수를 값으로 하는
# 딕셔너리를 컨프리헨션으로 만드세요. (공백 제외)
# 예상 출력: {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1}
print("문제3-7")

text = "hello world"

### 기본적인 반복문 ###
result = {}

for ch in text:
    if ch != ' ':
        result[ch] = text.count(ch)

print(result)

### 딕셔너리 컴프리헨션 ###
a = {ch: text.count(ch) for ch in text if ch != ' '}
print(a)

# ----------------------------------------------------------------


# [문제 3-8]
# items = [("apple",3),("banana",5),("cherry",2),("date",8)]에서
# 수량이 4 이상인 항목만 골라 {품목: 수량} 딕셔너리를 만드세요.
# 예상 출력: {'banana': 5, 'date': 8}
print("문제3-8")

items = [("apple",3),("banana",5),("cherry",2),("date",8)]

### 기본적인 반복문 ###
result = {}

for item, qty in items:
    if qty >= 4:
        result[item] = qty

print(result)

### 딕셔너리 컴프리헨션 ###
a = {item: qty for item, qty in items if qty >= 4}
print(a)

# ----------------------------------------------------------------


# [문제 3-9]
# numbers = [1,2,3,4,5,6,7,8,9,10]에서
# 홀수는 키로 "odd", 짝수는 키로 "even"으로 분류하되,
# {숫자: "odd"/"even"} 형태의 딕셔너리를 만드세요.
# 예상 출력: {1:'odd',2:'even',3:'odd',4:'even',5:'odd',
#             6:'even',7:'odd',8:'even',9:'odd',10:'even'}
print("문제3-9")

numbers = [1,2,3,4,5,6,7,8,9,10]

### 기본적인 반복문 ###
result = {}

for n in numbers:
    if n % 2 == 0:
        result[n] = "even"
    else:
        result[n] = "odd"

print(result)

### 딕셔너리 컴프리헨션 ###
a = {n: "even" if n % 2 == 0 else "odd" for n in numbers}
print(a)

# ----------------------------------------------------------------


# [문제 3-10]
# two = {1:'one',2:'two',3:'three'}, three = {2:'TWO',3:'THREE',4:'FOUR'}
# 두 딕셔너리에서 공통 키만 골라 {키: (값1, 값2)} 형태의 딕셔너리를 만드세요.
# 예상 출력: {2: ('two', 'TWO'), 3: ('three', 'THREE')}
print("문제3-10")

two = {1:'one',2:'two',3:'three'}
three = {2:'TWO',3:'THREE',4:'FOUR'}

### 기본적인 반복문 ###
result = {}

for key in two:
    if key in three:
        result[key] = (two[key], three[key])

print(result)

### 딕셔너리 컴프리헨션 ###
a = {key: (two[key], three[key]) for key in two if key in three}
print(a)
 
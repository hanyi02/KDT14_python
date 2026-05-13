## Chap 9. 문자열 사용하기

""" 
s = 'Python isn't difficult'
SyntaxError: invalid syntax ==> 작은 따옴표 안에 작은 따옴표 넣을 수 없음

s = "He said "Python is easy""
SyntaxError: invalid syntax ==> 큰 따옴표 안에 큰 따옴표 넣을 수 없음
"""

# 문자열에 따옴표 포함하는 다른 방법
print('Python isn\'t difficult') #"Python isn't difficult"


# 따옴표 세 개로 묶지 않고 여러 줄로 된 문자열 사용하기
print('Hello\nPython')

""" SyntaxError: Non-UTF-8 code starting with '\xbe' in file string_multiline_quote.py on line 1, 
but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
===> 파일(F) > 다른 이름으로 저장(A)-> 인코딩(E)에서 UTF-8 선택한 뒤 저장
!!! 기본 인코딩이 UTF-8 !!!
"""

# ==============================================================
# 퀴즈
# ===========================================

# 1. 다음 중 문자열을 표현하는 방법으로 올바른 것을 모두 고르세요.
# a. Hello, world!
# b. "Hello, world!"
# c. `Hello, world!`
# d. 'Hello, world!'
# e. [Hello, world!]
# 
# => b, d
# 
# 문자열 표현 방식: "문자", '문자', ''' ''', """  """
# 
# 2. 다음 중 문자열을 여러 줄로 표현하는 방법으로 올바른 것을 모두 고르세요.
# a. '''안녕하세요.
#    파이썬입니다.'''
# 
# b. ``안녕하세요.
#    파이썬입니다.``
# 
# c. """안녕하세요.
#    파이썬입니다."""
# 
# d. 안녕하세요.
#    파이썬입니다.
# 
# e. # 안녕하세요.
#    # 파이썬입니다.
# 
# => a, c
# 
# 여러 줄 문자열은 ''' ''' 이나, """ """로 묶어줘야 함
# 
# 3. 다음 중 문자열 안에 '(작은따옴표)나 "(큰따옴표)를 넣는 방법으로 올바른 것을 모두 고르세요.
# 
# a. 'Hello, \'Python\''
# b. 'Hello, 'Python''
# c. "Hello, 'Python'"
# d. """Hello", Python"""
# e. ""Hello", Python"
# 
# => a, c, d
# 
# b: 작은 따옴표 안에 작은 따옴표 안 됨
# e: 큰 따옴표 안에 큰 따옴표 안 됨
# 

 
 
#   ==============================================================
 
 



#  ==============================================================
# 연습 문제 1: 여러 줄로 된 문자열 사용하기


# 다음 소스 코드를 완성하여 실행 결과대로 문자열이 출력되게 만드세요.
# 실행 결과:
# Python is a programming language that lets you work quickly
# and
# integrate systems more effectively.

# 1번째 방법: ''' 문자열 '''
s= ''' \nPython is a programming language that lets you work quickly
and
integrate systems more effectively.
'''
print(s)


# 2번째 방법: """ 문자열 """
s= """ \nPython is a programming language that lets you work quickly
and
integrate systems more effectively.
"""
print(s)


# 번외: 3번째 방법=> \n 사용
print("\nPython is a programming language that lets you work quickly\nand\nintegrate systems more effectively.")


#  ==============================================================

#  ==============================================================
# 심사문제: 여러 줄로 된 문자열 사용하기
# 다음 소스 코드를 완성하여 실행 결과대로 문자열이 출력되게 만드세요.
# 표준 출력:
# 'Python' is a "programming language"
# that lets you work quickly
# and
# integrate systems more effectively.


s = """'Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively."""

print(s)
#  ==============================================================




## Chap 22. 리스트와 튜플 응용하기

## 리스트에 요소 추가하기
# * append: 요소 하나 추가
a = [10, 20, 30]
a.append(500)
print(a) #[10, 20, 30, 500] 
print(len(a)) #4

a.append([500, 400]) # 리스트 자체가 하나의 요소로 추가 됨. 
print(a) #[10, 20, 30, 500, [500, 400]]
print(len(a)) #5


# * expend: 리스트 연결하여 확장
a = [10, 20, 30]
a.extend([500, 600]) #============> 리스트 자체가 하나의 요소로 추가 되는 게 아니라 리스트 벗겨져서 두 개의 요소로 연결됨.
print(a) #[10, 20, 30, 500, 600]
print(len(a)) #5


# * insert: 특정 인덱스에 요소 추기
a = [10, 20, 30]
a.insert(2, 500)
print(a) #[10, 20, 500, 30]
print(len(a)) #4


# 리스트에서 특정 !!!!!!!!!인덱스!!!!!!!!!!의 요소 삭제하기

# 방법 1: pop()
a = [10, 20, 30]
a.pop() #=> 30
print(a) #[10, 20]

a.pop(1) # 20
print(a) #[10, 30]

# 방법 2: del
a = [10, 20, 30]
del a[1]
print(a) #[10, 30]


# 리스트에서 특정 !!!!!!!!!값!!!!!!!!!! 삭제하기

a = [10, 20, 30, 20]
a.remove(20)
print(a) #[10, 30, 20]----> 값 중복이면 처음 값만 삭제 함



# 리스트에서 특정 값 인덱스 구하기

a = [10, 20, 30, 15, 20, 40]
a.index(20) #1 --> 처음 인덱스만 반환


# 특정 값 개수 구하기
a = [10, 20, 30, 15, 20, 40]
a.count(20) #2






## sort 메서드/ sorted 함수  ===>  정렬 해주는 함수 **
'sort는 메서드 리스트 @@변경@@/ sorted 함수는 정렬된 새 리스트 @@생성@@'
a = [10, 20, 30, 15, 20, 40]
a.sort()    # a의 내용을 변경하여 정렬
print(a) #[10, 15, 20, 20, 30, 40]

b = [10, 20, 30, 15, 20, 40]
print(sorted(b))    #[10, 15, 20, 20, 30, 40]===> 새 리스트 
print(b)  #[10, 20, 30, 15, 20, 40]====> 원본 리스트



##  리스트 모든 요소 삭제하기
# 방법1: clear()
a = [10, 20, 30]
a.clear()
print(a) #[]

# 방법 2: del a[:]
a = [10, 20, 30]
del a[:]
print(a) #[]


## 슬라이스로 조작
a = [10, 20, 30]
a[len(a):] = [500] #a[3:]=[500] ====> len이랑 index 헷갈리지 말기
print(a) #[10, 20, 30, 500]

""" 리스트가 비어 있는지 확인하기 """
seq = []

if not len(seq):
    print("비어 있음")

seq = [14]
if len(seq):
    print("요소 있음")

## 복사
a = [0, 0, 0, 0, 0]
b = a.copy()

print(a is b) #False ==> 값만 복사 한 거라서 F(주소 다름)

print(a == b) #True ==> 값이 똑같아서 T


""" 인덱스와 요소를 함께 출력하기 """
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)

# 0 38
# 1 21
# 2 53
# 3 62
# 4 19

for index, value in enumerate(a):
    print(index + 1, value) #1부터 출력

# 1 38
# 2 21
# 3 53
# 4 62
# 5 19

for index, value in enumerate(a, start=1):
    print(index, value)

# 1 38
# 2 21
# 3 53
# 4 62
# 5 19




""" 가장 작은 수와 가장 큰 수 구하기 """

a = [38, 21, 53, 62, 19]
smallest = a[0]

for i in a:
    if i < smallest:
        smallest = i

print(smallest)

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a)) #map 뒤에 있는 식을 함수식으로 사용. 여기서는 a를 모두 정수처리 하겠다는 의미
print(a) #[1, 2, 3, 4]


# =============================================
# 퀴즈
# ==============================================

"""
1. 리스트 a가 있을 때 다음 중 리스트 a.append(40)과 동작이 같은 것을 모두 고르세요.
a. a.insert(len(a), 40)
b. a[0:] = 40
c. a[len(a):] = 40
d. a[len(a):] = [40]
e. a[-1:] = [40]
===>  a, d

b: 그냥 [40]
c: 리스트 끝에 요소를 추가할 때는 insert(len(a), 값)을 쓰거나 슬라이스 범위에 리스트를 할당
e: 마지막 요소를 덮어씀

40 → 반복 불가 → 에러
[40] → 반복 가능 → 가능



2. 다음 중 리스트의 모든 요소를 삭제하는 메서드를 고르세요.
a. clean
b. remove
c. reverse
d. pop
e. clear

==> e

3. 다음 중 리스트 a의 모든 요소를 출력하는 방법으로 올바른 것을 모두 고르세요.
a. for i in range(len(a)):
       print(a[i])
b. for i in a:
       print(a[i])
c. i = 0
   while i <= len(a):
       print(a[i])
       i += 1
d. i = 0
   while i < len(a):
       print(a[i])
       i += 1
e. for i in a:
       print(i)

=> a, d, e

4. 다음 중 튜플 a에 사용할 수 없는 코드를 고르세요.
a. print(a[:])
b. a.pop()
c. sum(a)
d. a.count(10)
e. min(a)
=> b: 튜플은 불변(immutable)이므로 요소를 삭제하는 pop() 메서드는 사용할 수 없음

5. 리스트 [0, 1, 2, 3, 17, 18, 19]를 만드는 방법으로 올바른 것을 고르세요.
a. [i for i in range(20)]
b. [i for i in range(30) if i < 3 or i > 17]
c. [if i <= 3 or i >= 17 for i in range(20)]
d. [i for i in range(20) if i <= 3 or i >= 17]
e. [i for i if i < 3 or i > 17 in range(20)]
=> d
[식 for 변수 in 반복가능객체 if 조건식]


6. 다음 중 실수가 들어있는 리스트 [4.7, 3.5, 2.9]의 요소를 문자열로 변환하는 방법으로 올바른 것을 고르세요. a는 리스트가 되어야 합니다.
# a. a = str([4.7, 3.5, 2.9])
# b. a = map(str, [4.7, 3.5, 2.9])
# c. a = list(map(str, [4.7, 3.5, 2.9]))
# d. a = list(str, [4.7, 3.5, 2.9])
# e. a = map(int, [4.7, 3.5, 2.9])
=> c

"""





# ============================================
# 연습문제
# ===========================================
#연습문제: 리스트에서 특정 요소만 뽑아내기
# 다음 소스 코드를 완성하여 리스트 a에 들어있는 문자열 중에서 길이가 5인 것들만 리스트 형태로 출력되게 만드세요(리스트 표현식 사용).
# 실행 결과: ['alpha', 'bravo', 'delta', 'hotel', 'india']

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]

print(b)


# 22.10 심사문제: 2의 거듭제곱 리스트 생성하기
# 표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 1~20, 두 번째 입력 값의 범위는 10~30이며 
# 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 첫 번째 정수부터 두 번째 정수까지를 지수로 하는 
# 2의 거듭제곱 리스트를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 
# 단, 리스트의 두 번째 요소와 뒤에서 두 번째 요소는 삭제한 뒤 출력하세요. 출력 결과는 리스트 형태여야 합니다.


start, stop = map(int, input().split())

result = [2 ** i for i in range(start, stop + 1)]
del result[1]      # 두 번째 요소 삭제
del result[-2]     # 뒤에서 두 번째 요소 삭제

print(result)
import numpy as np
import matplotlib.pyplot as plt



# 0. shape, axis =======================================

# np.array([1, 2, 3]).shape--> (3,)=> 1행 3열도 아니고, 3행 1열도 X
# 행/열로 말하려면 2차원으로 reshape 해야 함.


# shape = (판 개수/깊이, 행, 열)
# axis=0 길이 = 첫 번째 숫자
# axis=1 길이 = 두 번째 숫자
# axis=2 길이 = 세 번째 숫자

arr = np.array([1, 2, 3])
print(arr)
print(arr.shape)
print(arr.ndim)

print(arr.reshape(1, 3))
print(arr.reshape(1, 3).shape)

print(arr.reshape(3, 1))
print(arr.reshape(3, 1).shape)

arr3d = np.arange(24).reshape(2, 3, 4)
print(arr3d)
print(arr3d.shape)
print(arr3d[0])
print(arr3d[1])

#  =========================================================
# 1. 요소별 연산 ================================

# 같은 크기의 배열끼리는 같은 위치 원소끼리 연산됨 A * B는 행렬곱이 아니라 원소별 곱셈임

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

print(A + B)
print(A * B)

#  =========================================================

# 2. 1차원 벡터의 내적 =======================================

# np.dot(a, b)는 같은 위치끼리 곱한 뒤 모두 더한다.


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))
print(1*4 + 2*5 + 3*6)
# ========================================================

 
# 3. 2차원 행렬곱 ==========================================

# 2차원 배열에서는 np.dot(), np.matmul(), @ 결과가 같음
# ==> 앞 행렬의 열 개수와 뒤 행렬의 행 개수가 같아야 함
 

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(np.dot(A, B))
print(np.matmul(A, B))
print(A @ B)

# ========================================================


 
#  =========================================================
# 4. 3차원 배열에서 dot과 matmul 차이

# 3차원 이상에서는 np.dot()과 np.matmul()의 결과 shape가 달라질 수 있다.
# matmul 또는 @는 마지막 두 축을 행렬로 보고 계산함

A = np.array([[[1, 2],
               [3, 4]],
              [[5, 6],
               [7, 8]]])

B = np.array([[[9, 10],
               [11, 12]],
              [[13, 14],
               [15, 16]]])

dot_result = np.dot(A, B)
matmul_result = np.matmul(A, B)

print(dot_result)
print(dot_result.shape)

print(matmul_result)
print(matmul_result.shape)

print(A @ B)
#  ========================================================= 

# 5. 외적 Outer Product-----> outer()
 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

outer_result = np.outer(a, b)

print(outer_result)
print(outer_result.shape)

#  =========================================================
# 6. 전치 행렬
# A.T 또는 np.transpose(A) 사용함

A = np.array([[1, 2, 3],
              [4, 5, 6]])

print(A)
print(A.shape)

print(A.T)
print(A.T.shape)

print(np.transpose(A))

#  =========================================================

 
# 7. 역행렬

# np.linalg.inv()=> 역행렬 구함
# np.linalg.det()=> 행렬식 구함
# 행렬식이 0이면 역행렬 존재X
 

matrix = np.array([[1, 2],
                   [3, 4]])

det_matrix = np.linalg.det(matrix)
inv_matrix = np.linalg.inv(matrix)

print(det_matrix)
print(inv_matrix)

#  =========================================================

 
# 8. 배열 정렬

# np.sort(arr)는 정렬된 새 배열을 반환= 원본은 유지
# arr.sort()는 원본 자체를 바꿈

# 9. 2차원 배열 정렬

# axis=1은 행 내부 정렬 /axis=0은 열 내부 정렬 
# axis=None은 전체를 1차원으로 펼친 뒤 정렬함


arr2d = np.array([[3, 1, 6],
                  [0, 7, 4],
                  [5, 3, 2]])

print(np.sort(arr2d, axis=1))
print(np.sort(arr2d, axis=0))
print(np.sort(arr2d, axis=None))

#  =========================================================

# 10. argsort
# np.argsort(arr)는 정렬된 값 자체가 아니라 정렬했을 때 필요한 기존 인덱스를 반환함


arr = np.array([4, 2, 3, 5, 1])
indices = np.argsort(arr)

print(indices)
print(arr[indices])

fruit_array = np.array(["Apple", "Banana", "Cherry", "Grape", "Kiwi"])
price_array = np.array([800, 1000, 900, 950, 700])

price_indices = np.argsort(price_array)[::-1]

print(price_array[price_indices])
print(fruit_array[price_indices])
#  =========================================================

# 11. 배열 병합 vstack, hstack

# vstack=> 2차원 기준으로 위아래로 붙어서 행이 늘어남.
# hstack=> 2차원 기준으로 좌우로 붙어서 열이 늘어남.


a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print(np.vstack([a, b]))
print(np.hstack([a, b]))
#  =========================================================

"""
12. dstack

dstack은 axis=2 방향으로 병합함

1차원 배열을 dstack하면 내부적으로 (N,) -> (1, N, 1) 형태로 바꾼 뒤 axis=2로 붙인다.

그래서 [1,2,3]과 [4,5,6]을 dstack하면 shape는 (1, 3, 2) 
"""

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.dstack((arr1, arr2))

print(result)
print(result.shape)

arr1_3d = arr1.reshape(1, 3, 1)
arr2_3d = arr2.reshape(1, 3, 1)

print(arr1_3d)
print(arr2_3d)
print(np.concatenate((arr1_3d, arr2_3d), axis=2))

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

result = np.dstack((arr1, arr2))

print(result)
print(result.shape)

"""
13. concatenate

np.concatenate()는 axis를 직접 지정해서 병합함
/// 2차원 ////
axis=0이면 위아래 병합/ axis=1이면 좌우 병합/ axis=None이면 1차원으로 펼친 뒤 병합
"""

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print(np.concatenate([a, b], axis=0))
print(np.concatenate([a, b], axis=1))
print(np.concatenate([a, b], axis=None))

"""
14. 병합 조건

- 병합할 축은 크기가 달라도 되지만 병합 안 하는 나머지 축의 shape는 같아야 함

hstack은 axis=1 방향 병합 
vstack은 axis=0 방향 병합 
"""
 
x = np.array([[1, 2, 3],
              [4, 5, 6]])

y = np.array([[7, 8, 9, 10],
              [11, 12, 13, 14]])

print(x.shape)
print(y.shape)

print(np.hstack((x, y)))

 

"""
15. 배열 분할

hsplit은 열 기준으로 나눈다.
vsplit은 행 기준으로 나눈다.
split은 axis를 직접 지정해서 나눈다.
"""

arr = np.arange(12).reshape(3, 4)

print(arr)

print(np.hsplit(arr, 2))
print(np.vsplit(arr, 3))

print(np.split(arr, 2, axis=1))
print(np.split(arr, 3, axis=0))

arr = np.arange(18).reshape(3, 6)

print(arr)
print(np.hsplit(arr, [2, 4]))

"""
16. copy와 view

copy는 복사본을 바꿔도 원본은 안 바뀜
view는 view를 바꾸면 원본도 바뀜
"""

arr = np.array([1, 2, 3, 4, 5])
view_arr = arr.view()

view_arr[0] = 100

print(arr)
print(view_arr)

arr = np.array([1, 2, 3, 4, 5])
copy_arr = arr.copy()

copy_arr[0] = 100

print(arr)
print(copy_arr)

"""
17. 단항 유니버설 함수

ufunc는 배열의 각 원소에 한 번에 적용되는 함수
반복문 없이 원소별 계산 수행함

18. reduce, accumulate, reduceat

reduce는 결과가 하나로 줄어들 때까지 연산한다.
accumulate는 누적 중간 결과를 모두 보여준다.
reduceat은 지정한 인덱스를 기준으로 구간별 reduce를 수행한다.
"""

x = np.arange(1, 6)

print(np.add.reduce(x))
print(np.multiply.reduce(x))
print(np.add.accumulate(x))

arr = np.array([1, 2, 3, 4, 5, 6])

print(np.add.reduceat(arr, [0, 3]))
print(np.multiply.reduceat(arr, [0, 2, 4]))

arr = np.arange(1, 13).reshape(4, 3)

print(arr)
print(np.add.reduceat(arr, [0, 2], axis=0))
print(np.add.reduceat(arr, [0, 2], axis=1))

"""
19. 이항 ufunc와 브로드캐스팅
이항 ufunc는 두 배열을 받아 같은 위치끼리 계산/
브로드캐스팅은 shape가 달라도 규칙이 맞으면 자동 확장되어 계산됨

20. 파일 입출력
- np.save()는 배열 1개를 .npy로 저장 
- np.load()는 저장된 배열을 불러옴

- np.savez()는 여러 배열을 하나의 .npz 파일에 저장함
- np.savez_compressed()는 압축해서 저장
 
- np.savetxt()는 텍스트 파일로 저장
- np.loadtxt()는 텍스트 파일을 읽음
===================================================
"""

# 21. imshow 시각화


data= np.arange(0, 256).reshape((16, 16))

data.size, data.shape

# np.random.seed(0)


data = np.random.rand(16, 16) *100
# np.random.randint(0, 255)
# print(data)
data= np.ceil(data)
# plt.colorbar()
plt.title('16*16')
plt.imshow(data, cmap='coolwarm')
plt.show()
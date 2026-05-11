## =======================================================================
## Iterable 타입: 반복이 가능한 데이터 타입
##              => for~ in 반복문으로 요소
##              => 확인

iterator= [10, 20, 30].__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
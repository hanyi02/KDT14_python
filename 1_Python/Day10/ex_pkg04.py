## ====================================================
##              파이썬 표준 모듈 및 패키지 
## ====================================================
## random 모듈 :  무작위 값 생성 모듈 
## ====================================================

## ----------------------------------------------------
## 모듈 로딩
## ----------------------------------------------------
import random as rd


## ----------------------------------------------------
## 모듈 사용
## ----------------------------------------------------
## random.random()      : 실수 0<= ~ <1
## => 0 이상 1 미만(0<= ~ <1)의 실수를 무작위로 반환
print( rd.random(), rd.random() , rd.random() )


## random.randint(a, b) : 정수 a<= ~ <=b
## => a 이상 b 이하(a<= ~ <=b)의 정수를 무작위 반환
print(rd.randint(1, 2), rd.randint(1, 2), rd.randint(1, 2))



## random.randrange(start, stop, step) : 정수, start<= ~ <stop
## => range()처럼 범위를 정해서 무작위 값 반환
print(rd.randrange(1, 10))     # 1~9
print(rd.randrange(0, 10, 2))  # 0,2,4,6,8 중 하나


## random.uniform(start, stop)  : 실수 , start<= ~ <stop
## => a부터 b 사이의 실수를 무작위로 반환
print(rd.uniform(1, 2), rd.uniform(10, 11), rd.uniform(10, 11))    


## random.choice(순서있는 데이터타입)  
## => 1개 무작위 선택 반환
print(rd.choice([1,2,3]), rd.choice([1,2,3]), rd.choice([1,2,3]))   

## random.choices(순서있는 데이터타입, k=n)  
## => n개 무작위 선택 반환. 중복 가능함
print(rd.choices([1,2,3], k=5))   
print(rd.choices("GoodLuck", k=10)) 

## random.sample(순서있는 데이터타입, k=n)  
## => n개 무작위 선택 반환. 중복 불허!!!
print(rd.sample([1,2,3], k=2))   
print(rd.sample("GoodLuck", k=7))   

print(rd.sample(range(1,46), k=6))   
print(rd.sample(range(1,46), k=6))   
print(rd.sample(range(1,46), k=6))   
print(rd.sample(range(1,46), k=6))   

## random.seed()  
## => 매번 동일한 랜덤값 추출하도록 고정
rd.seed(10)
print("seed 고정")
print(rd.sample(range(1,46), k=6))   
print(rd.sample(range(1,46), k=6))   
print(rd.sample(range(1,46), k=6))   
print(rd.sample(range(1,46), k=6))   
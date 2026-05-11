## ====================================================================
## 변수 - 지역(Local) 변수와 전역(Global) 변수 
## ====================================================================
## -> 지역(Local) 변수 : 함수의 매개변수, 함수 내부에 선언된 변수
##                      함수 호출될 때 메모리에 존재
##                      함수 종료될 때 메모리에서 삭제
##                      함수에서만 사용 가능!!!
##
## -> 전역(Global) 변수 : 파이썬 파일 안에 생성된 변수
##                      파이썬 파일 실행 시에 메모리에 생성    
##                      파이썬 파일 종료 시에 메모리에서 삭제
##                      파인썬 파일 안에서 모두 사용 가능!!!            
## ====================================================================
## --------------------------------------------------------------------
## [예시-01] 지역변수에서 전역변수 사용하기 
## --------------------------------------------------------------------
## Global Variable
num = 100

## Custom Function
def test(a, b):         ## local variable : a, b
    print(a, b, num)    ## use global variable
    

def change(a, b):       ## local variable : a, b
    global num          ## use & change global variable
    num = num * 2       ## change value
    print(a, b, num)    ## use global variable
    
## Run code ==========================================
print("Before num : ", num) 
test(10, 5) 
print("After  num : ", num) 

print(' ----- ')

print("Before num : ", num) 
change(10, 5) 
print("After  num : ", num) 
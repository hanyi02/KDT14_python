## ==============================================================
## 클래스/ 객체/ 인스턴스 
## ==============================================================
## 클래스: 특정 데이터에 대한 속성과 기능을 묶어서 정의한 것
##        새로운 사용자 정의한 데이터 타입

## 객체: 클래스를 기반으로 메모리 힙영역에 저장된 데이터들(힙영역에 있는 객체 덩어리를 묶어서)
## 인스턴스: 힙 영역에 있는 객체 하나하나 (list instance, str instance ...)
## ==============================================================
## --------------------------------------------------------------
## 클래스 목적: 자동차 데이터를 저장하는 타입 
## 클래스 이름: Car 
## 클래스 속성: width, height, length, color, kind, number, user
## 클래스 기능: forward() 전진
##            backward() 후진
##            stop() 정지
##            


# 클래스 명은 대문자로 시작
class Car:
    ## 자동차 인스턴스/ 객체 생성을 위한 메모리 힙영역 스캠 후 메모리 할당 메서드
    ## 메모리 힙 영역 생성된 자동차 인스턴스/ 객체 주소 반환
    ##-> cls: 클래스 정보
    ##-> user, number: 인스턴스 생성 시 전달 데이터
    
    def __new__(cls, user, number):
        print("(1) __new__ 호출")
        instance = super().__new__(cls)
        print("instance id:", id(instance))
        return instance
    
    ## 위에서 반환된 주소가 아래 __init__의 self 인자로 할당됨.

    # 자동차 인스턴스/ 객체를 생성 및 초기화 해주는 매직 매서드
    # 파이썬 시스템에서 자동 호출 실행됨
    def __init__(self, user, number):
        self_value =  int(str(self).split()[-1][:-1], base=16)
        print("(2) __init__() => self : ", self_value) 
        self.user=user
        self.number= number
    
    # 자동차만이 가진 기능 함수==> 매서드
    # 메모리 힙영역에 자동차 인스턴스/ 객체 생성이 되어야만
    # 사용할 수 있는 메더스 
    def forward(self):
        print("forward() 호출")
        print(f"{self.number}가 앞으로 전진한다.")

    def backward(self):
        print("backward() 호출")
        print(f"{self.number}가 후진한다.")

    def stop(self, where):
        print("stop() 호출")
        print(f"{self.user}가 {where}에 정지한다.") #인스턴스가 가지고 있지않은 속성(where)을 사용하려면 매개변수로 추가 하면 된다



## ----------------------------------------------------------------------
## 객체 즉, Car 인스턴스 생성: 변수명= 클래스이름()
##
## -> 생성자 매서드: 클래스 이름()==> 연결==> __init__()
## ----------------------------------------------------------------------

myCar=Car('홍길동', '12가 1212')
yourCar=Car('마징가', '88아 8888')
print(f'myCar id=>', id(myCar))


## 자동차 인스턴스와 메서드 사용
myCar.forward() #self는 인식 안 함
yourCar.forward() #self는 인식 안 함
myCar.stop(where= '운동장')



## 자동차 인스턴스/ 객체 속성 읽기
print("내 자동차 번호: ", myCar.number)
print("내 자동차 소유자: ", myCar.user)
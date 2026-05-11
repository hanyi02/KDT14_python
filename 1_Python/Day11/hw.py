##================================================================
## 사용자 정의 클래스
##================================================================

##-----------------------------------------------------------------
## 사람 클래스 정의
##-----------------------------------------------------------------
## -> 데이터 : 이름, 성별, 키, 몸무게, 나이
## -> 기능/역할 : 개인정보출력, 나이계산, 키/몸무게 변경, BMI 계산
##-----------------------------------------------------------------
## -> 클래스이름 : Person
## -> 클래스속성 : name, gender, height, weight, birth
## -> 클래스함수 : info(), get_age(), set_height(), set_weight(), get_bmi()
##-----------------------------------------------------------------
from datetime import datetime



class Person:
    def __init__(self, name, gender, height, weight, birth):
        self.name=name
        self.gender=gender
        self.height=height
        self.weight=weight
        self.birth= birth  #"YYYY-MM-DD" 형식


    def info(self):
        print(f"이름: {self.name}")
        print(f"성별: {self.gender}")
        print(f"키: {self.height}cm")
        print(f"몸무게: {self.weight}kg")
        print(f"생일: {self.birth}")
        print(f"나이: {self.get_age()}세")

    # 나이 계산
    def get_age(self):
        today= datetime.today()
        birth_date= datetime.strptime(self.birth, "%Y-%m-%d")

        age= today.year- birth_date.year

        # 생일 아직 안 지났으면 -1
        if (today.month, today.day)< (birth_date.month, birth_date.day):
            age-= 1

        return age

    # 키 변경
    def set_height(self, height):
        self.height= height

    # 몸무게 변경
    def set_weight(self, weight):
        self.weight = weight

    # BMI 계산
    def get_bmi(self):
        height_m= self.height/ 100
        bmi= self.weight/ (height_m** 2)
        return round(bmi, 2)
    



    ## 사람이면 하는 행동

    def forward(self):
        print("forward() 호출")
        print(f"{self.name}이/가 앞으로 전진한다.")

    def backward(self):
        print("backward() 호출")
        print(f"{self.name}이/가 후진한다.")

    def stop(self, where):
        print("stop() 호출")
        print(f"{self.name}이/가 {where}에 정지한다.")


me = Person("홍길동", "남", 175, 70, "2000-05-10")

me.backward()
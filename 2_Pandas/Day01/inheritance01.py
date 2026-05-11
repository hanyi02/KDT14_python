## ==================================================================
##                          상속 (inheritance)
##  -> 말 그대로 물려받은 기능을 유지하되 다른 기능을 더 추가해 사용할 수 있는 방법
##
##  기반 클래스(base class): 기능을 물려주는 클래스
##      -> 부모 클래스(parent class)
##      -> 슈퍼 클래스(parent class)
##  파생 클래스(derived class): 상속 받아 새로 만들어진 클래스
##      -> 자식 클래스(child class)
##      -> 서브 클래스(sub class)
## ==================================================================

# ------------------------------------
# 클래스 상속하기 
# ------------------------------------
class Person:
    def greeting(self):
        print("안녕하세요")

class Student(Person):  # 여기서 파생 클래스는 Student, 기반 클래스는 Person
    def study(self):
        print("공부하기")

james= Student()
james.greeting() # 기반 클래스 Person 매서드 호출
james.study() # 파생 클래스 Student에 추가된 study 매서드

# 상속 확인하려면 
issubclass(Student, Person) 

# ------------------------------------
# 상속 관계/ 포함 관계
# ------------------------------------

# Person과 Student 관계는 동등한 관계--> 상속, is-a 관계

## 포함관계 --> has-a 관계
## 속성에 인스턴스를 넣어 관리하므로 Personlist가 Person을 포함하고 있음
class Person:
    def greeting(self):
        print('안녕하세요')

class PersonList:
    def __init__(self): # ==> 속성 만들 때는 __init__ 매서드 안에서 self.속성에 값을 할당
        self.person_list=[] # 리스트 속성에 Person 인스턴스 넣어서 사용
    
    def append_person(self, person):
        self.person_list.append(person)


## 기반 클래스의 속성 사용
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello='안녕하세요'

class Student(Person): # 상속받음=> 파생클래스 
    def __init__(self):
        print('Student__init__')
        self.school='파이썬 코딩 도장'

james= Student()
print(james.school)
print(james.hello) # 파생클래스에서 기반클래스의 속성 호출=> 에러------- Student객체는 hello 속성이 없음

## 상속관계일 때 부모클래스의 매서드 호출은 되지만, 속성 호출은 안 됨

# ------------------------------------
# super()로 기반 클래스 초기화하기
# ------------------------------------
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello='안녕하세요'

class Student(Person): # 상속받음=> 파생클래스 
    def __init__(self):
        print('Student__init__')
        super().__init__() #super()로 기반클래스의 __init__ 호출
        # super() 사용함으로써 기반클래스가 초기화돼서 속성이 만들어짐
        self.school='파이썬 코딩 도장'

james= Student()
print(james.school)
print(james.hello)



# ------------------------------------
# super()로 기반 클래스 초기화하기
# ------------------------------------

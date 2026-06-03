
## ----------------------------------------------------------
## 클래스이름 : Point
## 클래스속성 : x, y          --- 위치. 좌표값  
##            color         --- 색상
##            radius        --- 반지름
##            shape         --- 형태. [기] 동그라미
## 클래스기능 : 정보 출력 기능  --- print_info()
##            점 그리기 기능  --- drawing()
## ----------------------------------------------------------
class Point:
    # -----------------------
    # 클래스 변수/속성/필드
    # -----------------------    
    
    # -----------------------
    # 인스턴스 변수/속성/필드 초기화 매직 메서드
    # -----------------------
    def __init__(self, x, y, color, radius, shape='동그라미'):
        self.x = x
        self.y = y 
        self.color = color
        self.radius = radius
        self.shape = shape

    # -----------------------
    # 인스턴스 메서드 
    # -----------------------
    def drawing(self):
        print(f'({self.x},{self.y})좌표에 {self.shape} 그리기')

    def print_info(self):
        print('[Point 정보]---')
        print(f'형  태 : {self.shape}')
        print(f'좌  표 : ({self.x},{self.y}) ')
        print(f'색  상 : {self.color}')
        print(f'반지름 : {self.radius}')



## ----------------------------------------------------------
## 클래스이름 : Point3D
## 클래스속성 : x, y, z       --- 위치. 좌표값  
##            color         --- 색상
##            radius        --- 반지름
##            shape         --- 형태. [기] 동그라미
## 클래스기능 : 정보 출력 기능  --- print_info()
##            점 그리기 기능  --- drawing()
## ----------------------------------------------------------
class Point3D:
    # -----------------------
    # 클래스 변수/속성/필드
    # -----------------------    
    
    # -----------------------
    # 인스턴스 변수/속성/필드 초기화 매직 메서드
    # -----------------------
    def __init__(self, x, y, z, color, radius, shape='동그라미'):
        self.x = x
        self.y = y 
        self.z = z
        self.color = color
        self.radius = radius
        self.shape = shape

    # -----------------------
    # 인스턴스 메서드 
    # -----------------------
    def drawing(self):
        print(f'({self.x},{self.y}, {self.z})좌표에 {self.shape} 그리기')

    def print_info(self):
        print('[Point 정보]---')
        print(f'형  태 : {self.shape}')
        print(f'좌  표 : ({self.x},{self.y}, {self.z}) ')
        print(f'색  상 : {self.color}')
        print(f'반지름 : {self.radius}')
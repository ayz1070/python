class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2 

    def getArea(self):
        return abs(self.x1-self.x2)*abs(self.y1-self.y2)
    
    def getPerimeter(self):
        return (abs(self.x1-self.x2) + abs(self.y1-self.y2))*2
    
    def show(self):
        print(f"좌측 상단 꼭지점이 ({self.x1},{self.y1})이고 우측 상단 꼭지점이 ({self.x2},{self.y2})인 사각형입니다.")


r1 = Rectangle(5,5,20,10)
a = r1.getArea()
p=r1.getPerimeter()

r1.show()
print(f"넓이는 {a}, 둘레는 {p}")

class Shape:
    def __init__(self):
        pass
    def draw(self):
        print("Shape")
    def getArea(self):
        return 0
class Circle(Shape):
    def __init__(self, radius=10):
        super().__init__()
        self.radius = radius
    def draw(self):
        print("Circle")
    def getArea(self):
        return 3.14*self.radius*self.radius    #오버라이딩 = 다시 정의
    
c1 = Circle(10)
c1.draw()
print("원의 면적:", c1.getArea())


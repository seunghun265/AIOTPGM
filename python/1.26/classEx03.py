class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        return 3.14 *self.radius **2
    
    def getPrimeter(self):
        return 2 *3.14 *self.radius
    def prtCircleInfo(self):
        print(f"반지름이 {self.radius}인 원의 면적은{self.getArea()}이고 둘레는 {self.getPrimeter()}입니다")


c1 = Circle(6) 
c1.prtCircleInfo()#self = c1, c2
print(f"반지름이 {c1.radius}이 원의 면적은 {c1.getArea()}이고 둘레는 {c1.getPrimeter()}입니다.")
c2 = Circle(12)
print(f"반지름이 {c2.radius}이 원의 면적은 {c2.getArea()}이고 둘레는 {c2.getPrimeter()}입니다.")


class Rectangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def setBase(self,base):
        self.base = base
    def getBase(self):
        return self.base
    def setHeight(self, height):
        self.height = height
    def getHeight(self):
        return self.height
    
rect1 = Rectangle(30,30)
rect1.base = 10        
rect1.setBase(10)     #두가지 방법다 가능

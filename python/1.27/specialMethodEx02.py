class Rectangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def __add__(self,other):
        return Rectangle(self.base + other.base, self.height + other. height)
    
    def __str__(self):
        return f"({self.base},{self.height})"
    
    def __eq__(self,other):                          #면적이 같은지 판별할때 eq 사용
        return self.base * self.height == other.base *other.height
    
    #객체끼리 연산할수 있는 특수 메소드 필요 ^
    
    
r1 = Rectangle(4,5)
r2 = Rectangle(5,4) #base=4,height=2
if r1==r2:
    print("두 사각형의 면적은 같습니다")
else :
    print("두 사각형의 면적은 같지 않습니다")
#객체 끼리 더하고 싶으면? 
r3 = r1+r2
print(r1,r2,r3)   #(8,7)이만들어짐

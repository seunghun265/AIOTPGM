def mulReturn():
    return 1,2

x,y = mulReturn()
print(f"x= {x},y= {y}")
print(mulReturn())   #1,2 리턴이 두개라고 생각하지만 튜플이다 (1,2) 하나의 튜플로 전달

x=("abcd",)
print(x)

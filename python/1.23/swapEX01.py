def swapFunc(x, y) :
    temp = x
    x = y
    y = temp
    return x, y

num1 = 1
num2 = 2
print(f"num1 = {num1}, num2 = {num2}")
num1, num2 = swapFunc(num1,num2)
print(f"num1 = {num1}, num2 = {num2}")
num1, num2 = swapFunc(5,6)
print(f"num1 = {num1}, num2 = {num2}")

x = 1
y = 2
print(f"x={x},y={y}")
x, y = y, x #두 변수값을 바꾸는 코드 (파이썬에서만 가능,굳이 temp 설정할 필요 x)
print(f"x={x},y={y}")
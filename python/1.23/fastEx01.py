# def greet(name, msg="별일없죠?"):
#     print("안녕 ", name + ', ' + msg)
    
# greet("영희")
# greet("영희","안녕하세요")

# sub(z=1,y=2,x=1)     #디폴트 인수
# sub(1,2,3)          #positional argument


def add(*numbers) :
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

print(f'sum = {add(10)}, {add(10,20)}, {add(10,20,30)}')

def circleArea(radius) :
    area = 3.141592 * radius ** 2
    return area

def triangleArea(base,height) :
    area = 0.5 * base * height
    return area

def rectangle(base,height) :
    area base * height
    return area

while True :
    choice = int(input("1.원의 면적\n2.삼각형의 면적\n,3.사각형의면적\n0.종료\n선택(1,2,3,0)"))
    if choice == 1 :
        radius = int(input("원의 반지름 입력 :"))
        area = circleArea(radius)
        print(f"반지름이 {radius}인 원의 면적은 {area}입니다.")
    
    if choice == 2 :
        base = int(input("삼각형의 밑변을 입력하세요 : "))
        height = int(input("삼각형의 높이를 입력하세요 : "))
        area = triangle(base,height)
        print(f"반지금이 {base}이고 높이가 {height}인 삼각형의 면적은 {area}입니다")
        
    
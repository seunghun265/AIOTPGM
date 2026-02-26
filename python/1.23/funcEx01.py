def circleArea(radius) :
    area = 3.141592 * radius ** 2
    return area

def rectangleArea(base, height) :
    area = base * height
    return area

def triangleArea(base, height) :
    area = 0.5 * base * height
    return area

while True :
    choice = int(input("1. 원의 면적\n2.삼각형의 면적\n3.사각형의 면적 \n,0.종료\n 선택(1,2,3,0) :"))
    if choice == 1:
        radius = int(input("원의 반지름 입력 : "))
        area = circleArea(radius)
        print(f"반지름이 {radius}인 원의 면적은 {area} 입니다.")
    elif choice == 2:
        base = int(input("삼각형의 밑변 입력 : "))
        height = int(input("삼각형의 높이 입력 :"))
        area = triangleArea(base, height)
        print(f"밑변이 {base}이고, 높이가 {height}인 삼각형의 면적은 {area}입니다.")
    elif choice == 3:
        base = int(input("사각형의 밑변 입력 : "))
        height = int(input("사격형의 높이 입력 :"))
        area = rectangleArea(base, height)
        print(f"밑변이 {base}이고, 높이가 {height}인 사각형의 면적은 {area}입니다.")
    elif choice == 0:
        break
    else:
        print("1,2,3,0중에 하나를 입력하세요")
    
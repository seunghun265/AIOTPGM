try:
    year = int(input("년도 입력 : "))
    
    if year < 1:
        print("1 이상의 년도를 입력해주세요.")
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year}는 윤년입니다.")
    else:
        print(f"{year}는 평년(common year)입니다.")
except ValueError:
    print("올바른 숫자를 입력해주세요.")
    
    
    
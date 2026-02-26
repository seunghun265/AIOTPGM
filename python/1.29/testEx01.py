while True:
    try:
        numerator = int(input("분자 입력 : "))
        denominator = int(input("분모 입력 : "))
    except ZeroDivisionError:
        print("오류: 분모는 0이 될 수 없습니다! 다시 입력하세요.")
        continue
    try:   
        quotient = numerator // denominator
        remainder = numerator % denominator

        print(f"{numerator}/{denominator} = {numerator/denominator}")
        print(f"몫 quotient = {quotient}, 나머지 remainder = {remainder}")
        break  # 정상 입력이면 반복 종료
    except ValueError:
        print("오류: 숫자를 입력해야 합니다! 다시 입력하세요.")



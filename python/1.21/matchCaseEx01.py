score = int(input("점수 입력 : "))

match score :
    case 100 :
        print("A 학점")
    case 90 :
        print("B 학점")
    case 80 :
        print("C 학점")
    case 70 :
        print("D 학점")
    case 60 :
        print("E 학점")
    case _:
        print("F 학점")
        
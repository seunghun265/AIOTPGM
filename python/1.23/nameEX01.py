def nameAge():
    name = input("이름 :")
    age = input("나이 :")
    return name, age

a,b = nameAge()
print(f"이름은 {a}이고 나이는{b}살 입니다.")
class Student :
    def __init__(self, name,age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
std1 = Student("홍길동",500)
std2 = Student("강감찬",1200)

print(f"{std1.getName()}님의 나이는{std1.getAge()}입니다")    #__는 클래스 내부에서만 사용가능

# 변수는 전부 차단해라 private로 하지만 외부에서 사용하려면 set, get 를사용해서 메소드를 만들어줘라

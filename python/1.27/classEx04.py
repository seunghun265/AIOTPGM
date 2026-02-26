class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(self.name, self.age)
        
class Student:
    def __init__(self,id):
        self.id = id

    def getId(self):
        return self.id

class CollegeStudent(Person,Student):
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)          #하나만 있을때는 super 사용했고 두개 이상일경우 지칭 해줘야한다
        Student.__init__(self,id)
        
cs1 = CollegeStudent("홍길동", 500, 123456798)
cs1.show()
print(cs1.getId())    
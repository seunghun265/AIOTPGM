# class Person:
#     def __init__(self,name,socNumber):
#         self.name = name
#         self.socNumber = socNumber

# class Student(Person):
#     UNDERGRADUATE = 0                   #모든 객체 공유
#     POSTGRADUATE = 0
#     def __init__(self,name,socNumber,studentType):
#         super().__init__(name,socNumber)
#         self.studentType = studentType
#         self.gpa = 0                                      #평점
#         self.classes = []                               #수강과목
#     def enrollCourse(self,course):                      #수강 과목 추가가능
#         self.classes.append(course)
#     def __str__(self):
#         return f"\n이름={self.name}\n주민번호={self.socNumber}\n수강과목={str(self.classes)}\n평점={self.gpa}" 
    
# class Teacher(Person):
#     def __init__(self,name,socNumber):
#         super().__init__(name,socNumber)
#         self.courses = []                               #강의 과목
#         self.salary = 3000000
#     def assignTeaching (self,course):                   #강의 과목 추가가능
#         self.courses.append(course)
#     def __str__(self):
#         return f"\n이름={self.name}\n주민번호={self.socNumber}\n강의과목={str(self.courses)}\n월급={self.salary}" 

# s1 = Student("홍길동","123456-78946513",Student.UNDERGRADUATE)
# s1.enrollCourse("파이썬프로그래밍")
# s1.enrollCourse("자료구조")
# print(s1)
# t1 = Teacher("김길동","1235-14124")
# t1.assignTeaching("파이썬 프로그래민")
# t1.assignTeaching("자료구조")
# print(t1)


class Person:
    def __init__(self,name,socNumber):
        self.name = name
        self.socNumber = socNumber

class Student(Person):
    UNDERGRADUATE = 0
    POSTGRADUATE = 0
    def __init__(self,name, socNumber, studentType):
    super().__init__(name, socNumber, studentType)
    self.studentType = studentType
    self.gpa = 0 
    self.classes = []
    def enrollCourse(self,course):
        self.classes.append(course)
    def __str__(self):
        return f"이름={self.name}\n주민번호={self.socNumber}\n평점={self.gpa}\n수강과목={self.classes}"
    
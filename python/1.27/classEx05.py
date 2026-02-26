class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        return self.salary
    def displayInfo(self):
        return f"{self.name}님의 월급은{self.salary}입니다."
    
class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
    
    def getSalary(self):
        return super().getSalary() + self.bonus
    def displayInfo(self):
        return f"{self.name}님의 월급은{self.salary}이고 보너스는 {self.bonus}이고 합쳐서 {self.salary+self.bonus}입니다."
emp1 = Employee("홍길동",500)
man1 = Manager("강감찬",500,50)
print(emp1.displayInfo())
print(man1.displayInfo())


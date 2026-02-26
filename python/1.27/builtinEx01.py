class Person:
    def __init__(self,name,phone,addr,age):
        self.name = name
        self.phone = phone
        self.addr = addr
        self.age = age
    def __repr__(self):
        return f"<{self.name},{self.phone},{self.addr},{self.age}>"



p1 = Person("천길동","123-456","우산국",3)
p2 = Person("강길동","1253-456","정산국",2)
p3 = Person("한길동","12543-456","한산국",1)
personList = [p1,p2,p3]
for i in personList:
    print(i)
    
def keyName(person):
    return person.name
print(sorted(personList,key=keyName))

list1 = [3,4,5,2,1,8,18]

print(list1)
list2 = list1          #list1은 1번에 정의된 리스트의 ㅜ소를 가지고 있고, list2도같은 주소를 가짐
print(list2)
list1[0] = 100
print(list1)
print(list2)
list3 = list(list1) #list3는 새로운 주소에 list1이 가지고 있는 리스트를 만들고 그 주소를 가짐
print(list1)
print(list3)
list1[1] = 200
print(list1)
print(list3)

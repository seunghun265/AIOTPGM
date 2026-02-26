capitals ={"Korea":"Seoul","USA":"Washington","UK":"London "}

for k in capitals:             #k에 key값이들어감
    print(capitals[k])

for k in capitals.keys():           #키 값 함수
    print(k)
    
for v in capitals.values():                #벨류값 함수
    print(v)
    
for k, v in capitals.items():   #items 함수 사용하면 키 벨류 동시에 가져올수있슴
    print(k, v)

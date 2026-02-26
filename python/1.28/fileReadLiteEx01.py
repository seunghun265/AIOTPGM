counter = [0] * 26 
inFile = open("0128/mobydick.txt","r")
ch = inFile.read(1)                #1개씩 읽기
while ch != "":
    ch = ch.upper()            #무조건 대문자로 변경
    if "A" <= ch <= "Z":
        i = ord(ch) - ord("A")
        counter[i] += 1
    ch = inFile.read(1)
inFile.close()   
print(counter)

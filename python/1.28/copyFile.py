inFile = open("develop.png", "rb")                          #텍스트 파일 아니라서 b붙여야됨
outFile = open("associ.png", "wb")

while True:
    copyBuffer = inFile.read(1024)                      #읽어와서 copyBuffer에 넣어줘
    if not copyBuffer:                             #아무것도 없으면 not 이니까 true 로 break됨
        break
    outFile.write(copyBuffer)
    
inFile.close()
outFile.close()
print(f"{inFile} 파일을 {outFile}로 복사 했습니다")

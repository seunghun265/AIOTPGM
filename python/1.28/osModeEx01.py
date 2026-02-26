import os

cwd = os.getcwd()
print(cwd)                        #cwd or pwd 사용
files= os.listdir()          #작업중인 모든 디렉터파일 불러옴
for name in files:
    if name.endswith(".txt"):                    #os.path.isfile(name)  <경로안에 파일이 있는지확인할때
        print(name)
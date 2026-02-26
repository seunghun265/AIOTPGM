# 파일이름과 문자열을 입력받고, 파일이 있으면 그 파일 안에 문자열이 있는지 판별하여,
# 파일이름과 해당 문자열을 가진 라인을 출력하는 프로그램을 작성하시오.
# # 파일 이름 : input.txt
# 문자열 : 홍길동
# input.txt : 홍길동
# 파일이름 : input.txt
# 문자열 : 장길동
# input.txt : 해당 문자열 없음
# 파일 이름 : inoutput.txt
# 문자열 : 홍길동
# inoutput.txt 파일이 없습니다.

import os
print(os.getcwd())

filename = input("파일 이름 : ")
target = input("문자열 : ")


if not os.path.isfile(filename):                                #파일존재여부 확인
    print(f"{filename} 파일이 없습니다.")
else:
    found = False

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if target in line:
                print(f"{filename} : {line}")
                found = True

    if not found:                                               #문자열이 없는경우
        print(f"{filename} : 해당 문자열 없음")

    
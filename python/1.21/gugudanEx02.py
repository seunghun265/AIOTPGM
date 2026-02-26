#단을 입력 받아 해당 단을 출력하는 프로그램 작성
#0을 입력하기 전까지 계속 실행

while True:
    dan = int(input("단 입력(0을 입력하면 종료) :"))
    if dan == 0:
        break
    for i in range(1, 10):
        print(f"{dan}*{i} = {dan*i}")
    
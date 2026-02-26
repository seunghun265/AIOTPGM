while True :
    n=int(input("라인 수를 입력:"))
    if n == 0 :
        break
    for i in range(1,n+1):
        print("*" * i)
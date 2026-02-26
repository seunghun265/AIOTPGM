def fib(n):
    # 종료 조건 (base case)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # 재귀 호출
    else:
        return fib(n-1) + fib(n-2)

number = fib(50)
print(number)

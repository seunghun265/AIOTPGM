# myList = [1,2,3,4,5]
# myList[4] = 6
# print(myList[0])
# print(myList[-1])

# for i in range(10,50,2):
#     print(i)
    
# # 1부터 100까지의 합을 구하는 프로그램 
# # 화면에 1부터 100까지의 수 중에 짝수들의 합과 홀수들의 합을 출력하세요
# oddSum = 0
# evenSum = 0

# for i in range(1,101) : 
#     if i %2 == 0 :
#         evenSum = evenSum + i 
#     else:
#         oddSum = oddSum + i

    
# print(f"1부터 100까지의 수 중에 홀수들의 합 = {oddSum} 입니다.")
# print(f"1부터 100까지의 수 중에 짝수들의 합 = {evenSum} 입니다.")
# oddSum = 0
# evenSum = 0

# for i in range(1,101) :
#     if i %2 == 0 :
#         evenSum = evenSum + i
#     else :
#         oddSum = oddSum + i
        
# print(f"1부터 100까지의 수중에 홀수 들의 합은 {oddSum}입니다")
# print(f"1부터 100까지의 수중에 짝수들의 합은{evenSum}입니다") 

# 1부터 100까지 3배수 의 갯수와 합계는?
# sum = 0
# count = 0

# for i in range(1,101) :
#     if i %3 == 0 :
#         count += 1
#         sum += i

# print(f"1부터 100까지의 수 중에 3의 배수는 {count}개 있습니다")
# print(f"1부터 100까지의 수 중에 3의 배수들의 합 = {sum}입니다")

sum = 0
count = 0

for i in range(1,101) :
    sum += i
    if sum >3000:
        break

print(f"1부터 100까지의 수 중에 3의 배수는 {count}개 있습니다")
print(f"1부터 100까지의 수 중에 3의 배수들의 합 = {sum}입니다")
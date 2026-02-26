def sumtwoDimList(numbers):
    total = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[0])):
            total += numbers[i][j]
    return total

# def sumtwoDimList(thrs):  # 3차원일경우
#     total = 0
#     for i in range(len(thrs)):
#         for j in range(len(thrs[0])):
#             for k in range(len(thrs[0][0])):
#             total += thrs[i][j][k]
#     return total


s = [[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15]]

rows = len(s)
cols = len(s[0])
print(rows)
print(cols)
for i in range(rows):
    for j in range(cols):
        print(s[i][j], end=".")
    print()

print(sumtwoDimList(s))


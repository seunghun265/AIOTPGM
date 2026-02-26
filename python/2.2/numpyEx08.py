import numpy as np

# 1️⃣ 실수로 이루어진 5x6 행렬 생성
data = np.random.rand(5,6)   # 0~1 사이 실수
print("원본 데이터:")
print(data)

# 1. 전체의 최댓값
print("\n1. 전체의 최댓값")
print(np.max(data))

# 2. 각 행의 합
print("\n2. 각 행의 합")
print(np.sum(data, axis=1))             #axis = 1 행 기준

# 3. 각 행의 최댓값
print("\n3. 각 행의 최댓값")
print(np.max(data, axis=1))

# 4. 각 열의 평균
print("\n4. 각 열의 평균")
print(np.mean(data, axis=0))           #axis = 0 열 기준

# 5. 각 열의 최솟값
print("\n5. 각 열의 최솟값")
print(np.min(data, axis=0))

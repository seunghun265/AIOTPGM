import numpy as np

def mat_access1(mat):                 # 원소 직접 접근 방법
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat[i, j]             # 원소 접근
            mat[i, j] = k * 2          # 원소 변경


def mat_access2(mat):                 # item(), itemset() 함수 사용
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat.item(i, j)        # 원소 접근
            mat[i, j] = k * 2         # 원소 변경,  itemset()이 삭제됨


mat1 = np.arange(10).reshape(2, 5)     # 0~9 생성 후 2x5 행렬
mat2 = np.arange(10).reshape(2, 5)

print("원소 처리 전:\n%s\n" % mat1)
mat_access1(mat1)
print("원소 처리 후:\n%s\n" % mat1)

print("원소 처리 전:\n%s\n" % mat2)
mat_access2(mat2)
print("원소 처리 후:\n%s" % mat2)

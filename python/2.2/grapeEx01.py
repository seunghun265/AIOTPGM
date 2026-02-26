import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D 그래프 사용

# 3차원축(axis) 생성
axis = plt.axes(projection='3d')

# 3차원 데이터 생성
Z = np.linspace(0, 1, 100)
X = Z * np.sin(30 * Z)
Y = Z * np.cos(30 * Z)

# 3차원 그래프 그리기
axis.plot3D(X, Y, Z)

# 그래프 표시
plt.show()

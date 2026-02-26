from sklearn import datasets
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
import numpy as np

# 데이터셋 읽기
digit = datasets.load_digits()

# 훈련 집합 / 테스트 집합 분할
x_train, x_test, y_train, y_test = train_test_split(
    digit.data, digit.target, train_size=0.6
)

# Perceptron 모델 생성
p = Perceptron(max_iter=1000, eta0=0.001, verbose=0)

# 모델 학습
p.fit(x_train, y_train)

# 테스트 집합으로 예측
res = p.predict(x_test)

# 혼동 행렬 생성
conf = np.zeros((10, 10), dtype=int)
for i in range(len(res)):
    conf[y_test[i]][res[i]] += 1

print("혼동 행렬:")
print(conf)

# 정확도 계산
no_correct = 0
for i in range(10):
    no_correct += conf[i][i]

accuracy = no_correct / len(res)
print("테스트 집합에 대한 정확률은", accuracy * 100, "% 입니다.")

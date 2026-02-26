import tensorflow as tf
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

# Dense 레이어
dense = Dense(units=1, input_shape=[1])

# 모델
model = Sequential([dense])

# 컴파일
model.compile(optimizer='sgd', loss='mean_squared_error')

# 학습 데이터
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# 학습
model.fit(xs, ys, epochs=500, verbose=0)

# 예측 (2차원 배열 필수)
print(model.predict(np.array([[10.0]])))

# 가중치 확인
print("신경망이 학습한 것:", dense.get_weights())
print("신경망이 학습한 것:", model.layers[0].get_weights())

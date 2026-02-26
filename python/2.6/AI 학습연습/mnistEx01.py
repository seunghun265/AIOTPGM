## ✅ Fashion MNIST 코드 정리 (노션 필기용 · 오류 없는 정석)
## 📌 전체 코드 (정리본)

import tensorflow as tf

# 1️⃣ 데이터 로드
fashion_mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = fashion_mnist.load_data()

# 2️⃣ 데이터 정규화 (0~255 → 0~1)
training_images = training_images / 255.0
test_images = test_images / 255.0

# 3️⃣ 모델 정의
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),   # 입력층
    tf.keras.layers.Dense(128, activation='relu'),   # 은닉층
    tf.keras.layers.Dense(10, activation='softmax')  # 출력층
])

# 4️⃣ 모델 컴파일
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 5️⃣ 모델 학습
model.fit(training_images, training_labels, epochs=5)

# 6️⃣ 모델 평가
model.evaluate(test_images, test_labels)

# 7️⃣ 예측
classifications = model.predict(test_images)

print(classifications[0])
print(test_labels[0])


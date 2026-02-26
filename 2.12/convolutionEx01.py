import tensorflow as tf

# 데이터 로드
data = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = data.load_data()

# 데이터 전처리
training_images = training_images.reshape(60000, 28, 28, 1)
training_images = training_images / 255.0

test_images = test_images.reshape(10000, 28, 28, 1)
test_images = test_images / 255.0

# CNN 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(
        32, (3, 3),
        activation='relu',
        input_shape=(28, 28, 1)
    ),
    tf.keras.layers.MaxPooling2D((2, 2)),

    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),  #커널(필터)적용, 주로 3x3,5,5 적용, 32개적용
    tf.keras.layers.MaxPooling2D((2, 2)),   #최대값풀링
    tf.keras.layers.Dropout(0.25),    #1/4 선을 뺌 
    tf.keras.layers.Flatten(),        #1차원으로 만듬
    tf.keras.layers.Dense(128, activation='relu'),         #활성함수 렐루
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 모델 구조 확인
model.summary()

# 모델 컴파일
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 모델 학습
model.fit(
    training_images,
    training_labels,
    epochs=50
)

# 모델 평가
model.evaluate(test_images, test_labels)

# 예측 수행
classifications = model.predict(test_images)

# 첫 번째 테스트 이미지 결과 확인
print(classifications[0])
print(test_labels[0])

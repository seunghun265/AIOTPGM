import tensorflow as tf
import urllib.request
import zipfile
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop

# ===============================
# 1️⃣ 학습 데이터 다운로드
# ===============================
url = "https://storage.googleapis.com/learning-datasets/horse-or-human.zip"
file_name = "horse-or-human.zip"
training_dir = "horse-or-human/training/"

urllib.request.urlretrieve(url, file_name)

zip_ref = zipfile.ZipFile(file_name, "r")
zip_ref.extractall(training_dir)
zip_ref.close()

# ===============================
# 2️⃣ 이미지 데이터 제너레이터
# ===============================
train_datagen = ImageDataGenerator(rescale=1/255)

train_generator = train_datagen.flow_from_directory(
    training_dir,
    target_size=(300, 300),
    batch_size=32,
    class_mode='binary'
)

# ===============================
# 3️⃣ CNN 모델 구성
# ===============================
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu',
                           input_shape=(300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()

# ===============================
# 4️⃣ 모델 컴파일
# ===============================
model.compile(
    loss='binary_crossentropy',
    optimizer=RMSprop(learning_rate=0.001),
    metrics=['accuracy']
)

# ===============================
# 5️⃣ 모델 학습
# ===============================
model.fit(
    train_generator,
    epochs=10
)
import sys
# 코랩을 사용중인지확인합니다.
if 'google.colab' in sys.modules:
    from google.colab import files
    uploaded = files.upload()
    sample_images = ['/content/' + fn for fn in uploaded.keys()]
    # 업로드된 파일이없으면깃허브에서다운로드합니다.
    if len(uploaded) < 1:
        import gdown
    base_url = 'https://github.com/rickiepark/aiml4coders/raw/main/ch03/'
    for i in range(1,4):
        gdown.download(base_url + 'hh_image_{}.jpg'.format(i))
    sample_images = ['/content/hh_image_{}.jpg'.format(i) for i in range(1,4)]
# 로컬 컴퓨터면ch03 폴더에 있는 이미지를사용합니다.
else:
    sample_images = ['hh_image_{}.jpg'.format(i) for i in range(1,4)]


# ===============================
# 6️⃣ 검증 데이터 다운로드
# ===============================
validation_url = "https://storage.googleapis.com/learning-datasets/validation-horse-or-human.zip"
validation_file_name = "validation-horse-or-human.zip"
validation_dir = "horse-or-human/validation/"

urllib.request.urlretrieve(validation_url, validation_file_name)

zip_ref = zipfile.ZipFile(validation_file_name, "r")
zip_ref.extractall(validation_dir)
zip_ref.close()

validation_datagen = ImageDataGenerator(rescale=1/255)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(300, 300),
    batch_size=32,
    class_mode='binary'
)

# ===============================
# 7️⃣ 검증 포함 재학습
# ===============================
model.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator
)

model.save("horse_human_model.h5")   #훈련 저장
# ===============================
# 8️⃣ 개별 이미지 예측
# ===============================
import os

horse_dir = "horse-or-human/validation/horses"
human_dir = "horse-or-human/validation/humans"

sample_images = [
    os.path.join(horse_dir, os.listdir(horse_dir)[0]),
    os.path.join(human_dir, os.listdir(human_dir)[0])
]


for fn in sample_images:
    plt.imshow(mpimg.imread(fn))
    plt.axis('off')
    plt.show()

    img = tf.keras.utils.load_img(fn, target_size=(300, 300))
    x = tf.keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    prediction = model.predict(x)[0][0]
    print("모델 출력:", prediction)

    if prediction > 0.5:
        print(fn, "→ 사람입니다.")
    else:
        print(fn, "→ 말입니다.")

    print("--------------------")

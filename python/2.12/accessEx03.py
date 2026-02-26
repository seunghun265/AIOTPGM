import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# Windows 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"   # 맑은 고딕
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# ------------------------------
# 픽셀 처리 함수들
# ------------------------------

def pixel_access1(image):
    image1 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i, j]
            image1[i, j] = 255 - pixel
    return image1


def pixel_access2(image):
    image2 = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image.item(i, j)
            image2[i, j] = 255 - pixel
    return image2


def pixel_access3(image):
    lut = [255 - i for i in range(256)]
    lut = np.array(lut, np.uint8)
    image3 = lut[image]
    return image3


def pixel_access4(image):   # OpenCV 함수
    image4 = cv2.subtract(255, image)
    return image4


def pixel_access5(image):   # NumPy ndarray 연산
    image5 = 255 - image
    return image5


# ------------------------------
# 영상 읽기
# ------------------------------
image = cv2.imread("images/bright.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")


# ------------------------------
# 수행시간 체크 함수
# ------------------------------
def time_check(func, msg):
    start_time = time.perf_counter()
    ret_img = func(image)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(msg, "수행시간 : %0.2f ms" % elapsed)
    return ret_img


# ------------------------------
# 실행
# ------------------------------
image1 = time_check(pixel_access1, "[방법1] 직접 접근 방식")
image2 = time_check(pixel_access2, "[방법2] item() 방식")
image3 = time_check(pixel_access3, "[방법3] LUT 방식")
image4 = time_check(pixel_access4, "[방법4] OpenCV 함수")
image5 = time_check(pixel_access5, "[방법5] NumPy 연산")


# ------------------------------
# Matplotlib 한 화면에 출력
# ------------------------------
plt.figure(figsize=(12, 6))

# 원본
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original")
plt.axis('off')

# 방법1
plt.subplot(2, 3, 2)
plt.imshow(image1, cmap='gray')
plt.title("Method1: Direct Access")
plt.axis('off')

# 방법2
plt.subplot(2, 3, 3)
plt.imshow(image2, cmap='gray')
plt.title("Method2: item() Access")
plt.axis('off')

# 방법3
plt.subplot(2, 3, 4)
plt.imshow(image3, cmap='gray')
plt.title("Method3: LUT")
plt.axis('off')

# 방법4
plt.subplot(2, 3, 5)
plt.imshow(image4, cmap='gray')
plt.title("Method4: OpenCV subtract")
plt.axis('off')

# 방법5
plt.subplot(2, 3, 6)
plt.imshow(image5, cmap='gray')
plt.title("Method5: NumPy Operation")
plt.axis('off')
plt.tight_layout()

titles = [
    "원본",
    "직접 접근",
    "item() 접근",
    "LUT",
    "OpenCV subtract",
    "NumPy 행렬연산"
]

images = [image, image1, image2, image3, image4, image5]

# ==============================
# 1) 한 화면에 6개 출력 (subplot)
# ==============================
plt.figure(figsize=(12, 6))

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()


# ==============================
# 2) 개별 창으로 6개 출력 (figure)
# ==============================
for i in range(6):
    plt.figure()   # 새 창 생성
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')


# ==============================
# 모든 창 한번에 출력
# ==============================
plt.show()
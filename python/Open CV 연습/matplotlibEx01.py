import cv2
import matplotlib.pyplot as plt      # pyplot 모듈 임포트

# 영상 읽기 (컬러로)
image = cv2.imread("images/matplot.jpg", cv2.IMREAD_COLOR)   # 영상 읽기
if image is None:
    raise Exception("영상파일 읽기 에러")   # 예외처리

# 영상 크기 정보
rows, cols = image.shape[:2]          # 영상 크기 정보

# BGR → RGB 변환 (matplotlib 표시용)
rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   # 컬러 공간 변환

# BGR → Gray 변환
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 흑백 영상 변환

# figure 1: 원본 영상 표시
fig = plt.figure(num=1, figsize=(3,4))   # 그림 생성
plt.imshow(image)                        # 영상 표시
plt.title("figure1- original(bgr)")      # 제목
plt.axis('off')                           # 축 제거
plt.tight_layout()                        # 여백 제거

# figure 2: RGB / Gray 서브플롯 표시
fig = plt.figure(figsize=(6,4))          # 그림 생성
plt.suptitle("figure2- pyplot image display")   # 전체 제목

# 서브플롯 1: 컬러 이미지
plt.subplot(1, 2, 1)
plt.imshow(rgb_img)
plt.title("rgb color")

# 서브플롯 2: 그레이 이미지
plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.title("gray_img")

plt.show()    # 전체 그림 띄우기

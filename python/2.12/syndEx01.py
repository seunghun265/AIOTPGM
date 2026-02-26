import numpy as np, cv2

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)   # 영상 읽기
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None:
    raise Exception("영상파일 읽기 오류")

# -----------------------------
# 영상 합성 방법
# -----------------------------
alpha, beta = 0.5, 0.5     # 가중 비율

add_img1 = cv2.add(image1, image2)                     # 두 영상 단순 더하기
add_img2 = cv2.add(image1 * alpha, image2 * beta)     # 두 영상 비율 곱 후 더하기
add_img2 = np.clip(add_img2, 0, 255).astype("uint8")  # saturation 처리
add_img3 = cv2.addWeighted(image1, alpha, image2, beta, 0)  # OpenCV 가중합

titles = ['image1', 'image2', 'add_img1', 'add_img2', 'add_img3']   # 윈도우 이름

for t in titles:
    cv2.imshow(t, eval(t))     # 변수 이름 문자열 → 실제 변수값 변환

cv2.waitKey(0)

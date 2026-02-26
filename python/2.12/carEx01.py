import numpy as np
import cv2

# ------------------------------
# 영상 읽기 (번호 입력 제거)
# ------------------------------
fname = "images/test_car/01.jpg"   # ← 여기 파일명만 바꿔서 사용
image = cv2.imread(fname, cv2.IMREAD_COLOR)

if image is None:
    raise Exception("영상파일 읽기 오류")

# ------------------------------
# 마스크 생성 (가로로 긴 커널)
# ------------------------------
mask = np.ones((5, 17), np.uint8)

# ------------------------------
# 영상 처리
# ------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)     # 흑백 변환
gray = cv2.blur(gray, (5, 5))                      # 블러링
gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5)         # 수평 엣지 검출

# 이진화
th_img = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)[1]

# Morph Close 연산 (번호판 문자 연결)
morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations=3)

# ------------------------------
# 결과 출력
# ------------------------------
cv2.imshow("image", image)
cv2.imshow("binary image", th_img)
cv2.imshow("morph image", morph)

cv2.waitKey(0)
cv2.destroyAllWindows()

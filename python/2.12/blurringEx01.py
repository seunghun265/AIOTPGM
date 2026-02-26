import numpy as np
import cv2

# ------------------------------
# 회선 수행 함수 1 (행렬 연산 방식)
# ------------------------------
def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)

    ycenter = mask.shape[0] // 2
    xcenter = mask.shape[1] // 2   # ✅ 수정

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1

            roi = image[y1:y2, x1:x2].astype("float32")
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]

    return dst


# ------------------------------
# 회선 수행 함수 2 (직접 접근)
# ------------------------------
def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)

    ycenter = mask.shape[0] // 2
    xcenter = mask.shape[1] // 2   # ✅ 수정

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            s = 0.0
            for u in range(mask.shape[0]):
                for v in range(mask.shape[1]):
                    y = i + u - ycenter
                    x = j + v - xcenter
                    s += image[y, x] * mask[u, v]

            dst[i, j] = s

    return dst


# ------------------------------
# 영상 읽기
# ------------------------------
image = cv2.imread("images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

# ------------------------------
# 3x3 평균 필터
# ------------------------------
mask = np.ones((3, 3), np.float32) / 9.0

# ------------------------------
# 필터 적용
# ------------------------------
blur1 = filter(image, mask)
blur2 = filter2(image, mask)

blur1 = cv2.convertScaleAbs(blur1)
blur2 = cv2.convertScaleAbs(blur2)

# ------------------------------
# 출력
# ------------------------------
cv2.imshow("Original", image)
cv2.imshow("Blur1 Matrix Method", blur1)
cv2.imshow("Blur2 Pixel Access Method", blur2)

cv2.waitKey(0)
cv2.destroyAllWindows()

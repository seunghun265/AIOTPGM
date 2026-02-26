import cv2
import pytesseract
import numpy as np
import time

# Tesseract 경로
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ------------------------------
# 이미지 읽기 + 시간 측정
# ------------------------------
start_total = time.perf_counter()

image = cv2.imread("images/test_car/06.jpg")
if image is None:
    print("이미지 로딩 실패")
    exit()

# ------------------------------
# 전처리
# ------------------------------
t1 = time.perf_counter()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
# gray = cv2.GaussianBlur(gray, (5,5), 0)
t2 = time.perf_counter()
print(f"[전처리] { (t2 - t1)*1000:.2f} ms")

# ------------------------------
# 엣지 검출
# ------------------------------
t1 = time.perf_counter()
edged = cv2.Canny(gray, 30, 200)
t2 = time.perf_counter()
print(f"[엣지 검출] { (t2 - t1)*1000:.2f} ms")

# ------------------------------
# 모폴로지 연산
# ------------------------------
t1 = time.perf_counter()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated = cv2.dilate(edged, kernel, iterations=1)
eroded  = cv2.erode(dilated, kernel, iterations=1)
closed  = cv2.morphologyEx(eroded, cv2.MORPH_CLOSE, kernel, iterations=2)
t2 = time.perf_counter()
print(f"[모폴로지] { (t2 - t1)*1000:.2f} ms")

# ------------------------------
# 윤곽선 탐색
# ------------------------------
t1 = time.perf_counter()
cnts, _ = cv2.findContours(closed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
t2 = time.perf_counter()
print(f"[윤곽선 탐색] { (t2 - t1)*1000:.2f} ms")

# ------------------------------
# 번호판 찾기
# ------------------------------
plate = None
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        plate = approx
        break

# ------------------------------
# OCR
# ------------------------------
if plate is not None:
    x, y, w, h = cv2.boundingRect(plate)
    plate_img = gray[y:y+h, x:x+w]

    t1 = time.perf_counter()
    text = pytesseract.image_to_string(plate_img, lang="kor+eng")
    t2 = time.perf_counter()
    print(f"[OCR] { (t2 - t1)*1000:.2f} ms")

    print("번호판 인식 결과:", text)

    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imshow("Plate", plate_img)

# ------------------------------
# 전체 수행 시간
# ------------------------------
end_total = time.perf_counter()
print(f"전체 처리 시간: {(end_total - start_total)*1000:.2f} ms")

# ------------------------------
# 결과 출력
# ------------------------------
cv2.imshow("Original", image)
cv2.imshow("Edge", edged)
cv2.imshow("Morphology", closed)

cv2.waitKey(0)
cv2.destroyAllWindows()

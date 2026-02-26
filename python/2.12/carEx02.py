import cv2
import pytesseract
import numpy as np
import imutils


# Tesseract 경로 (Windows만 필요)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 이미지 불러오기
image = cv2.imread("images/test_car/06.jpg")
if image is None:
    print("이미지 로딩 실패")
    exit()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 노이즈 제거
gray = cv2.bilateralFilter(gray, 11, 17, 17)

# 엣지 검출
edged = cv2.Canny(gray, 30, 200)

# 윤곽선 찾기
cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

plate = None

# 번호판 후보 찾기
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # 사각형이면 번호판 후보
    if len(approx) == 4:
        plate = approx
        break

# 번호판 영역 추출
if plate is not None:
    x, y, w, h = cv2.boundingRect(plate)
    plate_img = gray[y:y+h, x:x+w]

    # OCR
    text = pytesseract.image_to_string(plate_img, lang="kor+eng")
    print("번호판:", text)

    # 번호판 표시
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imshow("Plate", plate_img)

cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

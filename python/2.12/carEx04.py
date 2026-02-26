import os
import cv2
import pytesseract
from ultralytics import YOLO
from openpyxl import Workbook

# Tesseract 경로
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# YOLO 모델 로드
model = YOLO("yolov5s.pt")   # 번호판 전용 모델 있으면 교체

# 이미지 폴더 경로
folder_path = "images"

# 엑셀 생성
wb = Workbook()
ws = wb.active
ws.append(["파일명", "번호판 인식 결과"])

# 이미지 반복 처리
for file in os.listdir(folder_path):
    if file.lower().endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(folder_path, file)
        img = cv2.imread(img_path)

        results = model(img)
        plate_text = "인식 실패"

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                plate = img[y1:y2, x1:x2]

                # 전처리
                gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
                _, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

                # OCR
                config = "--psm 7 -c tessedit_char_whitelist=가나다라마바사아자차카타파하0123456789"
                text = pytesseract.image_to_string(th, lang="kor", config=config)
                plate_text = text.strip()
                break  # 첫 번호판만

        # 엑셀 저장
        ws.append([file, plate_text])
        print(file, "->", plate_text)

# 엑셀 파일 저장
wb.save("license_plate_result.xlsx")
print("엑셀 저장 완료")

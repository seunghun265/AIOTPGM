from ultralytics import YOLO
import cv2
import pytesseract
import time
import os

# Tesseract 경로
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# YOLO 모델
model = YOLO("yolov8n.pt")  # 번호판 모델 있으면 교체

# 이미지 폴더
image_folder = "images/test_car"

# 모든 이미지 반복
for img_name in os.listdir(image_folder):
    if not img_name.lower().endswith((".jpg",".png",".jpeg")):
        continue

    img_path = os.path.join(image_folder, img_name)
    print(f"\n처리 중: {img_name}")

    image = cv2.imread(img_path)
    if image is None:
        print("이미지 로딩 실패")
        continue

    # YOLO 탐지
    results = model(image)

    # 결과 박스 표시
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls]

            # 번호판 모델 아니면 car/bus 등 임시 필터
            if label not in ["license-plate", "plate", "car", "bus"]:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            plate_img = image[y1:y2, x1:x2]

            # OCR
            gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            text = pytesseract.image_to_string(gray, lang="kor+eng", config="--psm 7")
            text = text.strip()

            # 박스 + 텍스트 표시
            cv2.rectangle(image, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(image, text, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    # 화면 출력
    cv2.imshow("YOLO Plate Detection", image)

    # 키 입력 대기 (다음 이미지)
    key = cv2.waitKey(0)  # 아무 키 누르면 다음 이미지
    if key == 27:  # ESC 누르면 종료
        break

cv2.destroyAllWindows()

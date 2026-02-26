from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
results = model("images/bus.jpg")

img = results[0].plot()

cv2.imshow("YOLO Result", img)
cv2.waitKey(0)   # 아무 키나 누를 때까지 대기
cv2.destroyAllWindows()

import numpy as np              # 수치 계산용 라이브러리 (sqrt 사용)
import cv2                       # OpenCV 영상 처리 라이브러리

# 마우스 이벤트 발생 시 자동 호출되는 콜백 함수
def onMouse(event, x, y, flags, param):
    global title, pt             # 전역 변수 title, pt 사용 선언

    # 왼쪽 마우스 버튼 눌렀을 때
    if event == cv2.EVENT_LBUTTONDOWN:

        # 시작점이 아직 없으면 현재 좌표를 시작점으로 저장
        if pt[0] < 0:
            pt = (x, y)

        # 시작점이 이미 있으면 사각형 그리기
        else:
            cv2.rectangle(image, pt, (x, y), (255, 0, 0), 2)  # 파란색 사각형
            cv2.imshow(title, image)        # 화면에 다시 출력
            pt = (-1, -1)                  # 시작점 초기화 (다시 그리기 가능)

    # 오른쪽 마우스 버튼 눌렀을 때
    elif event == cv2.EVENT_RBUTTONDOWN:

        # 중심점이 아직 없으면 현재 좌표 저장
        if pt[0] < 0:
            pt = (x, y)

        # 중심점이 이미 있으면 원 그리기
        else:
            dx, dy = pt[0] - x, pt[1] - y   # 두 점 사이 거리 계산용 차이값
            radius = int(np.sqrt(dx*dx + dy*dy))  # 피타고라스 정리 → 반지름 계산

            cv2.circle(image, pt, radius, (0, 0, 255), 2)  # 빨간색 원 그리기
            cv2.imshow(title, image)       # 화면 업데이트
            pt = (-1, -1)                 # 중심점 초기화


# 흰색 배경 영상 생성 (300x500 크기, 3채널 RGB)
image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)                 # 시작 좌표 초기값 (없는 상태 표시)
title = "Draw Event"           # 윈도우 제목

cv2.imshow(title, image)       # 영상 창 출력
cv2.setMouseCallback(title, onMouse)  # 마우스 이벤트 함수 등록
cv2.waitKey(0)                  # 키 입력 대기 (아무 키나 누르면 종료)

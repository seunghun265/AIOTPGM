import numpy as np, cv2

m1 = np.full((3, 6), 10, np.uint8)     # 3x6 행렬, 값 10으로 초기화
m2 = np.full((3, 6), 50, np.uint8)     # 3x6 행렬, 값 50으로 초기화

m_mask = np.zeros(m1.shape, np.uint8)  # 마스크 행렬 생성
m_mask[:, 3:] = 1                       # 오른쪽 절반 영역을 1로 설정

m_add1 = cv2.add(m1, m2)                # 행렬 덧셈
m_add2 = cv2.add(m1, m2, mask=m_mask)  # 마스크 영역만 덧셈 수행

# 행렬 나눗셈 수행
m_div1 = cv2.divide(m1, m2)             # 정수 나눗셈
m1 = m1.astype(np.float32)
m2 = np.float32(m2)                     # m2를 float32로 변환
m_div2 = cv2.divide(m1, m2)             # 실수 나눗셈

titles = ['m1', 'm2', 'm_mask', 'm_add1', 'm_add2', 'm_div1', 'm_div2']
for title in titles:
    print("[%s]\n%s\n" % (title, eval(title)))

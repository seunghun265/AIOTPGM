from tkinter import *
import random

# 정답 설정
answer = random.randint(1, 100)  # 1에서 100 사이 난수

# 추측 함수
def guessing():
    guess = float(guessField.get())  # Entry에서 값 읽기
    if guess > answer:
        msg = "높음!"
    elif guess < answer:
        msg = "낮음!"
    else:
        msg = "정답!"
    resultLabel["text"] = msg      # 메시지 출력
    guessField.delete(0, END)      # 입력창 비우기

# 리셋 함수
def reset():
    global answer
    answer = random.randint(1, 100)
    resultLabel["text"] = "다시 한번 해보세요!"

# Tkinter 윈도우 설정
window = Tk()
window.configure(bg="white")
window.title("숫자를 맞춰보세요!")
window.geometry("400x150")

# 제목
titleLabel = Label(window, text="숫자 게임에 오신 것을 환영합니다!", bg="white")
titleLabel.pack()

# 입력 필드
guessField = Entry(window)
guessField.pack()

# 버튼
guessButton = Button(window, text="확인", command=guessing)
guessButton.pack()

resetButton = Button(window, text="다시 시작", command=reset)
resetButton.pack()

# 결과 출력
resultLabel = Label(window, text="", bg="white")
resultLabel.pack()

window.mainloop()


from tkinter import *
import random

window = Tk()
window.title("주사위 게임")
window.geometry("400x300")

# 전역 변수
dice1_value = 0
dice2_value = 0
throw_count = 0
total = 0

# 이미지 로드
dice_img_move = PhotoImage(file="dice1.gif")  # 움직이는 이미지
dice_img_stop = PhotoImage(file="dice2.png")  # 멈춘 이미지

# 주사위 레이블
dice1_label = Label(window, image=dice_img_stop)
dice1_label.pack(side=LEFT, padx=20, pady=20)

dice2_label = Label(window, image=dice_img_stop)
dice2_label.pack(side=RIGHT, padx=20, pady=20)

# 결과 라벨
result_label = Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Low/High 라벨
lh_label = Label(window, text="", font=("Arial", 14))
lh_label.pack(pady=10)

def show_final_result():
    """주사위 값을 결정하고 멈춘 이미지로 바꾸는 함수"""
    global dice1_value, dice2_value, total, throw_count

    # 랜덤 주사위 값
    dice1_value = random.randint(1,6)
    dice2_value = random.randint(1,6)
    total = dice1_value + dice2_value

    # 멈춘 이미지로 바꾸기
    dice1_label.configure(image=dice_img_stop)
    dice2_label.configure(image=dice_img_stop)

    result_label.configure(text=f"주사위 값: {dice1_value} + {dice2_value} = {total}")

    # 두 번 던지고 결과 표시
    if throw_count == 2:
        if total > 7:
            lh_label.configure(text="High! 🎉 이겼다!")
        else:
            lh_label.configure(text="Low! 😢 졌다!")
        throw_button.configure(state=DISABLED)

def throw_dice():
    """주사위 던지기 버튼 누르면 호출"""
    global throw_count
    throw_count += 1

    # 움직이는 이미지 먼저 보여주기
    dice1_label.configure(image=dice_img_move)
    dice2_label.configure(image=dice_img_move)
    window.update()  # 화면 갱신

    # 딜레이 후 최종 주사위 값 표시
    window.after(1000, show_final_result)  # 1000ms = 1초

# 버튼
throw_button = Button(window, text="주사위 던지기", command=throw_dice)
throw_button.pack(pady=10)

def reset_game():
    global throw_count, total
    throw_count = 0
    total = 0
    dice1_label.configure(image=dice_img_stop)
    dice2_label.configure(image=dice_img_stop)
    result_label.configure(text="")
    lh_label.configure(text="")
    throw_button.configure(state=NORMAL)

reset_button = Button(window, text="다시 시작", command=reset_game)
reset_button.pack(pady=10)

window.mainloop()

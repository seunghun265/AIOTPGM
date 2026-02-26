import random
from tkinter import *
from PIL import Image, ImageTk  # Pillow 사용

window = Tk()
window.title("가위바위보 게임")
window.geometry("500x450")

Label(window, text="선택하세요", font=("Helvetica", 16)).pack(pady=10)
frame = Frame(window)
frame.pack(pady=10)

# Pillow로 이미지 열기
rock_img = Image.open(r"C:\Users\SAMSUNG\Documents\Aiot\2.2\rock.png")
paper_img = Image.open(r"C:\Users\SAMSUNG\Documents\Aiot\2.2\paper.png")
scissors_img = Image.open(r"C:\Users\SAMSUNG\Documents\Aiot\2.2\scissors.png")

# 50x50으로 크기 조절
rock_img = rock_img.resize((120, 120))
paper_img = paper_img.resize((120, 120))
scissors_img = scissors_img.resize((120, 120))

# Tkinter에서 쓸 수 있는 이미지로 변환
rock_image = ImageTk.PhotoImage(rock_img)
paper_image = ImageTk.PhotoImage(paper_img)
scissors_image = ImageTk.PhotoImage(scissors_img)

# 컴퓨터 이미지 레이블
computer_image_label = Label(window, image=rock_image)
computer_image_label.pack(pady=10)

# 결과 라벨
output = Label(window, text="", font=("Helvetica", 16))
output.pack(pady=10)

def decide(user_choice):
    options = ["가위", "바위", "보"]
    comp_choice = random.choice(options)

    # 컴퓨터 이미지 바꾸기
    if comp_choice == "가위":
        computer_image_label.configure(image=scissors_image)
    elif comp_choice == "바위":
        computer_image_label.configure(image=rock_image)
    else:
        computer_image_label.configure(image=paper_image)

    # 승패 계산
    if user_choice == comp_choice:
        result = "비겼습니다!"
    elif (user_choice == "가위" and comp_choice == "보") or \
         (user_choice == "바위" and comp_choice == "가위") or \
         (user_choice == "보" and comp_choice == "바위"):
        result = "이겼습니다! 🎉"
    else:
        result = "졌습니다 😢"

    output.configure(text=f"사용자: {user_choice}, 컴퓨터: {comp_choice}\n{result}")

# 버튼 클릭 함수
def pass_s(): decide("가위")
def pass_r(): decide("바위")
def pass_p(): decide("보")

# 버튼 생성
rock = Button(frame, image=rock_image, command=pass_r)
rock.pack(side="left", padx=10)
paper = Button(frame, image=paper_image, command=pass_p)
paper.pack(side="left", padx=10)
scissors = Button(frame, image=scissors_image, command=pass_s)
scissors.pack(side="left", padx=10)

window.mainloop()

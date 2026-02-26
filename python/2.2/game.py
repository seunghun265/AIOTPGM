import tkinter as tk
import random

def generate_lotto():
    numbers = random.sample(range(1, 46), 6)  # 1~45 사이 6개 숫자
    numbers.sort()  # 정렬
    result_label.config(text="로또 번호: " + " - ".join(map(str, numbers)))

# tkinter 창
root = tk.Tk()
root.title("로또 자동 번호 생성기")
root.geometry("400x200")

title_label = tk.Label(root, text="로또 번호 자동 생성기", font=("Arial", 16))
title_label.pack(pady=10)

generate_btn = tk.Button(root, text="번호 생성", font=("Arial", 14), command=generate_lotto)
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

root.mainloop()

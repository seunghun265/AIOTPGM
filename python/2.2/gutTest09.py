from tkinter import *

window = Tk()

Label(window, text="화씨").grid(row=0, column=0)
Label(window, text="섭씨").grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def f_to_c():
    f = float(e1.get())          # 화씨 값 가져오기 , float 는 실수 소수점까지표현
    c = (f - 32) * 5 / 9         # 섭씨 변환
    e2.delete(0, END)
    e2.insert(0, str(c))

Button(window, text="화씨→섭씨", command=f_to_c).grid(row=2, column=0, columnspan=2)

window.mainloop()

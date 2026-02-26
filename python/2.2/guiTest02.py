from tkinter import *
window = Tk()
button = Button(window,    text="클릭하세요!",
bg="yellow",    fg="blue", # 전경색과배경색설정
width=80,    height=2    # 크기설정
)
button.pack()        #배치 ?
window.mainloop()         #상호작용
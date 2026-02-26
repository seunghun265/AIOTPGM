from tkinter import *
window = Tk()
f = Frame(window)        #frame = 컨테이너 위젯

b1 = Button(f, text="박스#1", bg="red",    fg="white")
b2 = Button(f, text="박스#2", bg="green",  fg="black")
b3 = Button(f, text="박스#3", bg="orange", fg="white")

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

l = Label(window, text="이레이블은버튼들위에배치된다.")

l.pack()
f.pack()
window.mainloop()

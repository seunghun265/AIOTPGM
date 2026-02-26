from tkinter import * # tkinter모듈을포함
window = Tk() # 루트윈도우를생성
label = Label(window, text="Hello tkinter") # 레이블위젯을생성
label.pack() # 레이블위젯을윈도우에배치
window.mainloop() # 윈도우가사용자동작을대기
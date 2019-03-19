from tkinter import *
from PIL import Image, ImageTk



window=Tk()
window.title("TicTacToe") #창이름
window.geometry("300x300") #윈도우 창 크기
image1 = PhotoImage(file="D:/GitHub/tictactoe/tictoc/image/o.gif")
label1 = Label(window, image=image1)
label2 = Label(window, image=image1,width=100, height=100)
label1.place(x=0,y=0)
label2.place(x=100,y=100)
window.mainloop()
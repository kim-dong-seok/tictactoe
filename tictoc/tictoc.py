from tkinter import *
from PIL import Image, ImageTk
from random import *


window=Tk()
window.title("TicTacToe") #창이름
window.geometry("300x330") #윈도우 창 크기
originimage1=Image.open("D:/GitHub/tictactoe/tictoc/image/o.gif").resize((100,100))
originimage2=Image.open("D:/GitHub/tictactoe/tictoc/image/x.gif").resize((100,100))
image1=ImageTk.PhotoImage(originimage1)
image2=ImageTk.PhotoImage(originimage2)
L=[[choice([1,2])for j in range(3)]for i in range(3)]
for i in range(3):
    for j in range(3):
        if L[i][j]==1:
            L[i][j] = Label(window, image=image1)
        elif L[i][j]==2:
            L[i][j] = Label(window, image=image2)
        L[i][j].place(x=100*j, y=100*i)
def closecallback():
    L = [[choice([1, 2]) for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            if L[i][j]==1:
                L[i][j] = Label(window, image=image1)
            elif L[i][j]==2:
                L[i][j] = Label(window, image=image2)
            L[i][j].place(x=100*j, y=100*i)
b1=Button(window,text="다시생성",command=closecallback)
b1.pack(side="bottom")

window.mainloop()
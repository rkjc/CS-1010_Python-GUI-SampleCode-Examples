from tkinter import *

groot = Tk()
groot.geometry("200x200")

def addStar():
    global str_1
    str_1 = str_1 + "*"
    lbl_2.config(text=str_1)

def addX():
    global str_1
    str_1 = str_1 + "X"
    lbl_2.config(text=str_1)

def del_last():
    global str_1
    str_length = len(str_1)
    str_1 = str_1[ : str_length - 1]
    lbl_2.config(text=str_1)

str_1 = ""

# adding widgets to the Top window
lbl_2 = Label(groot, text="this label")
lbl_2.pack()

btn_2 = Button(groot, text="add *", command=addStar)
btn_2.pack()

btn_3 = Button(groot, text="add x", command=addX)
btn_3.pack()

btn_5 = Button(groot, text="del", command=del_last)
btn_5.pack()

groot.mainloop()
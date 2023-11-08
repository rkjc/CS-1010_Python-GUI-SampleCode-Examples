 
import tkinter as tk
import random

groot = tk.Tk()
groot.geometry("800x800")

cx = 0
cy = 0

def moveCat():
    global cx, cy
    lbl_cat.place(x = cx, y = cy)
    lbl_cat.tkraise()

def diagCat():
    global cx, cy
    cx += 20
    cy += 30
    moveCat()

def randomCat():
    global cx, cy
    cx = random.randint(0, 730)
    cy = random.randint(0, 730)
    moveCat()

def centerCat():
    global cx, cy
    cx = 350
    cy = 300
    moveCat()

def downCat():
    global cx, cy
    cy += 10
    moveCat()

myCatImg = tk.PhotoImage(file="cat.png")
myBackImg = tk.PhotoImage(file="background.png")

lbl_cat = tk.Label(groot, image=myCatImg)


lbl_back = tk.Label(groot, image=myBackImg)
lbl_back.place(x=0, y=0)

btn1 = tk.Button(groot, text="diag cat", command=diagCat)
btn1.pack()
btn2 = tk.Button(groot, text="random cat", command=randomCat)
btn2.pack()
btn3 = tk.Button(groot, text="center cat", command=centerCat)
btn3.pack()
btn4 = tk.Button(groot, text="V", command=downCat)
btn4.place(x=700, y=700)

groot.mainloop()
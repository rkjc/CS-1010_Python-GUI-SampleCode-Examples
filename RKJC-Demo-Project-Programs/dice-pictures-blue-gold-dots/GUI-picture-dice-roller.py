 
import tkinter as tk
import random
groot = tk.Tk()
groot.geometry("300x300")

def doThis():
    dice = random.randint(1,6)
    if dice == 1:
        lbl1.config(image=dice1img)
    if dice == 2:
        lbl1.config(image=dice2img)
    if dice == 3:
        lbl1.config(image=dice3img)
    if dice == 4:
        lbl1.config(image=dice4img)
    if dice == 5:
        lbl1.config(image=dice5img)
    if dice == 6:
        lbl1.config(image=dice6img)

dice1img = tk.PhotoImage(file="1.png").subsample(4)
dice2img = tk.PhotoImage(file="2.png").subsample(4)
dice3img = tk.PhotoImage(file="3.png").subsample(4)
dice4img = tk.PhotoImage(file="4.png").subsample(4)
dice5img = tk.PhotoImage(file="5.png").subsample(4)
dice6img = tk.PhotoImage(file="6.png").subsample(4)

btn1 = tk.Button(groot, text="roll dice", command=doThis)
btn1.pack()

lbl1 = tk.Label(groot, text="picture of dice")
lbl1.pack()

groot.mainloop()
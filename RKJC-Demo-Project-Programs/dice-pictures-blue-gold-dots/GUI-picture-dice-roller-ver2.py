 
import tkinter as tk
import random
groot = tk.Tk()
#groot.geometry("300x300")

def doThis():
    dice = random.randint(1,6)
    lbl1.config(image=diceimgarray[dice-1])

substringsize = 3

dice1img = tk.PhotoImage(file="1.png").subsample(substringsize)
dice2img = tk.PhotoImage(file="2.png").subsample(substringsize)
dice3img = tk.PhotoImage(file="3.png").subsample(substringsize)
dice4img = tk.PhotoImage(file="4.png").subsample(substringsize)
dice5img = tk.PhotoImage(file="5.png").subsample(substringsize)
dice6img = tk.PhotoImage(file="6.png").subsample(substringsize)

diceimgarray = [dice1img, dice2img, dice3img, dice4img, dice5img, dice6img]

btn1 = tk.Button(groot, text="roll dice", command=doThis, font=('',30))
btn1.pack()

lbl1 = tk.Label(groot, text="picture of dice")
lbl1.pack()

doThis()
groot.mainloop()

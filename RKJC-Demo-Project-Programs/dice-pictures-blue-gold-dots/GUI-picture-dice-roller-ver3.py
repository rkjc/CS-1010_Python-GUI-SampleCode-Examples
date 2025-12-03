 
import tkinter as tk
import random
groot = tk.Tk()
#groot.geometry("300x300")

# --- function definitions ---
def roll_all_dice():
    roll_dice_1()
    roll_dice_2()
      
def roll_dice_1():
    dice = random.randint(1,6)
    #lbl1.config(image=diceimgarray[dice-1])
    btn1.config(image=diceimgarray[dice-1])
    
def roll_dice_2():
    dice = random.randint(1,6)
    btn2.config(image=diceimgarray[dice-1])

# --- variables ---
substringsize = 6
dice_val_1 = 0
dice_val_2 = 0

# --- program code ---
dice1img = tk.PhotoImage(file="1.png").subsample(substringsize)
dice2img = tk.PhotoImage(file="2.png").subsample(substringsize)
dice3img = tk.PhotoImage(file="3.png").subsample(substringsize)
dice4img = tk.PhotoImage(file="4.png").subsample(substringsize)
dice5img = tk.PhotoImage(file="5.png").subsample(substringsize)
dice6img = tk.PhotoImage(file="6.png").subsample(substringsize)

diceimgarray = [dice1img, dice2img, dice3img, dice4img, dice5img, dice6img]

btn_roll_all = tk.Button(groot, text="roll all dice", command=roll_all_dice, font=('',20))
btn_roll_all.pack()

btn1 = tk.Button(groot, text="roll dice 1", command=roll_dice_1, font=('',20))
btn1.pack()

lbl1 = tk.Label(groot, text="click dice to roll each", font=('',16))
lbl1.pack()

btn2 = tk.Button(groot, text="roll dice 2", command=roll_dice_2, font=('',20))
btn2.pack()

#lbl2 = tk.Label(groot, text="picture of dice")
#lbl2.pack()

roll_all_dice()
groot.mainloop()

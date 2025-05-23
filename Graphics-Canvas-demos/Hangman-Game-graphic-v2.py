from tkinter import *
import random

groot = Tk()
groot.title("GUESS THE WORD: AMONG US EDITION")
groot.geometry("600x400")


# ====================================Functions==============================================
def runTimer():
    global count2
    if count2 < 11:
        showGraphic(count2)
        label_1.config(text=count2)
        count2 += 1
        # the function '.after' waits that many millisecs and calls the function
        groot.after(500, runTimer)
    else:
        label_1.config(text="FINISHED!")

def submission_function():
    global count
    if count < 11:
        count += 1
        showGraphic(count)
        label_1.config(text=count)

def showGraphic(count):
    if count > 0:
        hangman_stick.create_oval(125, 100, 175, 50, width=2)
    if count > 1:
        hangman_stick.create_line(135, 65, 145, 65, width=2)
    if count > 2:
        hangman_stick.create_line(155, 65, 165, 65, width=2)
    if count > 3:
        hangman_stick.create_line(150, 70, 150, 85, width=2)
    if count > 4:
        hangman_stick.create_line(140, 90, 160, 90, width=2)
    if count > 5:
        hangman_stick.create_line(150, 100, 150, 200, width=2)
    if count > 6:
        hangman_stick.create_line(150, 125, 100, 150, width=2)
    if count > 7:
        hangman_stick.create_line(150, 125, 200, 150, width=2)
    if count > 8:
        hangman_stick.create_line(150, 200, 100, 225, width=2)
    if count > 9:
        hangman_stick.create_line(150, 200, 200, 225, width=2)


# ==================================== Variables ==============================================

count = 0
count2 = 0

# ==================================== widgets ========================

hangman_stick = Canvas(groot, bg='cyan')

hangman_stick.create_oval(10, 10, 80, 80, outline = "black", fill = "white",width = 2)

hangman_stick.create_line(70, 40, 70, 250, width=6)
hangman_stick.create_line(70, 40, 150, 20, width=2)
hangman_stick.create_line(150, 20, 150, 50, width=10)

label_1 = Label(groot, text=count)

test_button = Button(groot, text="Step", command=submission_function)
btn_2 = Button(groot, text="Animate", command=runTimer)


# ====================================Outputs==============================================

label_1.pack()
test_button.pack()
btn_2.pack()
hangman_stick.pack()

groot.mainloop()



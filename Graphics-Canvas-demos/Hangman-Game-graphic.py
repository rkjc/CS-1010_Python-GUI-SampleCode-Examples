from tkinter import *
import random

window = Tk()
window.title("GUESS THE WORD: AMONG US EDITION")
window.geometry("400x400+6000+100")


# ====================================Functions==============================================

def submission_function():
    global count
    count += 1

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

    label_1.config(text=count)


# ==================================== Variables ==============================================

count = 0

# ==================================== widgets ========================

hangman_stick = Canvas(window)
hangman_stick.create_line(70, 20, 70, 250, width=2)
hangman_stick.create_line(70, 20, 150, 20, width=2)
hangman_stick.create_line(150, 20, 150, 50, width=2)

label_1 = Label(window, text=count)

test_button = Button(window, text="Submit", command=submission_function)


# ====================================Outputs==============================================

label_1.pack()
test_button.pack()
hangman_stick.pack()

window.mainloop()



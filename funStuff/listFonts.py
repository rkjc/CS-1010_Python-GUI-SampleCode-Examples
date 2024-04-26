 
import tkinter
from tkinter import font

def doButton():
    label_1.configure(text = "you pushed the button")
    label_1.configure(font=("Wingdings", 9))

bob = tkinter.Tk()
bob.geometry('600x800')
bob.title("Font List")

list_fonts = list(font.families())

list_fonts.sort()

count = 0
while count < 10:
    this_family = list_fonts[count]
    temp_text = str(this_family) + " >>>  A quick brown fox got lost"
    tkinter.Label(bob, font=(this_family, 10), text=temp_text).pack()
    count += 1

label_1 = tkinter.Label(bob, text="A quick brown fox got lost")
label_1.pack()


bob.mainloop()







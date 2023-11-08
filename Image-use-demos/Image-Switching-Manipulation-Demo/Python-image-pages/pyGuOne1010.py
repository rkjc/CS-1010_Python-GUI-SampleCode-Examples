from tkinter import *

window = Tk()
window.geometry("300x300")
window["bg"] = ("#FFB^C1")
window.title("cs1010 student project debug")

E1 = Entry(window, bd = 5)
E1.grid(row=1, column=1)

fred = "yoo there"

def doButton():
    varOne.set(E1.get())
    print("output ", fred)
    # fred = "all done"

varOne = StringVar()
lableOne = Label(window, textvariable = varOne, relief = RAISED, width=30, height=5).grid(row=0, column = 1)

varOne.set("Insert name")

MyButton1 = Button(window, text="Submit", width=10, command = doButton)
MyButton1.grid(row=2, column=1)



window.mainloop()


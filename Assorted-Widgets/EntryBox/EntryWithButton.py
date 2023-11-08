from tkinter import *

def doButton():
    L1.config( text = E1.get() )

groot = Tk()

L1 = Label(text="output here")
L1.pack()

E1 = Entry(text = "enter something here")
E1.pack()

B1 = Button(text = "paste ENTRY to LABEL", command=doButton)
B1.pack()

groot.mainloop()
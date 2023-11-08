#https://stackoverflow.com/questions/50422735/tkinter-resize-frame-and-contents-with-main-window

from tkinter import *
from tkinter import scrolledtext

mw = Tk()
mw.title("Multi-window demo code - 4")
mw.geometry("600x500")

mw.columnconfigure(0, weight=1)
mw.rowconfigure(1, weight=1)

def showRed():
    redFrame.tkraise()

def showGreen():
    greenFrame.tkraise()


def showBlue():
    blueFrame.tkraise()


# bottom Frame ----------------------------------------------------
bottom = Frame(mw, bg="yellow")
bottom.grid_propagate(False)
bottom.grid(row=1, column=0, sticky=N+W+S+E)

bottom.columnconfigure(0, weight=1)
bottom.rowconfigure(0, weight=1)

# red Frame ----------------------------------------------------
redFrame = Frame(bottom, bg="red")
redFrame.grid_propagate(False)
redFrame.grid(row=0, column=0, sticky=N+W+S+E)
redFrame.columnconfigure(0, weight=1)
redFrame.rowconfigure(0, weight=1)

redLabel_1 = Label(redFrame, text="this is the Red Frame")
redLabel_1.grid(column=0, row=0)

btn_b2 = Button(redFrame, fg="blue", text='blue', width='5', command=showBlue)
btn_b2.grid(row=0, column=0, padx=10, pady=10, sticky=N+W)

btn_g2 = Button(redFrame, fg="green", text='green', width='5', command=showGreen)
btn_g2.grid(row=0, column=0, padx=10, pady=10, sticky=N+E)


# green Frame ----------------------------------------------------
greenFrame = Frame(bottom, bg="green")
greenFrame.grid_propagate(False)
greenFrame.grid(row=0, column=0, sticky=N+W+S+E)
greenFrame.columnconfigure(0, weight=1)
greenFrame.rowconfigure(0, weight=1)

greenLabel_1 = Label(greenFrame, text="this is the Green Frame")
greenLabel_1.grid(column=0, row=0)

btn_r3 = Button(greenFrame, fg="red", text='red', width='5', command=showRed)
btn_r3.grid(row=0, column=0, padx=10, pady=10, sticky=N+W)

btn_b3 = Button(greenFrame, fg="blue", text='blue', width='5', command=showBlue)
btn_b3.grid(row=0, column=0, padx=10, pady=10, sticky=N+E)



# blue Frame ----------------------------------------------------
blueFrame = Frame(bottom, bg="blue")
blueFrame.grid_propagate(False)
blueFrame.grid(row=0, column=0, sticky=N+W+S+E)
blueFrame.columnconfigure(0, weight=1)
blueFrame.rowconfigure(0, weight=1)

blueLabel_1 = Label(blueFrame, text="this is the Blue Frame")
blueLabel_1.grid(column=0, row=0)

btn_g4 = Button(blueFrame, fg="green", text='green', width='5', command=showGreen)
btn_g4.grid(row=0, column=0, padx=10, pady=10, sticky=N+W)

btn_r4 = Button(blueFrame, fg="red", text='red', width='5', command=showRed)
btn_r4.grid(row=0, column=0, padx=10, pady=10, sticky=N+E)


mainloop()

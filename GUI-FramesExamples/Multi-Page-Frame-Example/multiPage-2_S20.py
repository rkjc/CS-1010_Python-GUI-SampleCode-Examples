#https://stackoverflow.com/questions/50422735/tkinter-resize-frame-and-contents-with-main-window

from tkinter import *
from tkinter import scrolledtext

groot = Tk()
groot.title("Multi-window demo code - 2")
groot.geometry("600x500")

groot.columnconfigure(0, weight=1)
groot.rowconfigure(1, weight=1)

def showRed():
    redFrame.tkraise()

def showGreen():
    greenFrame.tkraise()

def showBlue():
    blueFrame.tkraise()

# Parent widget for the buttons
buttons_frame = Frame(groot, bg="cyan", highlightbackground="black", highlightthickness=1)
buttons_frame.grid(row=0, column=0, sticky=N+W+E)

btn_1 = Button(buttons_frame, text='red', width='5', command=showRed)
btn_1.grid(row=0, column=0, padx=(10), pady=0)

btn_2 = Button(buttons_frame, text='green', width='5', command=showGreen)
btn_2.grid(row=0, column=1, padx=(10), pady=0)

btn_3 = Button(buttons_frame, text='blue', width='5', command=showBlue)
btn_3.grid(row=0, column=2, padx=(10), pady=0)

# bottom Frame ----------------------------------------------------
lower_box = Frame(groot, bg="yellow", padx=5, pady=5)
#bottom.grid_propagate(False)
lower_box.grid(row=1, column=0, padx=10, pady=10, sticky=N + W + S + E)

lower_box.columnconfigure(0, weight=1)
lower_box.rowconfigure(0, weight=1)

# red Frame ----------------------------------------------------
redFrame = Frame(lower_box, bg="red", padx=5, pady=5)
redFrame.grid_propagate(False)
redFrame.grid(row=0, column=0, sticky=N+W+S+E)
redFrame.columnconfigure(0, weight=1)
redFrame.rowconfigure(0, weight=1)

redLabel_1 = Label(redFrame, text="this is the Red Frame")
redLabel_1.grid(column=0, row=0)

# green Frame ----------------------------------------------------
greenFrame = Frame(lower_box, bg="green", padx=5, pady=5)
greenFrame.grid_propagate(False)
greenFrame.grid(row=0, column=0, sticky=N+W+S+E)
greenFrame.columnconfigure(0, weight=1)
greenFrame.rowconfigure(0, weight=1)

greenLabel_1 = Label(greenFrame, text="this is the Green Frame")
greenLabel_1.grid(column=0, row=0)

# blue Frame ----------------------------------------------------
blueFrame = Frame(lower_box, bg="blue", padx=5, pady=5)
blueFrame.grid_propagate(False)
blueFrame.grid(row=0, column=0, sticky=N+W+S+E)
blueFrame.columnconfigure(0, weight=1)
blueFrame.rowconfigure(0, weight=1)

blueLabel_1 = Label(blueFrame, text="this is the Blue Frame")
blueLabel_1.grid(column=0, row=0)



mainloop()

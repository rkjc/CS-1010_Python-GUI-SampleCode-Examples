 
# from tkinter import *
import tkinter as tk
from tkinter import scrolledtext

mainWin = tk.Tk()
mainWin.title("Multi-window demo code - 1")
mainWin.geometry("600x500")

mainWin.columnconfigure(0, weight=1)
mainWin.rowconfigure(1, weight=1)

def showRed():
    redFrame.tkraise()

def showGreen():
    greenFrame.tkraise()

def showBlue():
    blueFrame.tkraise()

# top frame --------
my_top_frame = tk.Frame(mainWin, bg="cyan", highlightbackground="black", highlightthickness=1)
my_top_frame.grid(row=0, column=0, sticky=tk.N+tk.W+tk.E)
# bottom Frame -----
my_bottom_frame = tk.Frame(mainWin, bg="yellow")
my_bottom_frame.grid_propagate(False)
my_bottom_frame.grid(row=1, column=0, sticky=tk.N+tk.W+tk.S+tk.E)
my_bottom_frame.columnconfigure(0, weight=1)
my_bottom_frame.rowconfigure(0, weight=1)

# make the buttons
btn_1 = tk.Button(my_top_frame, text='red', width='5', command=showRed)
btn_1.grid(row=0, column=0, padx=(10), pady=10)

btn_2 = tk.Button(my_top_frame, text='green', width='5', command=showGreen)
btn_2.grid(row=0, column=1, padx=(10), pady=10)

btn_3 = tk.Button(my_top_frame, text='blue', width='5', command=showBlue)
btn_3.grid(row=0, column=2, padx=(10), pady=10)

# red Frame ----------------------------------------------------
redFrame = tk.Frame(my_bottom_frame, bg="red", padx=5, pady=5)
redFrame.place(x=20, y=20, width=300, height=300)
#redFrame.place(x=20, y=20, relwidth=1, height=300)

redLabel_1 = tk.Label(redFrame, text="this is the Red Frame")
redLabel_1.grid(column=0, row=0)

# green Frame ----------------------------------------------------
greenFrame = tk.Frame(my_bottom_frame, bg="green")
greenFrame.place(x=60, y=60, width=300, height=300)
#greenFrame.place(y=60, relx=0.5,  relheight=0.8)

greenLabel_1 = tk.Label(greenFrame, text="this is the Green Frame")
greenLabel_1.pack()

# blue Frame ----------------------------------------------------
blueFrame = tk.Frame(my_bottom_frame, bg="blue", padx=5, pady=5)
blueFrame.place( x=100, y=100, width=300, height=300)

blueLabel_1 = tk.Label(blueFrame, text="this is the Blue Frame")
blueLabel_1.grid(column=0, row=0)

mainWin.mainloop()

#https://stackoverflow.com/questions/50422735/tkinter-resize-frame-and-contents-with-main-window

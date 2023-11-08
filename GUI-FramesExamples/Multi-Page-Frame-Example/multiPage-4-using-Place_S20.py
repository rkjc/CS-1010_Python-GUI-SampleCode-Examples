#https://stackoverflow.com/questions/50422735/tkinter-resize-frame-and-contents-with-main-window

import tkinter as tk
from tkinter import scrolledtext

mainwindow = tk.Tk()
mainwindow.title("Multi-window demo code - 3")
mainwindow.geometry("600x500")

mainwindow.columnconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=1)

def showRed():
    redFrame.tkraise()

def showGreen():
    greenFrame.tkraise()


def showBlue():
    blueFrame.tkraise()

# Parent widget for the buttons
top_frame = tk.Frame(mainwindow, bg="cyan", highlightbackground="black", highlightthickness=1)

top_frame.grid(row=0, column=0, columnspan=3, sticky=tk.N+tk.W+tk.E)

btn_r1 = tk.Button(top_frame, text='red', width='5', command=showRed)
btn_r1.grid(row=0, column=0, padx=(10), pady=10)

btn_g1 = tk.Button(top_frame, text='green', width='5', command=showGreen)
btn_g1.grid(row=0, column=1, padx=(10), pady=10)

btn_b1 = tk.Button(top_frame, text='blue', width='5', command=showBlue)
btn_b1.grid(row=0, column=2, padx=(10), pady=10)

# bottom Frame ----------------------------------------------------
bottom_frame = tk.Frame(mainwindow, bg="yellow", padx=5, pady=5)
bottom_frame.grid_propagate(False)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.NSEW))

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)

# red Frame ----------------------------------------------------
redFrame = tk.Frame(bottom_frame, bg="red", padx=5, pady=5)
redFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

redLabel_1 = tk.Label(redFrame, text="this is the Red Frame")
redLabel_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

btn_b2 = tk.Button(redFrame, fg="blue", text='blue', width='5', command=showBlue)
btn_b2.place(x=0, y=0)

btn_g2 = tk.Button(redFrame, fg="green", text='green', width='5', command=showGreen)
btn_g2.place(relx=1.0, y=0, anchor=(tk.NE))


# green Frame ----------------------------------------------------
greenFrame = tk.Frame(bottom_frame, bg="green", padx=5, pady=5)
greenFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

greenLabel_1 = tk.Label(greenFrame, text="this is the Green Frame")
greenLabel_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

btn_r3 = tk.Button(greenFrame, fg="red", text='red', width='5', command=showRed)
btn_r3.place(x=0, y=0)

btn_b3 = tk.Button(greenFrame, fg="blue", text='blue', width='5', command=showBlue)
btn_b3.place(relx=1.0, y=0, anchor=(tk.NE))



# blue Frame ----------------------------------------------------
blueFrame = tk.Frame(bottom_frame, bg="blue", padx=5, pady=5)
blueFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

blueLabel_1 = tk.Label(blueFrame, text="this is the Blue Frame")
blueLabel_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

btn_g4 = tk.Button(blueFrame, fg="green", text='green', width='5', command=showGreen)
btn_g4.place(x=0, y=0)

btn_r4 = tk.Button(blueFrame, fg="red", text='red', width='5', command=showRed)
btn_r4.place(relx=1.0, y=0, anchor=(tk.NE))


mainwindow.mainloop()

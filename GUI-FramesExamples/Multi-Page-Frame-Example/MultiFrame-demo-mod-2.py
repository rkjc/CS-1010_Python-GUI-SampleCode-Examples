#https://stackoverflow.com/questions/50422735/tkinter-resize-frame-and-contents-with-main-window

import tkinter as tk
from tkinter import scrolledtext

mainwindow = tk.Tk()
mainwindow.title("Multi-window demo code - 3")
mainwindow.geometry("680x500")

mainwindow.columnconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=1)

def showRed():
    redFrame.tkraise()

def showFrame_2():
    frame_2.tkraise()

def showBlue():
    blueFrame.tkraise()

def showFrame4():
    frame_4.tkraise()

# Parent widget for the buttons
top_frame = tk.Frame(mainwindow, highlightbackground="black", highlightthickness=1)

top_frame.grid(row=0, column=0, columnspan=3, sticky=tk.N+tk.W+tk.E)

btn_r1 = tk.Button(top_frame, text='Entry with Button', command=showRed)
btn_r1.grid(row=0, column=0, padx=(2))

btn_g1 = tk.Button(top_frame, text='Buttons and Labels', command=showFrame_2)
btn_g1.grid(row=0, column=1, padx=(2))

btn_b1 = tk.Button(top_frame, text='Radio Buttons', command=showBlue)
btn_b1.grid(row=0, column=2, padx=(2))

btn_b04 = tk.Button(top_frame, text='Image Selector', command=showFrame4)
btn_b04.grid(row=0, column=3, padx=(2))

# bottom Frame ----------------------------------------------------
bottom_frame = tk.Frame(mainwindow, bg="yellow")
bottom_frame.grid_propagate(False)
bottom_frame.grid(row=1, column=0, sticky=(tk.NSEW))

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)

# red Frame ----------------------------------------------------
redFrame = tk.Frame(bottom_frame, bg="red", padx=5, pady=5)
redFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

redLabel_1 = tk.Label(redFrame, text="this is the Red Frame")
redLabel_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



# Frame-2 ----------------------------------------------------
frame_2 = tk.Frame(bottom_frame, padx=5, pady=5)
frame_2.place(x=0, y=0, relwidth=1.0, relheight=1.0)

subFrame2 = tk.Frame(frame_2, padx=5, pady=5)
subFrame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

butt1 = False
butt2 = False

def thisButton():
    label_1.configure(text="you pushed the button 1")
    global butt1
    butt1 = True

def thatButton():
    other_label.configure(text="that was button 2")
    other_label.configure(foreground="blue", background="yellow")
    global butt2
    butt2 = True

def daFunctionDude():
    global butt1
    global butt2
    if (butt1 == True and butt2 == True):
        label_1.configure(text="I'm reset")
        other_label.configure(text="Also reset")
        butt1 = False
        butt2 = False

label_1 = tk.Label(subFrame2, text="A Label")
label_1.pack()

other_label = tk.Label(subFrame2, text="Label B - other")
other_label.pack()

button_1 = tk.Button(subFrame2, text="Button ONE", command=thisButton)
button_1.pack()

two_button = tk.Button(subFrame2, text="Button TWO", command=thatButton)
two_button.pack()

resetButt = tk.Button(subFrame2, text="do the reset", command=daFunctionDude)
resetButt.pack()



# blue Frame ----------------------------------------------------
blueFrame = tk.Frame(bottom_frame, bg="blue", padx=5, pady=5)
blueFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

blueLabel_1 = tk.Label(blueFrame, text="this is the Blue Frame")
blueLabel_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# Frame_4 ----------------------------------------------------
frame_4 = tk.Frame(bottom_frame, bg="orange", padx=5, pady=5)
frame_4.place(x=0, y=0, relwidth=1.0, relheight=1.0)

frame_4_label = tk.Label(frame_4, text="this is frame_4")
frame_4_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



mainwindow.mainloop()

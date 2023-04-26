import tkinter

groot = tkinter.Tk()
groot.geometry('600x400')

# ------------------variables --------------------
butt1 = False
butt2 = False

# ------------------- function definitions --------------
def thisButton():
    label_1.configure(text = "you pushed the button 1")
    global butt1
    butt1 = True
    
def thatButton():
    other_label.configure(text = "that was button 2")
    other_label.configure(foreground="red", background="yellow")
    global butt2
    butt2 = True

def daFunctionDude():
    global butt1
    global butt2
    if(butt1 == True and butt2 == True):
        label_1.configure(text = "I'm reset")
        other_label.configure(text = "Also reset")
        butt1 = False
        butt2 = False

# --------- making widgets ---------------

label_1 = tkinter.Label(groot, text="A Label")
other_label = tkinter.Label(groot, text="Label B - other")                     
button_1 = tkinter.Button(groot, text="Button ONE", command=thisButton)
two_button = tkinter.Button(groot, text="Button TWO", command=thatButton)
resetButt = tkinter.Button(groot, text="do the reset", command=daFunctionDude)

# --------- doing layout -----------------
label_1.pack()
other_label.pack()
button_1.pack()
two_button.pack()
resetButt.pack()


# ------ starting gui -------------                
groot.mainloop()

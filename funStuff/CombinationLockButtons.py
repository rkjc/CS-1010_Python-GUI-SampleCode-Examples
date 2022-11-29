import tkinter

# to unlock => True, False, True

root = tkinter.Tk()
#root.geometry("300x300")
#root.columnconfigure(0, minsize=100)
#root.columnconfigure(1, minsize=200)

buttonState_1 = False
buttonState_2 = False
buttonState_3 = False


def pushButton1():
    global buttonState_1
    buttonState_1 = not buttonState_1
    if (buttonState_1): # True makes it green
        bColor1 = 'green'
    else:
        bColor1 = 'red'
    button1.configure(bg=bColor1, highlightbackground = bColor1, activebackground = bColor1)
    checkUnlock()

def pushButton2():
    global buttonState_2
    buttonState_2 = not buttonState_2
    if (buttonState_2): # True makes it green
        bColor2 = 'green'
    else:
        bColor2 = 'red'
    button2.configure(bg=bColor2, highlightbackground = bColor2, activebackground = bColor2)
    checkUnlock()
    
def pushButton3():
    global buttonState_3
    buttonState_3 = not buttonState_3
    if (buttonState_3): # True makes it green
        bColor3 = 'green'
    else:
        bColor3 = 'red'
    button3.configure(bg=bColor3, highlightbackground = bColor3, activebackground = bColor3)
    checkUnlock()

def checkUnlock():
    if(buttonState_1 and not buttonState_2 and buttonState_3):
        lockLabel.config(bg="cyan", text="UNLOCKED")
    else:
        lockLabel.config(bg="orange", text="LOCKED")


button1 = tkinter.Button(root, text=" ONE ", command=pushButton1, width=10, height=3)
bColor1 = 'red'
button1.configure(background = bColor1)
button1.grid(row=0, column=0)

button2 = tkinter.Button(root, text=" TWO ", command=pushButton2, width=10, height=3)
bColor2 = 'red'
button2.configure(background = bColor2)
button2.grid(row=0, column=1)

button3 = tkinter.Button(root, text="THREE", command=pushButton3, width=10, height=3)
bColor3 = 'red'
button3.configure(background = bColor3)
button3.grid(row=0, column=2)

lockLabel = tkinter.Label(root, text="LOCKED", bg="orange", height=3)
lockLabel.grid(row=1, column=0, columnspan=3, sticky=(tkinter.EW))

root.mainloop()

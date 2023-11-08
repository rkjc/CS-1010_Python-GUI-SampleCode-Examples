
import tkinter

root = tkinter.Tk()
root.geometry("500x400")
root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=200)

buttonOn3 = False
buttonOn4 = False
buttonOn5 = False


def pushButton3():
    global buttonOn3
    if (buttonOn3):
        # turn it off
        bColor3 = 'red'
    else:
        # turn it on
        bColor3 = 'green'
    buttonOn3 = not buttonOn3
    button3.configure(background=bColor3,highlightbackground = bColor3, activebackground = bColor3)

def pushButton4():
    pass
def pushButton5():
    pass


button3 = tkinter.Button(root, text="Push 3", command=pushButton3)
bColor3 = 'green'
button3.configure(background = bColor3)
button3.grid(row=2, column=0)

button4 = tkinter.Button(root, text="Push 4", command=pushButton4)
bColor4 = 'green'
button4.configure(background = bColor4)
button4.grid(row=3, column=0)

button5 = tkinter.Button(root, text="Push 5", command=pushButton5)
bColor5 = 'green'
button5.configure(background = bColor5)
button5.grid(row=4, column=0)

root.mainloop()
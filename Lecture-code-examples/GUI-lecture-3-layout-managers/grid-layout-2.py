 
import tkinter as tk

main = tk.Tk()


def thisButton():
    label_1.configure(bg="red")
    label_2.configure(bg="blue")
    button_1.configure(bg="orange")

frame_1 = tk.Frame(main) 
 
label_10 = tk.Label(frame_1, text="Label one")
label_20 = tk.Label(frame_1, text="Label two")
button_10 = tk.Button(frame_1, text="Button ONE", command=thisButton)


button_10.pack(side="left", ipadx=50, padx=50, ipady=50)
label_10.pack(side=tk.RIGHT)
label_20.pack(side=tk.LEFT)

# --------- function defs ---------------
def setButtonColor(c1):
    but5.config(bg = c1, highlightbackground = c1, activebackground = c1)
 
def doBut1():
    label_1.configure(text="pressed ONE")
    setButtonColor('red')

def doBut2():
    label_1.configure(text="pressed TWO")
    setButtonColor('red')
 
def doBut3():
    label_1.configure(text="pressed THREE")
    setButtonColor('red')
 
def doBut4():
    label_1.configure(text="pressed FOUR")
    setButtonColor('red')
 
def doBut5():
    label_1.configure(text="reset")
    setButtonColor('green')
 

# --------- widgets ---------------------
label_1 = tk.Label(main, text="empty")
label_2 = tk.Label(main, text=". . .", bg="cyan")

but1 = tk.Button(main, text="ONE", command=doBut1, width=10)

but2 = tk.Button(main, text="TWO", command=doBut2, width=10)

but3 = tk.Button(main, text="THREE", command=doBut3, width=10)

but4 = tk.Button(main, text="FOUR", command=doBut4, width=10)

but5 = tk.Button(main, text="RESET", command=doBut5, width=10, bg='yellow')
setButtonColor('yellow')


# ------------ layout ------------------
label_1.grid(row=0, column=0, columnspan=2)
but1.grid(row=1, column=0)
but2.grid(row=1, column=1)
but3.grid(row=2, column=0)
label_2.grid(row=0, column=2, sticky=(tk.NSEW))
but4.grid(row=2, column=1)
frame_1.grid(row=1, column=2, sticky=(tk.NSEW), rowspan=2)

# ------------- start it up -----------------




main.mainloop()
                

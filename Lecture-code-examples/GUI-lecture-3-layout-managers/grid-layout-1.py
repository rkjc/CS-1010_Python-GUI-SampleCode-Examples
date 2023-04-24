 
import tkinter as tk

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
 
main = tk.Tk()
 
label_1 = tk.Label(main, text="empty")
label_1.grid(row=0, column=0, columnspan=2)
 
but1 = tk.Button(main, text="ONE", command=doBut1, width=10)
but1.grid(row=1, column=0)
 
but2 = tk.Button(main, text="TWO", command=doBut2, width=10)
but2.grid(row=1, column=1)
 
but3 = tk.Button(main, text="THREE", command=doBut3, width=10)
but3.grid(row=2, column=0)
 
but4 = tk.Button(main, text="FOUR", command=doBut4, width=10)
but4.grid(row=2, column=1)
 
but5 = tk.Button(main, text="RESET", command=doBut5, width=10, bg='yellow')
setButtonColor('yellow')
but5.grid(row=1, column=2, sticky=(tk.NSEW), rowspan=2)
 
main.mainloop()
                

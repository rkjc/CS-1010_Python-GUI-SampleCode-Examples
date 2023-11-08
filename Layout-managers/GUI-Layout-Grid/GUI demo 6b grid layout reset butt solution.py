import tkinter

def doBut1():
    label_1.configure(text = "pressed ONE")
    
def doBut2():
    label_1.configure(text = "pressed TWO")

def doBut3():
    label_1.configure(text = "pressed THREE")

def doBut4():
    label_1.configure(text = "pressed FOUR")

def doBut5():
    label_1.configure(text = "reset")


bob = tkinter.Tk()

label_1 = tkinter.Label(bob, text="empty")
label_1.grid(row=0, column=0, columnspan=2)



but1 = tkinter.Button(bob, text="ONE", command=doBut1, width=10)
but1.grid(row=1, column=0)

but2 = tkinter.Button(bob, text="TWO", command=doBut2, width=10)
but2.grid(row=1, column=1)

but3 = tkinter.Button(bob, text="THREE", command=doBut3, width=10)
but3.grid(row=2, column=0)

but4 = tkinter.Button(bob, text="FOUR", command=doBut4, width=10)
but4.grid(row=2, column=1)

but5 = tkinter.Button(bob, text="Reset", command=doBut5,width=10,height=3,bg="red")
but5.grid(row=1, rowspan=2, column=3)
          
                    
bob.mainloop()

import tkinter as tk
groot = tk.Tk()
groot.geometry("700x450")

# Need to use the special tkinter.IntVar() variable
# to connect the radio buttons together as a group
myIntThing = tk.IntVar()

# sets which button will be selected by default
myIntThing.set( 0 )


def doButt():
    temp_var = myIntThing.get()
    L1.configure(text=temp_var)

L2 = tk.Label(groot, text="volume control")
L2.pack()

L1 = tk.Label(groot, text="selection", font=('arial', 20))
L1.pack()

F1 = tk.Frame(groot)
F1.pack()

for c in range(11):
    for r in range(10):
        tempRadButt = tk.Radiobutton(F1)
        tempRadButt.config(text=str(c+(r*10)), variable=myIntThing, value=(c+(r*10)), command=doButt)
        tempRadButt.grid(column=c, row=r)


groot.mainloop()

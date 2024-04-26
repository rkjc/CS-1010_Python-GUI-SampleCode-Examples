import tkinter as tk
groot = tk.Tk()
groot.geometry("200x450")

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


for x in range(12):
    tempRadButt = tk.Radiobutton(groot)
    tempRadButt.config(text=str(x), variable=myIntThing, value=x, command=doButt)
    tempRadButt.pack()


groot.mainloop()
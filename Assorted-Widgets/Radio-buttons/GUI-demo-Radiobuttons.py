import tkinter as tk
groot = tk.Tk()
groot.geometry("200x200")

# Need to use the special tkinter.IntVar() variable
# (or tkinter.StringVar() or tkinter.DoubleVar() etc)
# to connect the radio buttons together as a group
# use my_tkVar.set() and my_tkVar.get() to
# set and get the value of this variable for the radio buttons
my_tkVar = tk.IntVar()

# sets which button will be selected by default
my_tkVar.set(2)


def doButt():
    temp_var = my_tkVar.get()
    L1.configure(text=temp_var)

L1 = tk.Label(groot, text="selection", font=('arial', 20))
L1.pack()

my_radio_1 = tk.Radiobutton(groot)
my_radio_1.config(text="Radiobutton 1", variable=my_tkVar, value=1)

my_radio_2 = tk.Radiobutton(groot)
my_radio_2.config(text="Radiobutton 2", variable=my_tkVar, value=2)

my_radio_3 = tk.Radiobutton(groot)
my_radio_3.config(text="Radiobutton 3", variable=my_tkVar, value=3)

my_radio_1.pack()
my_radio_2.pack()
my_radio_3.pack()

L2 = tk.Label(groot, text="---------------------------")
L2.pack()

B1 = tk.Button(groot, text="push", command=doButt)
B1.pack()

groot.mainloop()
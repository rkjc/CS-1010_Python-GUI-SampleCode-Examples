import tkinter as tk
groot = tk.Tk()
groot.geometry("300x500")

# =============================================================

def doButt():
    temp_var = radioVar.get()
    L1.configure(text=temp_var)
    label_3.configure(text=checkBxVar_1.get())
    label_4.configure(text=checkBxVar_2.get())
    label_5.configure(text=checkBxVar_3.get())

# =============================================================
# Need to use the special tkinter.IntVar() variable
# to connect the radio buttons together as a group
radioVar = tk.StringVar()

# sets which button will be selected by default
radioVar.set(2)

checkBxVar_1 = tk.IntVar()
checkBxVar_2 = tk.IntVar()
checkBxVar_3 = tk.IntVar()

# =============================================================

L1 = tk.Label(groot, text="selection", font=('arial', 20))
L2 = tk.Label(groot, text="checkbutton selection")
label_3 = tk.Label(groot, text="checked state")
label_4 = tk.Label(groot, text="checked state")
label_5 = tk.Label(groot, text="checked state")


my_radio_1 = tk.Radiobutton(groot)
my_radio_1.config(text="animal 1", variable=radioVar, value="dog", command=doButt)

my_radio_2 = tk.Radiobutton(groot)
my_radio_2.config(text="animal 2", variable=radioVar, value='cat', command=doButt)

my_radio_3 = tk.Radiobutton(groot)
my_radio_3.config(text="animal 3", variable=radioVar, value='frog', command=doButt)

my_checkbutton_1 = tk.Checkbutton(groot, text="Checkbutton 1", variable=checkBxVar_1)
my_checkbutton_2 = tk.Checkbutton(groot, text="Checkbutton 2", variable=checkBxVar_2)
my_checkbutton_3 = tk.Checkbutton(groot, text="Checkbutton 3", variable=checkBxVar_3)

# set which button is pre-checked (can be more than one)
my_checkbutton_1.select()

B1 = tk.Button(groot, text="push", command=doButt)

# =============================================================

L1.pack()

my_radio_1.pack()
my_radio_2.pack()
my_radio_3.pack()

my_checkbutton_1.pack()
my_checkbutton_2.pack()
my_checkbutton_3.pack()

L2.pack()
label_3.pack()
label_4.pack()
label_5.pack()

B1.pack()
# =============================================================
groot.mainloop()


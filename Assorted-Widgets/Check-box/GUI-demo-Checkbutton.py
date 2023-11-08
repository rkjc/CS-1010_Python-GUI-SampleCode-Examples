import tkinter as tk
groot = tk.Tk()
groot.geometry("200x220")
groot.title("GUI Checkbuttons")

# need to use my_bool#.set() and my_bool#.get() to
# set and get the value of these variables for the check boxes
my_bool1 = tk.BooleanVar()
my_bool2 = tk.BooleanVar()
my_bool3 = tk.BooleanVar()

def doButt():
    label_3.configure(text=my_bool1.get())
    label_4.configure(text=my_bool2.get())
    label_5.configure(text=my_bool3.get())

label_3 = tk.Label(groot, text="checked state")
label_4 = tk.Label(groot, text="checked state")
label_5 = tk.Label(groot, text="checked state")

B2 = tk.Button(groot, text="push", command=doButt)

my_checkbutton_1 = tk.Checkbutton(groot, text="Checkbutton 1", var=my_bool1)
my_checkbutton_2 = tk.Checkbutton(groot, text="Checkbutton 2", var=my_bool2)
my_checkbutton_3 = tk.Checkbutton(groot, text="Checkbutton 3", var=my_bool3)

# set which button is pre-checked (can be more than one)
my_checkbutton_1.select()

my_checkbutton_1.pack()
my_checkbutton_2.pack()
my_checkbutton_3.pack()

label_3.pack()
label_4.pack()
label_5.pack()

B2.pack()

groot.mainloop()

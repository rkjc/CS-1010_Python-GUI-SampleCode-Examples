import tkinter as tk

my_window = tk.Tk(className='Color Changer')
my_window.minsize(300, 250)

# define the functions
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

def setColor():
    picked = listbox_1.curselection()
    temp_text = listbox_1.get(picked)
    if temp_text == 'custom':
        setCustomColor()
    else:
        lb_1.configure(text=temp_text)
        my_window.config(bg=temp_text)

def setCustomColor():
    # get spinbox r g b
    cR = int(spin_R.get())
    cG = int(spin_G.get())
    cB = int(spin_B.get())
    lblText = ("color values are - " + ' ' + str(cR) + ' ' + str(cG) + ' ' + str(cB))
    lb_1.configure(text=lblText)
    # set color using RGB
    my_window.config(bg=rgb_hack((cR, cG, cB)))


# define the widgets
listbox_1 = tk.Listbox(my_window, selectmode=tk.SINGLE, height="7")
listbox_1.insert(tk.END, 'red')
listbox_1.insert(tk.END, 'blue')
listbox_1.insert(tk.END, 'green')
listbox_1.insert(tk.END, 'orange')
listbox_1.insert(tk.END, 'cyan')
listbox_1.insert(tk.END, 'gray')
listbox_1.insert(tk.END, 'custom')
listbox_1.pack()
listbox_1.select_set(3)

spin_R = tk.Spinbox(my_window, from_=0, to=254, increment=20, width=5)
spin_G = tk.Spinbox(my_window, from_=0, to=254, increment=20, width=5)
spin_B = tk.Spinbox(my_window, from_=0, to=254, increment=20, width=5)

bt_1 = tk.Button(my_window, text='Set Color', command=setColor)

lb_1 = tk.Label(my_window, text='your selection')

# layout the GUI
spin_R.pack()
spin_G.pack()
spin_B.pack()

bt_1.pack()
lb_1.pack()

# start the GUI
my_window.mainloop()
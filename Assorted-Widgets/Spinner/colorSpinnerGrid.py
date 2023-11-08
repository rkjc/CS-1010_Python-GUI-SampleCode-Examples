import tkinter as tk

root = tk.Tk()

root.config(bg="#ff00ff")

def rgb_hex(r,g,b):
    color_str = '#' + ("%0.2X" % (int(r))) + ("%0.2X" % (int(g))) + ("%0.2X" % (int(b)))
    return color_str

def change_color():
    color_str_r = spin_r.get()
    color_str_g = spin_g.get()
    color_str_b = spin_b.get()
    hex_color = rgb_hex(color_str_r,color_str_g,color_str_b)
    L5.config(text=hex_color)
    L4.config(bg=hex_color)

frm1 = tk.Frame(root, padx=10, pady=10)
frm2 = tk.Frame(root,padx=10, pady=10, highlightbackground="black", highlightthickness=2)
frm3 = tk.Frame(root, padx=10, pady=10)

L1 = tk.Label(frm1, height = 3, width=20, bg="red")
L2 = tk.Label(frm1, height = 3, width=20, bg="blue")
L3 = tk.Label(frm1, height = 3, width=20, bg="green")
L4 = tk.Label(frm1, height = 3, width=20, bg="cyan")

L5 = tk.Label(frm2, text="#000000")

L1.grid(column=0, row=0)
L2.grid(column=0, row=1)
L3.grid(column=1, row=0)
L4.grid(column=1, row=1)

spin_r = tk.Spinbox(frm3, from_ = 0, to = 255, repeatinterval=20, repeatdelay=50, command=change_color)
spin_b = tk.Spinbox(frm3, from_ = 0, to = 255, repeatinterval=20, repeatdelay=50, command=change_color)
spin_g = tk.Spinbox(frm3, from_ = 0, to = 255, repeatinterval=20, repeatdelay=50, command=change_color)


B1 = tk.Button(frm2, text = "push this", command=change_color)

L5.pack()
#B1.pack()
spin_r.pack()
spin_g.pack()
spin_b.pack()

frm1.pack()
frm2.pack(side=tk.LEFT)
frm3.pack(side=tk.RIGHT)

root.mainloop()
import tkinter as tk
root = tk.Tk()
root.geometry("400x400")

def motion(event):
    x = event.x
    y = event.y
    lbl_x.config(text=x)
    lbl_y.config(text=y)
    abs_x = root.winfo_pointerx()
    abs_y = root.winfo_pointery()
    lbl_absx.config(text=abs_x)
    lbl_absy.config(text=abs_y)
    if 280 < x and x < 340 and 300 < y and y < 360:
        root.config(bg='red')
    if 50 < x and x < 90 and 200 < y and y < 240:
            root.config(bg='green')

lblfrm_1 = tk.LabelFrame(root, text="relative")
lblfrm_2 = tk.LabelFrame(root, text="absolute")

lbl_x = tk.Label(lblfrm_1, text="x-coord", font=(None, 20))
lbl_y = tk.Label(lblfrm_1, text="y-coord", font=(None, 20))
lbl_absx = tk.Label(lblfrm_2, text="x-coord", font=(None, 24))
lbl_absy = tk.Label(lblfrm_2, text="y-coord",  font=(None, 24))

lblfrm_1.pack()
lblfrm_2.pack()
lbl_x.pack(side=tk.LEFT, padx = 5)
lbl_y.pack(side=tk.LEFT, padx = 5)
lbl_absx.pack(side=tk.LEFT, padx = 5)
lbl_absy.pack(side=tk.LEFT, padx = 5)

root.bind('<Motion>', motion)


root.mainloop()

# https://stackoverflow.com/questions/22925599/mouse-position-python-tkinter

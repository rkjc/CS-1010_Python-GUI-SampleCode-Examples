import tkinter as tk
root = tk.Tk()
root.geometry("400x400")

def motion(event):
    x = event.x
    y = event.y
    lbl_x.config(text=x)
    lbl_y.config(text=y)
    if 280 < x and x < 340 and 300 < y and y < 360:
        root.config(bg='red')
    if 50 < x and x < 90 and 200 < y and y < 240:
            root.config(bg='green')

lblfrm_1 = tk.LabelFrame(root, text="relative")

lbl_x = tk.Label(lblfrm_1, text="x-coord")
lbl_y = tk.Label(lblfrm_1, text="y-coord")

lblfrm_1.pack()
lbl_x.pack(side=tk.LEFT, padx = 5)
lbl_y.pack(side=tk.LEFT, padx = 5)

root.bind('<Motion>', motion)
root.mainloop()

# https://stackoverflow.com/questions/22925599/mouse-position-python-tkinter

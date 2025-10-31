 
import tkinter as tk

def create_shadow(canv_in, text, font, color, offset):
    x = int(canv_in.winfo_reqwidth() / 2)
    y = int(canv_in.winfo_reqheight() / 2)
    canv_in.create_text(x + offset, y + offset, text=text, font=font, fill='gray70')
    canv_in.create_text(x, y, text=text, font=font, fill=color)
    print( canv_in.winfo_reqheight(), canv_in.winfo_reqwidth() )

root = tk.Tk()

can_vas1 = tk.Canvas(root, width=300, height=100, bg='cyan')
can_vas1.pack()

label_font = ('Arial', 24)
label_text = 'Hello, Shadow!'

shadow_offset = 3

create_shadow(can_vas1, label_text, label_font, 'black', shadow_offset)

root.mainloop()


# https://www.demo2s.com/g/python/how-to-add-shadow-in-tkinter-label-in-python.html 

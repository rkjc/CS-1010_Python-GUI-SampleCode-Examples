from tkinter import *

groot = Tk()
groot.geometry('400x300')


width = groot.winfo_width()
height = groot.winfo_height()

print("groot.winfo_width()", groot.winfo_width())

def show_size(event):
    label_w.config(text= groot.winfo_width())
    label_h.config(text= groot.winfo_height())

label_w = Label(groot, text=width)
label_h = Label(groot, text=height)


label_w.pack()
label_h.pack()

groot.bind('<Configure>', show_size)

groot.mainloop()

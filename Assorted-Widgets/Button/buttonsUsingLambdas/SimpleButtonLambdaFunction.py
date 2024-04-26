import tkinter
window = tkinter.Tk()


def click(value):
    label.config(text=value)


button = tkinter.Button(window, text='send 1', command=lambda: click(1))
button.pack()
button = tkinter.Button(window, text='send 7', command=lambda: click(7))
button.pack()
label = tkinter.Label(window, text="number goes here")
label.pack()
window.mainloop()
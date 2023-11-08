import tkinter

# for more complicated image manipulation checkout the PIL pillow library
# https://github.com/python-pillow/Pillow

root = tkinter.Tk()
root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=200)

def doButton1():
    label_1.config(image=img1)


#images have to be .png, .jpg does not work.
#img1 = tkinter.PhotoImage(file="beetleBug-still.gif")
#img1 = tkinter.PhotoImage(file="brownMouse.tif")
img1 = tkinter.PhotoImage(file="Anime-Astronaut.png")
img1sm = img1.subsample(5)


label_1 = tkinter.Label(root, text="images")
label_1.grid(row=1, rowspan=3, column=1)

MyButton1 = tkinter.Button(root, image=img1sm, text="b1", bg="blue",width=100, height=100, command = lambda: doButton1())
MyButton1.grid(row=1, column=0)


root.mainloop()

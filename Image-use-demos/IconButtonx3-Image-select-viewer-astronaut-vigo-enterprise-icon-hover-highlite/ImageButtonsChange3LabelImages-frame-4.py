import tkinter

root = tkinter.Tk()
root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=200)

def doButton1():
    #label_1.config(image=img01_size_2)
    label_1.config(image=img01)
    label_2.config(text="Image One")

def doButton2():
    label_1.config(image=img02)
    label_2.config(text="Image Two")

def doButton3():
    label_1.config(image=img03)
    label_2.config(text="Image Three")

#images have to be .png, .jpg does not work.
img01 = tkinter.PhotoImage(file="Space_Woman_500.png")
img01_thumb = img01.subsample(4)

img02 = tkinter.PhotoImage(file="vigo_500.png")
img02_thumb = img02.subsample(4)

img03 = tkinter.PhotoImage(file="Enterprise_500.png")
img03_thumb = img03.subsample(4)

label_1 = tkinter.Label(root, text="images")
label_1.grid(row=1, rowspan=3, column=1)

label_2 = tkinter.Label(root, text="select an image")
label_2.grid(row=0, column=1)

MyButton1 = tkinter.Button(root, image=img01_thumb, text="b1", bg="blue", width=100, height=100, command = lambda: doButton1())
MyButton1.grid(row=1, column=0)

MyButton1 = tkinter.Button(root, image=img02_thumb, text="b2", bg="blue",width=100, height=100, command = lambda: doButton2())
MyButton1.grid(row=2, column=0)

MyButton1 = tkinter.Button(root, image=img03_thumb, text="b3", bg="blue",width=100, height=100, command = lambda: doButton3())
MyButton1.grid(row=3, column=0)


root.mainloop()

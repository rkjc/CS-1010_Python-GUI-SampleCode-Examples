import tkinter

root = tkinter.Tk()
root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=200)


#images have to be .png, .jpg does not work.
img01 = tkinter.PhotoImage(file="Space_Woman_500.png")


label_1 = tkinter.Label(root, text="images", image=img01)
label_1.grid(row=1, rowspan=3, column=1)


root.mainloop()

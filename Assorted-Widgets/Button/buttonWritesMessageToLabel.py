import tkinter

def doButton():
  label_1.configure(text = "you pushed the button")

bob = tkinter.Tk()
bob.geometry('200x100')

label_1 = tkinter.Label(bob, text="A Label")
label_1.pack()

button_1 = tkinter.Button(bob, text="A Button", command=doButton)
button_1.pack()

bob.mainloop()

import tkinter

def doButton():
  label_1.configure(text = "you pushed the button")
  print("in the function")

bob = tkinter.Tk()
bob.geometry('400x120')

myfont = ("", 24)

label_1 = tkinter.Label(bob, text="A Label", font=myfont)
label_1.pack()

button_1 = tkinter.Button(bob, text="A Button", font=myfont, command=doButton)
button_1.pack()

bob.mainloop()

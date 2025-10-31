import tkinter

bob = tkinter.Tk()
bob.geometry('300x150')

myfont = ("", 24)

zim = tkinter.Label(bob, bg="cyan", text="  Hello World   ", font=myfont )
zim.pack()


bob.mainloop()
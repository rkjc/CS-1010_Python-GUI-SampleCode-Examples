import tkinter

bob = tkinter.Tk()
bob.geometry('300x150')

zim = tkinter.Label(bob, bg="cyan", text=" Hello World ", font=("", 24))
zim.pack()

bob.mainloop()
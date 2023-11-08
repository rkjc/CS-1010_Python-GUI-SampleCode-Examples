from tkinter import *

root = Tk()
root.config(height=300, width=300, bg="yellow")
root.pack()

frame1 = Frame(root)
frame1.config(height=250, width=250, bg="green")
frame1.pack()

##bottomframe = Frame(root)
##bottomframe.pack( side = BOTTOM )
##
##redbutton = Button(frame, text="Red", fg="red")
##redbutton.pack( side = LEFT)
##
##greenbutton = Button(frame, text="Brown", fg="brown")
##greenbutton.pack( side = LEFT )
##
##bluebutton = Button(frame, text="Blue", fg="blue")
##bluebutton.pack( side = LEFT )
##
##blackbutton = Button(bottomframe, text="Black", fg="black")
##blackbutton.pack( side = BOTTOM)

root.mainloop()

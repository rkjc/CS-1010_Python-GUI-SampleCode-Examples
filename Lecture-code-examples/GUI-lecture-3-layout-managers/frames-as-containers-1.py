 
from tkinter import *
  
groot = Tk()
groot.title("GUI-Frames-pack-demo")
  
my_topframe = Frame(groot)
# my_topframe.configure(highlightbackground="orange", highlightthickness=4)
my_topframe.pack()
  
my_bottomframe = Frame(groot)
# my_bottomframe.configure(bg="green")
# my_bottomframe.configure(padx=20, pady=20)
# my_bottomframe.configure(highlightbackground="black", highlightthickness=4)
my_bottomframe.pack()
  
redbutton = Button(my_topframe, text = "Red", fg = "red")
redbutton.pack( side = LEFT)
  
greenbutton = Button(my_topframe, text = "Brown", fg="brown")
greenbutton.pack( side = LEFT )
  
bluebutton = Button(my_topframe, text = "Blue", fg = "blue")
bluebutton.pack( side = LEFT )
  
blackbutton = Button(my_bottomframe, text = "Black", fg = "black")
blackbutton.pack()
  
groot.mainloop()

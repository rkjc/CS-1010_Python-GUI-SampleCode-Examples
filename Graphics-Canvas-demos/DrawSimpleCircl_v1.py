 
#Import the library
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Define the geometry of window
win.geometry("600x400")

#Create a canvas object
c= Canvas(win,width=400, height=400, bg='#2200ff')
c.pack()

#Draw an Oval in the canvas
c.create_oval(60,60,210,210)

win.mainloop()
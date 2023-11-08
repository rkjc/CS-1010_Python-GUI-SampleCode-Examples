from tkinter import *
import PIL
from PIL import Image


class App(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid(row=0)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        myImage = Image.open('example.png')
        myImage.load()
        self.display = Label(self,image=myImage)
        self.display.grid(row=0)

root = Tk()
app = App(root)
app.mainloop()
root.destroy()

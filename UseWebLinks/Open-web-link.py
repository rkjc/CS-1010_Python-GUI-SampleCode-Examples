from tkinter import *
import webbrowser

groot = Tk()

url = "https://gist.github.com/RandomResourceWeb/93e887facdb98937ab5d260d1a0df270"

def openweb():
    webbrowser.open(url)

Btn = Button(groot, text = "This opens a web page",command=openweb)
Btn.pack()

groot.mainloop()
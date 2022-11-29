from tkinter import *
import webbrowser

groot = Tk()
groot.geometry("200x80")

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def openweb():
    webbrowser.open(url)

Btn = Button(groot, text = "push button to\nopen a web page",command=openweb)
Btn.pack()

groot.mainloop()

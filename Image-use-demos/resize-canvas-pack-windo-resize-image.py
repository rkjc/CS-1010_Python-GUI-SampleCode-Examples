from tkinter import *
from PIL import ImageTk, Image

def resize_widgets(event):
    global resized 
    for items in canvas.find_all():
        if items != image:
            canvas.coords(items, 0, 0, event.width, event.height)

    resized = ImageTk.PhotoImage(im.resize((event.width, event.height), resample = Image.NEAREST))
    canvas.itemconfig(image, image=resized)
    canvas.moveto(image, 0, 0)
    
win = Tk()
win.title("Canvas and image resizes to window dimention changes")
win.geometry("600x600")
win.resizable()
w = 700
h = 700
x = 600 // 2
y = 600 // 2

# photo image object referance store - avoids garbage collection
resized = None

canvas = Canvas(win, width=w, height=h, bg="grey")

canvas.pack(expand=True, fill='both')
canvas.bind('<Configure>', resize_widgets)

im = Image.open("chameleon_tr.png")
img = ImageTk.PhotoImage(im)


canvas.create_rectangle(0, 0, 75, 500, fill="green")
item = canvas.create_rectangle(425, 0, 500, 500, fill="green")
canvas.create_rectangle(75, 0, 80, 500, fill="brown")

image = canvas.create_image(x, 440, image=img)

win.mainloop()
    
'''
https://stackoverflow.com/questions/65606641/how-to-to-resize-canvas-objects-to-window-size-in-tkinter-without-using-object-o 

You can resize all the items in the canvas using the Canvas.coords(tagorId, x0, y0...). This can be used for any item in the canvas other than the image. For image use Image.resize((x, y), resample).

Bind the <Configure> event to an event handler. So whenever the canvas is resized the event handler is called.

Here is a demo.(Note the other items on the canvas might be hidden by the image). The below code will automatically resize items to the canvas.
'''

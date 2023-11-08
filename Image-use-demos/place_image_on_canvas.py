
import tkinter as tk
from PIL import Image, ImageTk

win = tk.Tk()
win.geometry('1000x1000+1200+1000')


img1 = Image.open('chameleonOnTransparent.png')
img1 = img1.convert("RGBA")
#img1.putalpha(48)
photo1 = ImageTk.PhotoImage(img1)

width1, height1 = photo1.width(), photo1.height()
canvas1 = tk.Canvas(win, bg="white", width=900, height=900)

canvas1.create_image(0,0, image=photo1, anchor=tk.NW)
canvas1.place(x=50, y=20)


img2 = Image.open("policecats1.png")
img2 = img2.convert("RGBA")
img2c = img2.copy()
#img2c.putalpha(128)
iWd2, iHt2 = img2.size
i2scale = 0.3
new2wd = int(iWd2 * i2scale)
new2ht = int(iHt2 * i2scale)
img2c = img2c.resize((new2wd, new2ht))

photo2 = ImageTk.PhotoImage(img2c)

ph2_id = canvas1.create_image(800,400, image=photo2)

width2, height2 = photo2.width(), photo2.height()
#canvas2 = tk.Canvas(win, bg="red", width=width2, height=height2)

#canvas2.create_image(0, 0, image=photo2, anchor=tk.NW)
#canvas2.place(x=100, y=40)

win.mainloop() 

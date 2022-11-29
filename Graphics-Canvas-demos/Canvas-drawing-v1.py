 
from tkinter import *
import random

groot = Tk()
groot.title("Drawing V1")
#groot.geometry("400x400")


# ====================================Functions==============================================

def counter():
    global count
    count -= 5
    label_1.config(text=count)
    draw_area.coords(image_1, 450, count)
    if count > -300:
        groot.after(40, counter)
    else:
        count = 600


# ==================================== Variables ==============================================

count = 600

# ==================================== widgets ========================

draw_area = Canvas(groot)
draw_area.create_oval(125, 100, 175, 50, width=3, fill="cyan")
draw_area.create_line(370, 20, 70, 250, width=5, fill="blue")
draw_area.create_line(70, 20, 150, 20, width=2)
draw_area.create_line(150, 20, 150, 50, width=2)

draw_area.create_polygon(250, 150, 350, 150, 300, 325, width=2)

coord = 210, 50, 440, 210
arc = draw_area.create_arc(coord, start=0, extent=150, fill="red")
draw_area.create_line(400, 50, 100, 280, width=10, fill="green")

img_file = PhotoImage(file = "falcon9.png")
img_file_sm = img_file.subsample(2)
image_1 = draw_area.create_image(450, count, image=img_file_sm)

label_1 = Label(groot, text=count)

test_button = Button(groot, text="count", command=counter)


# ====================================Outputs==============================================
test_button.pack()
label_1.pack()

draw_area.pack()

groot.mainloop()


# https://coderslegacy.com/python/tkinter-canvas/


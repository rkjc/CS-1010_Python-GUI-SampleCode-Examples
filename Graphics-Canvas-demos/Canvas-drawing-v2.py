 
from tkinter import *
import random

groot = Tk()
groot.title("Drawing V1")
#groot.geometry("400x400")

draw_area = Canvas(groot)
# ====================================Functions==============================================

def counter():
    global count
    count -= 5


def motion(event):
    x = event.x
    y = event.y
    lbl_x.config(text=x)
    lbl_y.config(text=y)

def button_down(event):
    global x_start
    global y_start
    x_start = event.x
    y_start = event.y

def button_release(event):
    global x_end
    global y_end
    x_end = event.x
    y_end = event.y
    draw_line(x_start, y_start, x_end, y_end)

def draw_line(x1, y1, x2, y2):
    draw_area.create_line(x1, y1, x2, y2, width=2)

# ==================================== Variables ==============================================

count = 600
x_start = 0
y_start = 0
x_end = 0
y_end = 0

# ==================================== widgets ========================



lblfrm_1 = LabelFrame(groot, text="relative")
lbl_x = Label(lblfrm_1, text="x-coord")
lbl_y = Label(lblfrm_1, text="y-coord")
lblfrm_1.pack()
lbl_x.pack(side=LEFT, padx = 5)
lbl_y.pack(side=LEFT, padx = 5)

label_1 = Label(lblfrm_1, text=count)
test_button = Button(lblfrm_1, text="count", command=counter)
# ====================================Outputs==============================================
test_button.pack()
label_1.pack()

draw_area.pack()

groot.bind('<Motion>', motion)
groot.bind( "<Button-1>", button_down )
groot.bind( "<ButtonRelease-1>", button_release )
groot.mainloop()


# https://coderslegacy.com/python/tkinter-canvas/


# draw_area.create_oval(125, 100, 175, 50, width=3, fill="cyan")
# draw_area.create_line(370, 20, 70, 250, width=5, fill="blue")
# draw_area.create_line(70, 20, 150, 20, width=2)
# draw_area.create_line(150, 20, 150, 50, width=2)
#
# draw_area.create_polygon(250, 150, 350, 150, 300, 325, width=2)
#
# coord = 210, 50, 440, 210
# arc = draw_area.create_arc(coord, start=0, extent=150, fill="red")
# draw_area.create_line(400, 50, 100, 280, width=10, fill="green")
#
# img_file = PhotoImage(file = "falcon9.png")
# img_file_sm = img_file.subsample(2)
# image_1 = draw_area.create_image(450, count, image=img_file_sm)
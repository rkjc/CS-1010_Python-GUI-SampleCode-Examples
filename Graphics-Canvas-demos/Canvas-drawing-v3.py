 
from tkinter import *
import random

groot = Tk()
groot.title("Drawing V1")
#groot.geometry("400x400")


# ====================================Functions==============================================

def motion(event):
    global button_is_down
    x = event.x
    y = event.y
    lbl_x.config(text=x)
    lbl_y.config(text=y)
    if button_is_down == True:
        undo_stretchy()
        stretchy_line_list.append(draw_area.create_line(x_start, y_start, x, y))
        print("line_list size ", len(line_list))

def button_down(event):
    global button_is_down
    button_is_down = True
    global x_start
    global y_start
    x_start = event.x
    y_start = event.y


def button_release(event):
    global button_is_down
    button_is_down = False
    undo_stretchy()
    global x_end
    global y_end
    x_end = event.x
    y_end = event.y
    line_list.append(draw_area.create_line(x_start, y_start, x_end, y_end))
    print("line_list size (button up) ", len(line_list))
#
# def draw_line(x1, y1, x2, y2):
#     draw_area.create_line(x1, y1, x2, y2, width=2)

def undo_last():
    if len(line_list) > 0:
        l1 = line_list.pop()
        draw_area.delete(l1)
        print("line_list size (undo) ", len(line_list))

def undo_stretchy():
    if len(stretchy_line_list) > 0:
        l1 = stretchy_line_list.pop()
        draw_area.delete(l1)
        print("line_list size (undo) ", len(stretchy_line_list))

def undo_all():
    for l1 in line_list:
        draw_area.delete(l1)
        print("line_list size ", len(line_list))
    line_list.clear()

# ==================================== Variables ==============================================
button_is_down = False
line_list = []
stretchy_line_list = []
count = 600
x_start = 0
y_start = 0
x_end = 0
y_end = 0

# ==================================== widgets ========================

draw_area = Canvas(groot)

lblfrm_1 = LabelFrame(groot, text="relative")
lbl_x = Label(lblfrm_1, text="x-coord")
lbl_y = Label(lblfrm_1, text="y-coord")
lblfrm_1.pack()
lbl_x.pack(side=LEFT, padx = 5)
lbl_y.pack(side=LEFT, padx = 5)

#label_1 = Label(lblfrm_1, text=count)
btn_1 = Button(lblfrm_1, text="undo last", command=undo_last)
btn_2 = Button(lblfrm_1, text="undo all", command=undo_all)
# ====================================Outputs==============================================

btn_2.pack(side=RIGHT)
btn_1.pack(side=RIGHT)
draw_area.pack()

draw_area.bind('<Motion>', motion)
draw_area.bind( "<Button-1>", button_down )
draw_area.bind( "<ButtonRelease-1>", button_release )
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
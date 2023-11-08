
from tkinter import *
from random import *

groot = Tk()
groot.title("Drawing delete practice")
# groot.geometry("400x400")

draw_area = Canvas(groot)
# ====================================Functions==============================================

def draw_rnd_line():
    line_list.append(draw_area.create_line(randint(10, 580), randint(10, 380), randint(10, 580), randint(10, 380)))
    print("line_list size ", len(line_list))

# def draw_line(x1, y1, x2, y2):
#     draw_area.create_line(x1, y1, x2, y2, width=2)

def undo_last():
    if len(line_list) > 0:
        l1 = line_list.pop()
        draw_area.delete(l1)
        print("line_list size ", len(line_list))

# ==================================== Variables ==============================================

line_list = []

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

drawAline = Button(lblfrm_1, text="Draw line", command=draw_rnd_line)
btn_2 = Button(lblfrm_1, text="undo", command=undo_last)
# ====================================Outputs==============================================
btn_2.pack(side=RIGHT)
drawAline.pack(side=RIGHT)
draw_area.pack()

groot.mainloop()

# https://coderslegacy.com/python/tkinter-canvas/

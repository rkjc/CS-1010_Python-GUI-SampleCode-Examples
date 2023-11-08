from tkinter import *
import random

groot = Tk()
groot.title("Drawing V1")
# groot.geometry("400x400")

draw_area = Canvas(groot)

# ====================================Functions==============================================

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
    item = draw_area.create_line(x_start, y_start, x_end, y_end)
    lineList.append(item)

item = draw_area.create_line(0,0,0,0)

def draw_line(x1, y1, x2, y2):
    draw_area.create_line(x1, y1, x2, y2, width=2)

def makeAline():
    global item
    item = draw_area.create_line(50, 40, 200, 150, width=2)
    # lineList.append(item)


def eraseAline():
    global item
    # item = lineList.pop()
    draw_area.delete(item)

# ==================================== Variables ==============================================
lineList = []

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
lbl_x.pack(side=LEFT, padx=5)
lbl_y.pack(side=LEFT, padx=5)

label_1 = Label(lblfrm_1, text=count)
test_button = Button(lblfrm_1, text="make line", command=makeAline)
test_button2 = Button(lblfrm_1, text="erase line", command=eraseAline)

# ====================================Outputs==============================================
test_button.pack()
test_button2.pack()

draw_area.pack()

groot.bind('<Motion>', motion)
groot.bind("<Button-1>", button_down)
groot.bind("<ButtonRelease-1>", button_release)
groot.mainloop()


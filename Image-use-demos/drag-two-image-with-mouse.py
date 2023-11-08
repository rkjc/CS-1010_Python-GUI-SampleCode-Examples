#moving an item on a canvas
#https://stackoverflow.com/questions/6740855/board-drawing-code-to-move-an-oval/6789351#6789351 

import tkinter as tk
from PIL import Image, ImageTk

win = tk.Tk()
win.geometry('1000x1000+1200+1000')

# --- make a canvas -----

canvas1 = tk.Canvas(win, bg="white", width=900, height=900)
canvas1.place(x=50, y=20)

# --- mouse and actions ----
drag_data = {"x": 0, "y": 0, "item": None}


def id_item(event):
    print("coords", canvas1.coords("current"))
    print("bbox", canvas1.bbox("current"))  # returns a tuple like (x1, y1, x2, y2)
    print("get tags", canvas1.gettags("current"))
    print("find below", canvas1.find_below("current"))
    canvas1.lift("current")
            # record the item and its location
    drag_data["item"] = canvas1.find_closest(event.x, event.y)[0]
    drag_data["x"] = event.x
    drag_data["y"] = event.y
    
    item = canvas1.find_closest(event.x, event.y)
    item_type = canvas1.type(item)
    print(item_type)
    if item_type != "image":
        current_color = canvas1.itemcget(item, 'fill')
        print("current color", current_color)
        if current_color == 'black':
            canvas1.itemconfig(item, fill='white')
        else:
            canvas1.itemconfig(item, fill='black')

def lower_item(event):
    canvas1.lower("current")

def drag_start(event):
        """Begining drag of an object"""
        # record the item and its location
        drag_data["item"] = canvas1.find_closest(event.x, event.y)[0]
        drag_data["x"] = event.x
        drag_data["y"] = event.y

def drag_stop(event):
        """End drag of an object"""
        # reset the drag information
        drag_data["item"] = None
        drag_data["x"] = 0
        drag_data["y"] = 0

def drag(event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - drag_data["x"]
        delta_y = event.y - drag_data["y"]
        # move the object the appropriate amount
        canvas1.move(drag_data["item"], delta_x, delta_y)
        # record the new position
        drag_data["x"] = event.x
        drag_data["y"] = event.y

#canvas1.tag_bind("token", "<ButtonPress-1>", drag_start)
canvas1.tag_bind("current", "<ButtonRelease-1>", drag_stop)
canvas1.tag_bind("current", "<B1-Motion>", drag)

canvas1.tag_bind("current", "<ButtonPress-1>", id_item)
canvas1.tag_bind("current", "<ButtonPress-3>", lower_item)


# ---- images -----

img1 = Image.open('chameleonOnTransparent.png')
img1 = img1.convert("RGBA")
#img1.putalpha(48)
photo1 = ImageTk.PhotoImage(img1)


img2 = Image.open("policecats1_trans.png")
img2 = img2.convert("RGBA")
img2c = img2.copy()
#img2c.putalpha(128)
iWd2, iHt2 = img2.size
i2scale = 0.3
new2wd = int(iWd2 * i2scale)
new2ht = int(iHt2 * i2scale)
img2c = img2c.resize((new2wd, new2ht))
photo2 = ImageTk.PhotoImage(img2c)

# ---- layout -----
ph1_id = canvas1.create_image(0,0, image=photo1, anchor=tk.NW, tags=("lizard","bob"))

canvas1.create_oval(100 - 25,100 - 25,100 + 25,100 + 25,
            outline="black",
            fill="green",
            tags=("token",),
        )
ph2_id = canvas1.create_image(800,400, image=photo2, tags="cat")


for item_id in canvas1.find_all():
    tag = canvas1.gettags(item_id)
    #canvas1.tag_bind(tag, '<Button-1>', lambda _, t=tag: print(t))
    print(tag)

win.mainloop() 

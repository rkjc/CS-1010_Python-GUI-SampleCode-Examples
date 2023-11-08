 
from tkinter import *
from PIL import ImageTk, Image

# for more complicated image manipulation checkout the PIL pillow library
# https://github.com/python-pillow/Pillow

root = Tk()
root.geometry("600x600")
# root.columnconfigure(0, minsize=100)
# root.columnconfigure(1, minsize=200)


def doButton1():
    label_1.config(image = space_pic_resize_2)
    label_1.tkraise()
    root.after(1000, revert_all)

def doButton2():
    label_1.config(image = kat_pic_resize_2)
    label_1.tkraise()
    root.after(1000, revert_all)

def revert_all():
    label_1.config(image="")


#images have to be .png, .jpg does not work.

space_img_full = Image.open("Space_Woman-sm.png")
space_pic_full = ImageTk.PhotoImage(space_img_full)

simgw, simgh = space_img_full.size

space_scale_1 = 0.2
space_img_resize_1 = space_img_full.resize((int(simgw*space_scale_1), int(simgh*space_scale_1)))
space_pic_resize_1 = ImageTk.PhotoImage(space_img_resize_1)

space_scale_2 = 600/simgw
space_img_resize_2 = space_img_full.resize((int(simgw * space_scale_2), int(simgh*space_scale_2)))
space_pic_resize_2 = ImageTk.PhotoImage(space_img_resize_2)

# ==== start Kat image section ====
kat_img_full = Image.open("kitten.jpg")
kat_pic_full = ImageTk.PhotoImage(kat_img_full)

imgw, imgh = kat_img_full.size

scale_1 = 0.08
kat_img_resize_1 = kat_img_full.resize((int(imgw*scale_1), int(imgh*scale_1)))
kat_pic_resize_1 = ImageTk.PhotoImage(kat_img_resize_1)

scale_2 = 600/imgw
kat_img_resize_2 = kat_img_full.resize((int(imgw * scale_2), int(imgh*scale_2)))
kat_pic_resize_2 = ImageTk.PhotoImage(kat_img_resize_2)

# ==== end Kat image section ====

label_1 = Label(root)
label_1.place(x=0, y=0)


MyButton1 = Button(root, text="b1", image=space_pic_resize_1, bg="cyan", command = doButton1)
MyButton1.grid(row=0, column=0)

MyButton2 = Button(root, text="b2", image=kat_pic_resize_1, bg="cyan", command = doButton2)
MyButton2.grid(row=0, column=1)

root.mainloop()


# https://appdividend.com/2020/06/19/how-to-resize-image-in-python-using-pillow-example/


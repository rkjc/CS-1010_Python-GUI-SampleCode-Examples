from tkinter import *
from PIL import Image, ImageTk

groot = Tk()
window_size = (600,500) # width, height
window_start_loc = (3600,1000)
groot.geometry(str(window_size[0])+
               'x'+str(window_size[1])+
               '+'+str(window_start_loc[0])+
               '+'+str(window_start_loc[1]))

#canvas1 = Canvas(groot, bg="white", width=window_size[0], height=window_size[1]-35)
canvas1 = Canvas(groot, bg="white", width=1, height=1)

# ------------------------------
#file_names = ["chameleon_tr.png", "DubiousCat_tr.png", "policecats1_tr.png"]
# tagfname is the filename of the image used as its first tag
file_names = ["chameleon_tr.png"]

img_store = {}
itmScale = {}
photo_store = {}
img_rescale = {}

resized = None

# ----- add the image ------



# ------- function defs --------

def do_one():
    pass

def do_two():
    pass

def do_three():
    pass

def do_four():
    pass

def load_image():
    store_image_photo(0)
    tagfname = file_names[0]
    add_photo_to_canvas(tagfname)


def store_image_photo(filename_index = 0):
    tagfname = file_names[filename_index]
    img_rescale[tagfname] = 1.0
    img_store[tagfname] = Image.open(tagfname)
    photo_store[tagfname] = ImageTk.PhotoImage(img_store[tagfname])

def add_photo_to_canvas(tagfname):
    canvas1.create_image(0,0, image=photo_store[tagfname], anchor=NW, tags=(tagfname,"pic"))

    
def rescale_photo(scale_val = 1.0):
    img_rescale[tagfname] *= scale_val
    tempImg = img_store(tagfname)
    imgWide, imgHigh = tempImg.size
    newWide = int(imgWide * img_rescale[tagfname])
    newHigh = int(imgHigh * img_rescale[tagfname])
    tempImg = tempImg.resize((newWide, newHigh))
    photo_store[tagfname] = ImageTk.PhotoImage(tempImg)

def resize_widgets(event):
    global resized 
    for items in canvas.find_all():
        if items != image:
            canvas.coords(items, 0, 0, event.width, event.height)
    resized = ImageTk.PhotoImage(im.resize((event.width, event.height), resample = Image.NEAREST))
    canvas.itemconfig(image, image=resized)
    canvas.moveto(image, 0, 0)

def resize_image(event):
    new_width = event.width
    new_height = event.height
    print("window-dim=",new_width,new_height)

    screen_width = groot.winfo_screenwidth()
    screen_height = groot.winfo_screenheight()
    #print("screen-dim=",screen_width,screen_height)
    
    #img3 = img2.resize((new_width,new_height), Image.ANTIALIAS)
    #photo1 = ImageTk.PhotoImage(img3)
    #canvas1.config(height=new_height)
    

# ---- bindings ---------

groot.bind("<Configure>", resize_image)
#canvas.bind('<Configure>', resize_widgets)

# ----- widgets ----------
butt_frame = Frame(groot)
button_1 = Button(butt_frame, text="B1", command=do_one)
button_2 = Button(butt_frame, text="B2", command=do_two)
button_3 = Button(butt_frame, text="B3", command=do_three)
button_4 = Button(butt_frame, text="B4", command=do_four)

# ---- widget layout -----
button_1.pack(side = LEFT)
button_2.pack(side = LEFT)
button_3.pack(side = LEFT)
button_4.pack(side = LEFT)

# ------ container layouts --------
#butt_frame.place(x=0, y=0)
butt_frame.pack(side = TOP, fill='x')
#canvas1.place(x=0, y=35)
canvas1.pack(side = BOTTOM, expand=True, fill='both')


load_image()


groot.mainloop()



    

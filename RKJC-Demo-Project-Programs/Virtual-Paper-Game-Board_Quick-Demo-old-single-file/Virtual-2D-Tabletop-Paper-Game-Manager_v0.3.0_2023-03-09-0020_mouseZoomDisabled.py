
# v0.3.0_2023-03-09-0020 rkjc

'''
#!/usr/bin/env python3
'''

#moving an item on a canvas
#https://stackoverflow.com/questions/6740855/board-drawing-code-to-move-an-oval/6789351#6789351 

'''
TODO
load and save files to handle multiple items with shared file_name tag

open image/load file dialog option

side buttons for set item visiblility

link items by tag, group move and scale
(requires changing scale to zoom from common perspective anchor)

change log:
added mouse wheel zoom
debug output disable feature
'''

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

debug_visible = False
if debug_visible: # global debug_visible
    pass

groot = Tk()
groot.title("VPD game board")
window_size = (1400,1000) #width, height
window_start_loc = (3000,540)
groot.geometry(str(window_size[0])+
               'x'+str(window_size[1])+
               '+'+str(window_start_loc[0])+
               '+'+str(window_start_loc[1]))

# ---- containers -----

left_side_frame = Frame(groot)
right_side_butt_frame = Frame(groot)

top_butt_frame = Frame(left_side_frame)

canvas1 = Canvas(left_side_frame, bg="white", width=1000, height=1000)


# ------ variables --------

file_names = []
file_data_lines = []
img_store_by_filename = {}
init_loc = {} # (tagfname: (x,y))
init_scale = {} #used once to set initial view size
init_state = {}

obj_image_store = [""]
obj_photo_store = [""]
obj_photo_scale = [""]
obj_photo_button = [""]
obj_photo_button_icon = [""]

drag_data = {"x": 0, "y": 0, "item": None}
lastTagClicked = ""
lastIdClicked = 0

space_key_down = False

# ------ import file names, settings, and images -----

def read_file_names(file_list_path):
    global debug_visible
    # Using readline()
    file1 = open(file_list_path, 'r')
    count = 0
    while True:
        count += 1
        line = file1.readline() # Get next line from file 
        if not line: # if line is empty, end of file is reached
            break
        data1 = (line.strip()).split(',')
        file_data_lines.append(data1)
        tagfname = data1[0]
        file_names.append(tagfname)
        print(data1)
        init_scale[tagfname] = float(data1[1])
        init_loc[tagfname] = (int(data1[2]),int(data1[3]))
        init_state[tagfname] = data1[4]
        img_store_by_filename[tagfname] = Image.open(tagfname) # saves the original image file by fileName
        thisindex = file_names.index(tagfname)
        if debug_visible: # global debug_visible
            print("file_data_lines data", file_data_lines[thisindex])
    file1.close()

def load_all():
    read_file_names('fileNameList.txt')
    for tagfname in file_names: 
        add_photo_to_canvas_init(tagfname)

def save_state_as():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    
    text2save = ""
    all_item_ids = canvas1.find_all()
    file_name_check = []
    
    for obid in all_item_ids:
        fnam = (canvas1.gettags(obid))[0]
        if fnam in file_name_check:
            pass
        else:
            file_name_check.append(fnam)
            scale = obj_photo_scale[obid]
            tstate = canvas1.itemconfigure(obid)["state"][4]
            if tstate == 'normal' or tstate == "":     
                #locx = (canvas1.bbox(obid))[0]
                #locy = (canvas1.bbox(obid))[1]
                locx = int((canvas1.coords(obid))[0])
                locy = int((canvas1.coords(obid))[1])
            else:
                locx = 0
                locy = 0
            text2save = (text2save + str(fnam) +
                            ',' + str(scale) +
                            ',' + str(locx) +
                            ',' + str(locy) +
                            ',' + str(tstate) +
                            '\n' )   
            print(fnam)
        
    f.write(text2save)
    f.close()

def load_state():
    pass


    
# ----- menu bar ------

menubar = Menu(groot)
groot.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Save_as', command=save_state_as)
file_menu.add_command(label='Exit', command=groot.destroy)

menubar.add_cascade(label="File", menu=file_menu, underline=0)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(label="Help", menu=help_menu)


# --- mouse and actions ----

def left_mouse(event):
    print("----- mouse clicked -----")
    global lastTagClicked
    global lastIdClicked
    global debug_visible
 
    lastIdClicked = get_id_through_transparent(event)
    if debug_visible: # global debug_visible
        print("lastIdClicked =>", lastIdClicked)
        print("canvas1.gettags(lastIdClicked)", canvas1.gettags(lastIdClicked))
        #lastTagClicked = canvas1.gettags(lastIdClicked)[0]
        print("coords", canvas1.coords(lastIdClicked))
        print("bbox", canvas1.bbox(lastIdClicked))  # returns a tuple like (x1, y1, x2, y2)
        print("lastTagClicked",lastTagClicked)
        print("find below", canvas1.find_below(lastIdClicked))
     
    #drag_data["item"] = lastIdClicked
    if space_key_down:
        drag_data["item"] = ALL
    else:
        drag_data["item"] = lastIdClicked
    drag_data["x"] = event.x
    drag_data["y"] = event.y

    if debug_visible: # global debug_visible
        print("--- finish mouse click -----")


def right_mouse(event):
    global lastTagClicked
    global lastIdClicked
    lastTagClicked = canvas1.gettags("current")[0]
    item_list = canvas1.find_closest(event.x, event.y)
    lastIdClicked = item_list[0]
   
def drag_start(event):
        """Begining drag of an object"""
        # record the item and its location
        #drag_data["item"] = canvas1.find_closest(event.x, event.y)[0]
        #if space_key_down:
        #    drag_data["item"] = ALL
        #else:
        #    drag_data["item"] = lastIdClicked
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
        if space_key_down:
            drag_data["item"] = ALL
        else:
            drag_data["item"] = lastIdClicked
        canvas1.move(drag_data["item"], delta_x, delta_y)

        # record the new position
        drag_data["x"] = event.x
        drag_data["y"] = event.y

def get_id_through_transparent(event):
    global debug_visible
    overlap_list = canvas1.find_overlapping(event.x, event.y,event.x, event.y)
    if debug_visible: # global debug_visible
        print("get_id_through_transparent")
        print("overlap_list",overlap_list,"len(overlap_list)",len(overlap_list))
    rev_overlap_list = reversed(overlap_list)
    px = event.x
    py = event.y
    if len(overlap_list) == 0:
        return 0
 
    overlap_copy = list(overlap_list)
    while (len(overlap_copy) != 0):
        oid = overlap_copy.pop()
        offx = canvas1.bbox(oid)[0]
        offy = canvas1.bbox(oid)[1]
        r, g, b, p = (obj_image_store[oid]).getpixel((px - offx, py - offy))
        if debug_visible: # global debug_visible
            print("object:", oid, "color=" , r,g,b,p)
        if p == 0:
            if debug_visible: # global debug_visible
                print("transparent pixel at id: ",oid)
            if(len(overlap_copy) == 0):
                if debug_visible: # global debug_visible
                    print("overlap_copy list empty, returning 0")
                return 0
        if p != 0:
            if debug_visible: # global debug_visible
                print("visable pixel at id: ",oid)
            return oid

count = 0
def mouse_wheel(event):
    pass
##    global count
##    # respond to Linux or Windows wheel event
##    if event.num == 5 or event.delta == -120:
##        count -= 1
##        rescale_all(1.05, event.x, event.y)
##    if event.num == 4 or event.delta == 120:
##        count += 1
##        rescale_all(0.95, event.x, event.y)
##    button_5.config(text = count)

    
# ---- image manipulation ------

def increase_size():
    global debug_visible
    if debug_visible: # global debug_visible
        print("\ndecrease_size -> lastTagClicked", lastTagClicked)
    rescale_image(1.1)

def increase_all():
    global debug_visible
    if debug_visible: # global debug_visible
        print("\nincrease_all -> ids", canvas1.find_all())
    rescale_all(1.1)

def decrease_size():
    global debug_visible
    if debug_visible: # global debug_visible
        print("\ndecrease_size -> lastTagClicked",lastTagClicked)
    rescale_image(0.9)

def decrease_all():
    global debug_visible
    if debug_visible: # global debug_visible
        print("\ndecrease_all -> ids", canvas1.find_all())
    rescale_all(0.9)

def rescale_image(scale_val = 1.0):
    idn = lastIdClicked
    rescale_image_id(idn, scale_val)
    
def rescale_all(adjust_scale_val, x = 0, y = 0):
    list_of_all_items_ids = canvas1.find_all()
    global debug_visible
    if debug_visible: # global debug_visible
        print("rescale_all", adjust_scale_val)
    for idn in list_of_all_items_ids:
        rescale_image_id(idn, adjust_scale_val)
        canvas1.scale(idn, x, y, adjust_scale_val, adjust_scale_val)

       
def rescale_image_id(idn, scale_val = 1.0):
    cIntId = idn
    thisTags = canvas1.gettags(cIntId)
    tagfname = str(thisTags[0])

    rescale_val_float = obj_photo_scale[cIntId] * scale_val
    global debug_visible
    if debug_visible: # global debug_visible
        print("rescale image:", rescale_val_float ,tagfname)
    tempImg = img_store_by_filename[tagfname]
    iWide, iHigh = tempImg.size
    newWide = int(iWide * rescale_val_float)
    newHigh = int(iHigh * rescale_val_float)
    temp_img = tempImg.resize((newWide, newHigh))
    temp_photo = ImageTk.PhotoImage(temp_img)
    obj_photo_scale[cIntId] = rescale_val_float
    obj_image_store[cIntId] = temp_img
    obj_photo_store[cIntId] = temp_photo
    canvas1.itemconfigure(cIntId, image=obj_photo_store[cIntId])

   
# ---- object manipulation ------

def make_copy():
    cIntId = lastIdClicked
    thisTags = canvas1.gettags(cIntId)
    tagfname = str(thisTags[0])
    add_photo_to_canvas(tagfname)

def delete_item():
    cIntId = lastIdClicked
    thisTags = canvas1.gettags(cIntId)
    tagfname = str(thisTags[0])
    canvas1.delete(cIntId)
    obj_image_store[cIntId] = ""
    obj_photo_store[cIntId] = ""
    obj_photo_scale[cIntId] = ""
    

def add_photo_to_canvas(tagfname, rescaleValFloat = 1.0, placeX = 0, placeY = 0, tstate = ''):
    tempImg = img_store_by_filename[tagfname]
    imgWide, imgHigh = tempImg.size
    newWide = int(imgWide * rescaleValFloat)
    newHigh = int(imgHigh * rescaleValFloat)
    tempImg2 = tempImg.resize((newWide, newHigh))
    # this creates a new canvas-photo-object with the same tag from stored-image 
    temp_photo = ImageTk.PhotoImage(tempImg2)
    #cIntId = canvas1.create_image(placeX,placeY, image=temp_photo, anchor=NW, tags=(tagfname,"pic"))
    cIntId = canvas1.create_image(placeX,placeY, image=temp_photo, tags=(tagfname,"pic"))
    canvas1.itemconfig(cIntId, state=tstate)
    # storing the photo and matching image objects to avoid garbage collection
    obj_photo_scale.append("")
    obj_photo_scale[cIntId] = rescaleValFloat
    obj_image_store.append("")
    obj_image_store[cIntId] = tempImg2
    obj_photo_store.append("")
    obj_photo_store[cIntId] = temp_photo
    
    bicon = tempImg.resize((50, 50))
    button_text = "item " + str(cIntId)
    photoicon = ImageTk.PhotoImage(bicon)
    butobj = Button(right_side_butt_frame, image=photoicon, text=button_text, command=lambda: side_butt(cIntId))
    obj_photo_button.append("")
    obj_photo_button[cIntId] = butobj
    obj_photo_button_icon.append("")
    obj_photo_button_icon[cIntId] = photoicon
    butobj.pack(side = TOP)
    global debug_visible
    if debug_visible: # global debug_visible
        print("object number", cIntId)  # cIntId is just an integer
    return cIntId


def add_photo_to_canvas_init(tagfname):
    placeX = (init_loc[tagfname])[0]
    placeY = (init_loc[tagfname])[1]
    global debug_visible
    if debug_visible: # global debug_visible
        print("in scaleAdd init_scale[tagfname]", init_scale[tagfname])
    rescaleValFloat = init_scale[tagfname]
    tstate = init_state[tagfname]
    add_photo_to_canvas(tagfname, rescaleValFloat, placeX, placeY, tstate)


def lower_item():
    global lastIdClicked
    global debug_visible
    if debug_visible: # global debug_visible
        print("\nlower_item -> lastTagClicked",lastIdClicked)
    canvas1.tag_lower(lastIdClicked, canvas1.find_below(lastIdClicked))

def raise_item():
    global lastIdClicked
    global debug_visible
    if debug_visible: # global debug_visible
        print("\nraise_item -> lastTagClicked",lastIdClicked)
    canvas1.tag_raise(lastIdClicked, canvas1.find_above(lastIdClicked))


def key_board(event):
    print ("Keycode:", event.keycode, "State:", event.state, "char:", event.char)


# ------------- hold down key check ------------
afterId = None
def key_hold_press(event):
    global afterId
    global space_key_down
    global debug_visible
    space_key_down = True
    button_5.config(bg="green")
    if afterId != None:
        groot.after_cancel( afterId )
        afterId = None
    else:
        if debug_visible: # global debug_visible
            print ('key pressed %s' % event.time)

def key_hold_release(event):
    global afterId
    afterId = groot.after_idle( key_hold_process_release, event )

def key_hold_process_release(event):
    global afterId
    global space_key_down
    space_key_down = False
    button_5.config(bg="cyan")
    global debug_visible
    if debug_visible: # global debug_visible
        print ('key release %s' % event.time)
    afterId = None
    
    
# ----  bindings -----

canvas1.bind("<ButtonRelease-1>", drag_stop)
canvas1.bind( "<B1-Motion>", drag)
canvas1.bind( "<ButtonPress-1>", left_mouse)
canvas1.bind( "<ButtonPress-3>", right_mouse)

groot.bind("<Key>", key_board)

groot.bind("<KeyPress-space>", key_hold_press)
groot.bind("<KeyRelease-space>", key_hold_release)

# with Windows OS
groot.bind("<MouseWheel>", mouse_wheel)
# with Linux OS
groot.bind("<Button-4>", mouse_wheel)
groot.bind("<Button-5>", mouse_wheel)

# --- auto make images ----


# ---- gp button functions -----

def side_butt(idin):
    global debug_visible
    if debug_visible: # global debug_visible
        print(idin)
        print("state",idin," - ",(canvas1.itemconfigure(idin)["state"]))
        print("state",idin," - ",(canvas1.itemconfigure(idin)["state"][4]))
    
    tstate = canvas1.itemconfigure(idin)["state"][4]
    show = (tstate == 'hidden')
    if show:
        if debug_visible: # global debug_visible
            print("show it")
        canvas1.itemconfig(idin, state='')
    else:
        if debug_visible: # global debug_visible
            print("hide it")
        canvas1.itemconfig(idin, state='hidden')
    
    
# ----- widgets ----

button_inc = Button(top_butt_frame, text="increase", command=increase_size)
button_dec = Button(top_butt_frame, text="decrease", command=decrease_size)
button_raise = Button(top_butt_frame, text="raise", command=raise_item)
button_lower = Button(top_butt_frame, text="lower", command=lower_item)
button_1 = Button(top_butt_frame, text=" (1) ", command=None)
button_2 = Button(top_butt_frame, text="increase all", command=increase_all)
button_3 = Button(top_butt_frame, text="decrease all", command=decrease_all)
button_4 = Button(top_butt_frame, text=" (4) ", command=None)
button_5 = Button(top_butt_frame, text=" (5) ", command=None)

# ---- layout -----

button_inc.pack(side = LEFT)
button_dec.pack(side = LEFT)
button_raise.pack(side = LEFT)
button_lower.pack(side = LEFT)
button_1.pack(side = LEFT)
button_2.pack(side = LEFT)
button_3.pack(side = LEFT)
button_4.pack(side = LEFT)
button_5.pack(side = LEFT)

top_butt_frame.pack(side = TOP, fill='x')
canvas1.pack(side = BOTTOM, expand=True, fill='both') 

left_side_frame.pack(side=LEFT, expand=True, fill='both')
right_side_butt_frame.pack(side = RIGHT, fill = 'y')

# ----- run -------

load_all()

groot.mainloop() 

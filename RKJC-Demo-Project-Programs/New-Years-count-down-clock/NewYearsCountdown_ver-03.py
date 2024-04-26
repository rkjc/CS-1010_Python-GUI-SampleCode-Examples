#!/usr/bin/env python3

# New Years Eve count down clock ver-0.3
# NewYearsCountdown_ver-03.py
# Richard Cross
# 2023-12-31 at 11:13pm
# MIT open source licence 


import tkinter as tk
from tkinter.colorchooser import askcolor
import time
import datetime
import random

groot = tk.Tk()
#groot.geometry("420x100")
groot.resizable(False, False)
groot.config(bg="black")

tframe = tk.Frame(groot)
tframe.pack(fill='both', expand=True)
tframe.config(bg="black")

def syncronize_start():
    tnow_sec = str(time.gmtime().tm_sec)
    tnext_sec = str(time.gmtime().tm_sec)
    while(tnow_sec == tnext_sec):
        tnext_sec = str(time.gmtime().tm_sec)
    onUpdate()
    
  
def current_iso8601():
    """Get current date and time in ISO8601"""
    # https://en.wikipedia.org/wiki/ISO_8601
    # https://xkcd.com/1179/
    #return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    #return time.strftime("%Y-%m-%dT\n%H:%M:%SZ", time.gmtime())
    tempstr = str(time.gmtime().tm_hour) + " - " + str(time.gmtime().tm_min) + " - " + str(time.gmtime().tm_sec)
    return tempstr

def countDown():
    nextyear = datetime.datetime.now().year + 1
    targettime = datetime.datetime(year=nextyear, month=1, day=1, hour=0, minute=0, second=0)
    tnow = datetime.datetime.now()
    tdelta = targettime - tnow
    #return str(tdelta.days) + str(time.strftime(" + %H:%M:%S", time.gmtime(tdelta.seconds)))
    return str(tdelta.days) + str(time.strftime(" days; %H hr; %M min; %S sec", time.gmtime(tdelta.seconds)))

def onUpdate():
    # update displayed time
    nowt.set(countDown())
    time_label.config(text=nowt.get())
    # schedule timer to call itself after 1 second
    groot.after(1000, onUpdate)

def makeNegative():
    global isNegative
    # flip state value
    isNegative = not isNegative
    if isNegative:
        # set negative colors
        time_label.config(bg=color_1, fg=color_2)
        tframe.config(bg=color_1)
        menubar.config(bg=color_1, fg=color_2)
    else:
        time_label.config(fg=color_1, bg=color_2)
        tframe.config(bg=color_2) 
        menubar.config(fg=color_1, bg=color_2) 
        
def config_font(a_wigit, new_name, new_size):
    a_wigit.config(font=(new_name, new_size))

def increase_size():
    global afont_size
    afont_size += 6
    config_font(time_label, afont_name, afont_size)

def decrease_size():
    global afont_size
    if afont_size > 29:
        afont_size -= 6
        config_font(time_label, afont_name, afont_size)

def get_color():
    this_color = askcolor()
    print(this_color)
    return this_color

def set_color_1():
    global color_1
    tcolor = get_color()
    color_1 = tcolor[1]
    makeNegative()
    makeNegative()

def set_color_2():
    global color_2
    tcolor = get_color()
    color_2 = tcolor[1]
    makeNegative()
    makeNegative()

def do_button():
    random_colors()

def hex_from_rgb(rgb):
    r, g, b = rgb
    r = int(r)
    g = int(g)
    b = int(b)
    return f'#{r:02x}{g:02x}{b:02x}'
    
def random_colors():
    global color_1, color_2
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    hex_str_1 = hex_from_rgb(rgb)
    print("hex_str_1", hex_str_1)
    color_1 = hex_str_1
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    hex_str_2 = hex_from_rgb(rgb)
    print("hex_str_2", hex_str_2)
    color_2 = hex_str_2
    makeNegative()
    makeNegative()

    
isNegative = False

# startup values
afont_name = 'Terminal'
afont_size = 64
labl_bg = 'gray2'
color_1 = "white"
color_2 = "black"

# using tkinter StringVar variable instead of doing global variables in the functions
nowt = tk.StringVar()

time_label = tk.Label(tframe, bg=labl_bg, font=(afont_name, afont_size))
time_label.pack(fill='both', expand=True, padx=40, pady=10)
time_label.config(text=nowt.get())

time_label.config(fg=color_1, bg=color_2)


# make a menu bar object
menubar = tk.Menu(groot, fg=color_1, bg=color_2)

# making the file dropdown selector object
file_menu = tk.Menu(menubar, tearoff=0)
# adding the file dropdown to the menu bar
menubar.add_cascade(label="File", menu=file_menu)
# populate the file dropdown
file_menu.add_command(label="Reverse color", command=makeNegative)
file_menu.add_command(label="Exit", command=groot.quit)

# making an edit dropdown selector object (currently un-used)
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="select color 1", command=set_color_1)
edit_menu.add_command(label="select color 2", command=set_color_2)
edit_menu.add_command(label="select random", command=random_colors)

menubar.add_command(label=" | ")

#adding command items directly to the menu bar
menubar.add_command(label="Swap-colors", command=makeNegative)
menubar.add_command(label="^", command=increase_size)
menubar.add_command(label="v", command=decrease_size)

menubar.add_command(label=" | ")
menubar.add_command(label="random colors", command=do_button)

groot.config(menu=menubar)

# initial time display
# onUpdate()
syncronize_start()

groot.mainloop()



# https://stackoverflow.com/questions/51591456/can-i-use-rgb-in-tkinter
# rgb to hex conversion


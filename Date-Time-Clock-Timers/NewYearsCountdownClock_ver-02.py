
# New Years Eve count down clock ver-0.2
# NewYearsCountdown_ver-02.py
# Richard Cross
# 2023-12-31 at 11:13pm
# MIT open source licence 


import tkinter as tk
import time
import datetime

groot = tk.Tk()
#groot.geometry("420x100")
groot.resizable(False, False)
groot.config(bg="black")

tframe = tk.Frame(groot)
tframe.pack(fill='both', expand=True)
tframe.config(bg="black")


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
    return str(tdelta.days) + str(time.strftime(" + %H:%M:%S", time.gmtime(tdelta.seconds)))

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

# initial time display
onUpdate()

# make a menu bar object
menubar = tk.Menu(groot, fg=color_1, bg=color_2)

# making the file dropdown selector object
filemenu = tk.Menu(menubar, tearoff=0)
# adding the file dropdown to the menu bar
menubar.add_cascade(label="File", menu=filemenu)
# populate the file dropdown
filemenu.add_command(label="Reverse color", command=makeNegative)
filemenu.add_command(label="Exit", command=groot.quit)

#adding command items directly to the menu bar
menubar.add_command(label="Reverse color", command=makeNegative)
menubar.add_command(label="^", command=increase_size)
menubar.add_command(label="v", command=decrease_size)

# making an edit dropdown selector object (currently un-used)
editmenu = tk.Menu(menubar, tearoff=0)

groot.config(menu=menubar)

groot.mainloop()



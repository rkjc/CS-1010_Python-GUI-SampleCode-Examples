import tkinter as tk
import time
import datetime


# https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter
def donothing():
    filewin = tk.Toplevel(root)
    button = tk.Button(filewin, text="Do nothing button")
    button.pack()

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
    root.after(1000, onUpdate)

def makeNegative():
    global isNegative
    # flip state value
    isNegative = not isNegative
    if isNegative:
        # set negative colors
        filler.config(fg=defaultBG, bg="black")
        time_label.config(fg=defaultBG, bg="black")
        tframe.config(bg="black")
        root.config(bg="black")
        menubar.config(bg="black", fg="white")
        #QUIT.config(bg="black")
    else:
        filler.config(fg="black", bg=defaultBG)
        time_label.config(fg="black", bg=defaultBG)
        tframe.config(bg=defaultBG)
        root.config(bg="#ff0000")
        menubar.config(bg=defaultBG, fg="black")
        #QUIT.config(bg=defaultBG)

isNegative = True

root = tk.Tk()
root.geometry("420x100")
tframe = tk.Frame(root)
defaultBG = tframe.cget("background")
#print(defaultBG)

tframe.pack()
# using tkinter StringVar variable instead of doing global variables in the functions
nowt = tk.StringVar()
filler = tk.Label(tframe, height=1, bg="black")
filler.pack()
time_label = tk.Label(tframe, font=('Helvetica', 36))
time_label.pack()
time_label.config(text=nowt.get())

time_label.config(fg=defaultBG, bg="black")
tframe.config(bg="black")
root.config(bg="black")

# initial time display
onUpdate()

menubar = tk.Menu(root, bg="black", fg="white")
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Reverse color", command=makeNegative)

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)


root.config(menu=menubar)
root.mainloop()



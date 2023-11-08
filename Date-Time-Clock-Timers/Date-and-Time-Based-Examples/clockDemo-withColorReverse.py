import tkinter as tk
import time

# https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter

def current_iso8601():
    """Get current date and time in ISO8601"""
    # https://en.wikipedia.org/wiki/ISO_8601
    # https://xkcd.com/1179/
    #return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    return time.strftime("%Y-%m-%dT\n%H:%M:%SZ", time.gmtime())

def onUpdate():
    # update displayed time
    nowt.set(current_iso8601())
    time_label.config(text=nowt.get())
    # schedule timer to call itself after 1 second
    #tframe.after(1000, onUpdate)
    root.after(1000, onUpdate)

def makeNegative():
    global isNegative
    # flip state value
    isNegative = not isNegative
    if isNegative:
        # set negative colors
        time_label.config(fg=defaultBG, bg="black")
        tframe.config(bg="black")
        root.config(bg="black")
        NegativeB.config(bg="black")
        QUIT.config(bg="black")
    else:
        time_label.config(fg="black", bg=defaultBG)
        tframe.config(bg=defaultBG)
        root.config(bg="#ff0000")
        NegativeB.config(bg=defaultBG)
        QUIT.config(bg=defaultBG)

isNegative = False

root = tk.Tk()
tframe = tk.Frame(root)
defaultBG = tframe.cget("background")
print(defaultBG)

tframe.pack()
# using tkinter StringVar variable instead of doing global variables in the functions
nowt = tk.StringVar()
time_label = tk.Label(tframe, font=('Helvetica', 24))
time_label.pack(side="top")
time_label.config(text=nowt.get())

NegativeB = tk.Button(tframe, text="reverse color", fg="green", command=makeNegative)
NegativeB.pack()

QUIT = tk.Button(tframe, text="QUIT", fg="red", command=root.destroy)
QUIT.pack(side="bottom")

# initial time display
onUpdate()

root.mainloop()



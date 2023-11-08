# https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter
import tkinter as tk
import time

def current_iso8601():
    """Get current date and time in ISO8601"""
    # https://en.wikipedia.org/wiki/ISO_8601
    # https://xkcd.com/1179/
    #return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    return time.strftime("%Y-%m-%dT\n%H:%M:%SZ", time.gmtime())

def onUpdate():
    # update displayed time
    nowt.set(current_iso8601())
    timet.config(text=nowt.get())
    # schedule timer to call itself after 1 second
    tframe.after(1000, onUpdate)


root = tk.Tk()
tframe = tk.Frame(root)
tframe.pack()

# using tkinter StringVar variable instead of doing global variables in the functions
now_time_string = tk.StringVar()

timet = tk.Label(tframe, font=('Helvetica', 24))
timet.pack(side="top")
timet.config(text=nowt.get())

RedB = tk.Button(tframe, text="make red", fg="red", command=makeRed)
RedB.pack(side="bottom")

BlueB = tk.Button(tframe, text="make blue", fg="blue", command=makeBlue)
BlueB.pack(side="bottom")

QUIT = tk.Button(tframe, text="QUIT", fg="red", command=root.destroy)
QUIT.pack(side="bottom")

# initial time display
onUpdate()

root.mainloop()
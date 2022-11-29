#!/usr/bin/python3

"""
Copyright (c) 2020 by Richard kj Cross

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

2020-12-08
"""

import tkinter as tk
import time


def updateTime():
    # update displayed date and time in ISO8601 format
    tempTime = time.strftime("%Y-%m-%dT\n%H:%M:%SZ", time.gmtime())
    time_label.config(text=tempTime)
    # schedule timer to call itself after 1 second
    groot.after(1000, updateTime)

def makeNegative():
    global isNegative
    # flip state value first
    isNegative = not isNegative
    if isNegative:
        # set negative colors
        colorChange(defaultBG, "black")
        groot.config(bg="black")

    else:
        colorChange("black", defaultBG)
        groot.config(bg="#ff0000")


def colorChange(frontcolor, backcolor):
        time_label.config(fg=frontcolor, bg=backcolor)
        tframe.config(bg=backcolor)
        NegativeB.config(bg=backcolor, activebackground=backcolor)
        QUIT.config(bg=backcolor, activebackground=backcolor)

isNegative = False

groot = tk.Tk()
groot.title("UTC time")
tframe = tk.Frame(groot)
defaultBG = tframe.cget("background")

tframe.pack()
time_label = tk.Label(tframe, font=('Ariel', 24), padx=10, pady=5)
time_label.pack(side="top")
time_label.config(text="time goes here")

NegativeB = tk.Button(tframe, text="reverse color", fg="green", activeforeground='green', command=makeNegative)
NegativeB.pack(side="left", fill='x')

QUIT = tk.Button(tframe, text="QUIT", fg="red", activeforeground='red', command=groot.destroy)
QUIT.pack(side="right")

# start time display
updateTime()

groot.mainloop()



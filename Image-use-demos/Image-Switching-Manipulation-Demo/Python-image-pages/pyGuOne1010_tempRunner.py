from tkinter import *
import tkinter as tk

win=tk.Tk()
win.title('Table')
lb=Label(win,text='Type a number:',font='Helvetica 12 bold')
lb.grid(row=0, column=0)
lb2 = Label(text='')
e=Entry(win)
e.grid(row=1, column=0)
c = 2

def click():
    global c
    c = e.get()
    print('requested number ', c)
    reset()
    make_label(c)

def make_label(c):
    global lb2
    txt = []
    for b in (range(0, 11)):
        txt.append('{} x {} = {} '.format(c, b, int(b)*int(c)))
    text = '\n'.join(txt)
    lb2 = Label(text=text)
    lb2.grid(row=4, column=0)

def reset():
    global lb2
    lb2.destroy()
    lb2 = Label()
    lb2.grid(row=4, column=0)

make_label(c)

bt1=Button(win,text='GO',bg='lightblue',command=click)
bt1.grid(row=2, column=0)
bt2=Button(win,text='RESET',bg='lightblue',command=reset)   
bt2.grid(row=3, column=0)
win.mainloop()

from tkinter import *

root = Tk()
root.geometry("400x400+0+0")
frm1 = Frame(root)    
frm1.pack()

afterId = None
    
def key_press(event):
    global afterId
    indc_lbl.config(bg="green")
    if afterId != None:
        root.after_cancel( afterId )
        afterId = None
    else:
        print ('key pressed %s' % event.time)

def key_release(event):
    global afterId
    afterId = root.after_idle( process_release, event )

def process_release(event):
    indc_lbl.config(bg="cyan")
    global afterId
    print ('key release %s' % event.time)
    afterId = None

def motion(event):
    x = event.x
    y = event.y
    lbl_x.config(text=x)
    lbl_y.config(text=y)
    abs_x = root.winfo_pointerx()
    abs_y = root.winfo_pointery()
    lbl_absx.config(text=abs_x)
    lbl_absy.config(text=abs_y)
   

lblfrm_1 = LabelFrame(root, text="relative")
lblfrm_2 = LabelFrame(root, text="absolute")

lbl_x = Label(lblfrm_1, text="x-coord", width=8)
lbl_y = Label(lblfrm_1, text="y-coord", width=8)
lbl_absx = Label(lblfrm_2, text="x-coord", width=8)
lbl_absy = Label(lblfrm_2, text="y-coord", width=8)

lblfrm_1.pack()
lblfrm_2.pack()
lbl_x.pack(side=LEFT, padx = 5)
lbl_y.pack(side=LEFT, padx = 5)
lbl_absx.pack(side=LEFT, padx = 5)
lbl_absy.pack(side=LEFT, padx = 5)

indc_lbl = Label(root, bg="cyan", text="key press", width=8, height=3)
indc_lbl.pack()

root.bind('<Motion>', motion)

root.bind('<KeyPress-a>', key_press)
root.bind('<KeyRelease-a>', key_release)
        
root.mainloop()

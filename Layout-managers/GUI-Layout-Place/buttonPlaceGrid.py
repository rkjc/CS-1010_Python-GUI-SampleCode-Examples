from tkinter import *

root = Tk()
frame=Frame(root)
root.geometry("400x400")

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

def doButton(passin):
    texxt = str(passin)
    label.config(text=texxt)
    if(btn[int(passin)]['bg'] == 'blue'):     
        btn[int(passin)].configure(bg="red")
    else:
        btn[int(passin)].configure(bg="blue")

btn={} 
#example values
for x in range(10):
    for y in range(10):
        namme=str(x+10*y)
        btn[(x+10*y)] = Button(frame,  text=namme,
                            command=  lambda idd=(x+10*y): doButton(idd))
        btn[(x+10*y)].grid(column=x, row=y, sticky=N+S+E+W)

for x in range(10):
  Grid.columnconfigure(frame, x, weight=1)

for y in range(10):
  Grid.rowconfigure(frame, y, weight=1)

label = Label(frame, text="number here")
label.grid(column=0,row=11,columnspan=10)

root.mainloop()

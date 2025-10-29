import tkinter as tk
groot = tk.Tk()
groot.geometry("810x550")

# Need to use the special tkinter.IntVar() variable
# to connect the radio buttons together as a group
myIntThing = tk.IntVar()

# sets which button will be selected by default
myIntThing.set( 0 )

def doButt():
    temp_var = myIntThing.get()
    L1.configure(text=temp_var)

L2 = tk.Label(groot, text="volume control", font=('arial', 20))
L2.pack()

L1 = tk.Label(groot, text="selection", font=('arial', 20))
L1.pack()

iscolor = True

postitstore = []


for y in range(0,10):  
    aFrame = tk.Frame(groot)        
       
    if y == 0:   
        tempRadButt = tk.Radiobutton(aFrame)
        tempRadButt.config(text=str(0), font=(None, 18), bg='magenta', variable=myIntThing, value=0, command=doButt)
        tempRadButt.pack(side='left')
    

    if iscolor:
        thiscolor = 'magenta'
        iscolor = not iscolor
    else:
        thiscolor = 'cyan'
        iscolor = not iscolor
       
    for x in range(1,10):
        vol = x + (y * 10)
        tempRadButt = tk.Radiobutton(aFrame)
        tempRadButt.config(text=str(vol), font=(None, 18), bg=thiscolor, variable=myIntThing, value=vol, command=doButt)
        tempRadButt.pack(side='left')
     
    
    aFrame.pack()

aFrame.config(bg='magenta')


groot.mainloop()
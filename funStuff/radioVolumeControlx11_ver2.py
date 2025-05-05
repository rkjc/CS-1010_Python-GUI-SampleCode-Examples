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

L2 = tk.Label(groot, text="volume control")
L2.pack()

L1 = tk.Label(groot, text="selection", font=('arial', 20))
L1.pack()


for y in range(0,10):
    
    aFrame = tk.Frame(groot)
    
    for x in range(1,10):
        vol = x + (y * 10)
        tempRadButt = tk.Radiobutton(aFrame)
        tempRadButt.config(text=str(vol), font=(None, 18), variable=myIntThing, value=vol, command=doButt)
        tempRadButt.pack(side='right')
      
    aFrame.pack(side='bottom')


groot.mainloop()
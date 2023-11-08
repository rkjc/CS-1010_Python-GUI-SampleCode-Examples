from tkinter import *

root = Tk()
cando = "the cando text"

def doButton(attrb):
    print("did doButton", attrb)
    L2.config(text=cando)
    L1.config(image=im2)

    
im1a = PhotoImage(file="example.png")
im1 = im1a.subsample(2)

im2a = PhotoImage(file="cat1.png")
im2 = im2a.subsample(2)

im3 = PhotoImage(file="squirrel-coffee.png")

L1 = Label(root, image=im1)
L1.grid(row=0, column=1)

explanation = """Example using grid and a png image"""

L2 = Label(root, 
              justify=LEFT,
              padx = 10, 
              text=explanation)
L2.grid(row=0, column=0)

MyButton1 = Button(root, text="Submit", bg="blue",width=20, height=5, command = lambda: doButton("yoiks"))
MyButton1.grid(row=1, column=0)



L3 = Label(root, image=im2)
L3.grid(row=1, column=1)

L4 = Label(root, image=im3)
L4.grid(row=1, column=2)

root.mainloop()

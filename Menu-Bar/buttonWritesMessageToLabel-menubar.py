#import tkinter
from tkinter import *
from tkinter import filedialog

bob = Tk()
bob.geometry('200x100')

def doButton():
  label_1.configure(text = "you pushed the button")

def save_state_as():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = "putting\nsome lines of\ntext in a file"
 
    f.write(text2save)
    f.close()

def load_state():
    pass


    
# ----- menu bar ------

menubar = Menu(bob)
bob.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Save_as', command=save_state_as)
file_menu.add_command(label='Exit', command=bob.destroy)

menubar.add_cascade(label="File", menu=file_menu, underline=0)



label_1 = Label(bob, text="A Label")
label_1.pack()

button_1 = Button(bob, text="A Button", command=doButton)
button_1.pack()

bob.mainloop()

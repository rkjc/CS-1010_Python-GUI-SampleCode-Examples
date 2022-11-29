import tkinter

def doButton():
    label_1.configure(text = "you pushed the button")

groot = tkinter.Tk()
groot.geometry('200x100')

label_1 = tkinter.Label(groot, text="A Label")
label_1.pack()

button_1 = tkinter.Button(groot, text="A Button", command=doButton)

# Special note for Button Colors
# windows and Linux need the 'background' setting
# MacOs needs the 'highlightbackground' setting (MacOs Big Sur may have broken this)
# Linux needs the 'activebackground' setting to handle mouse-overs
bColor1 = 'cyan'
button_1.configure(background = bColor1, highlightbackground = bColor1, activebackground = bColor1)
button_1.pack()

groot.mainloop()
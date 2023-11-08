import tkinter

groot = tkinter.Tk()
#groot.geometry("200x100")

buttonOn = False

def pushButton():
    global buttonOn
    if(buttonOn):
        #turn it off
        bColor1 = 'red'
        label_1.configure(text="Button is OFF")
    else:
        #turn it on
        bColor1 = 'green'
        label_1.configure(text="Button is ON")
    buttonOn = not buttonOn
    button_1.configure(background=bColor1, highlightbackground=bColor1, activebackground=bColor1)

label_1 = tkinter.Label(groot, text="A sample Label", font=("ariel", 32))
label_1.pack()

label_2 = tkinter.Label(groot, text="A sample Label", font=("arial", 32))
label_2.pack()

button_1 = tkinter.Button(groot, text="Push Button", command=pushButton)
#initial button color setup
bColor1 = 'red'
button_1.configure(background = bColor1, highlightbackground = bColor1, activebackground = bColor1)
button_1.pack()

groot.mainloop()
# use your prefered way of importing and using the tkinter library

import tkinter

# by putting the macbutton.py file (contains the MButton class)
# in the same folder as your python tkinter program it can be imported
# without setting environment variables or using custom path

import macbutton


groot = tkinter.Tk()
groot.geometry("400x300")

count = 1

def butt_action():
    global count
    label_1.config(text = ('non-button pushes ' + str(count)))
    count += 1

def do_butt_1(): # set mbutton color
    button_0.config(bg='orange')

def do_butt_2(): # reset mbutton color
    button_0.config(bg = macbutton.MButton.default_bg)
    

button_0 = macbutton.MButton(groot, text='fake button', command=butt_action)

button_1 = tkinter.Button(groot, text='real button - set color', font = ('', 20), command=do_butt_1)

button_2 = tkinter.Button(groot, text='real button - clear color', font = ('', 20),command=do_butt_2)


label_1 = tkinter.Label(groot, text="I'm a label", font = ('', 20))
label_1.pack()


button_0.mpack()

button_1.pack()
button_2.pack()


groot.mainloop()



#print(button_0.default_bg)
#print(mb.MButton.default_bg)

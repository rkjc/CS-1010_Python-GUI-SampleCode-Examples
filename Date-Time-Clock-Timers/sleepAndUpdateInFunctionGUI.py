 
import tkinter
import time

print("hello")
groot = tkinter.Tk()

count = 0

def do_one():
    global count
    count += 1
    lcount = str(count)
    str_var1.set(lcount + ' - changed')
    label_1.update()
    time.sleep(1)
    str_var1.set(lcount + " - two")
    label_1.update()
    time.sleep(1)
    str_var1.set(lcount + ' - one')
    label_1.update()
    time.sleep(1)
    str_var1.set(lcount + ' - zero')


str_var1 = tkinter.StringVar()
str_var1.set('starting')

label_1 = tkinter.Label(groot,font=("wingdings", 9))

label_1['textvariable']= str_var1

label_1.pack()

button_1 = tkinter.Button(groot, text="Button one", command=do_one)
button_1.pack()


groot.mainloop()


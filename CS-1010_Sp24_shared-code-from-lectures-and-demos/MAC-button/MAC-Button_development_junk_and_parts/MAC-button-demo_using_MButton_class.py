import tkinter as tk
import MButton as mb

groot = tk.Tk()
groot.geometry("400x300")

print(groot.tk)

def butt_action():
    print("hello from out there")

def do_butt_1():
    button_0.config(bg='cyan')

button_0 = mb.MButton(groot, text='fun button', command=butt_action)

button_1 = tk.Button(groot, text='real button 1', font = ('', 20), command=do_butt_1)

button_2 = tk.Button(groot, text='real button 2', font = ('', 20))


label_1 = tk.Label(groot, text="I'm a label", font = ('', 20), relief="sunken")
label_1.pack()


button_0.mpack()

button_1.pack()
button_2.pack()


groot.mainloop()

 
from tkinter import *

def show_values():
    print (slide_v1.get(), slide_v2.get())
    print(slideVar1.get())

def all_off():
    all_set_val(0)

def all_mid():
    all_set_val(800)

def all_full():
    all_set_val(1600)

def all_set_val(val):
    slide_v1.set(val)
    slide_v2.set(val)
    slide_v3.set(val)
    slide_v4.set(val)
    slide_v5.set(val)
    slide_v6.set(val)
    slide_v7.set(val)
    slide_v8.set(val)

def slider_callback_1(var):
    message = "motor 1 -> " + str(var)
    value_label_1.config(text=message)

def slider_callback_2(var):
    message = "motor 2 -> " + str(var)
    value_label_2.config(text=message)

def slider_callback_3(var):
    message = "motor 3 -> " + str(var)
    value_label_3.config(text=message)

def slider_callback_4(var):
    message = "motor 4 -> " + str(var)
    value_label_4.config(text=message)

def slider_callback_5(var):
    message = "motor 5 -> " + str(var)
    value_label_5.config(text=message)

def slider_callback_6(var):
    message = "motor 6 -> " + str(var)
    value_label_6.config(text=message)

def slider_callback_7(var):
    message = "motor 7 -> " + str(var)
    value_label_7.config(text=message)

def slider_callback_8(var):
    message = "motor 8 -> " + str(var)
    value_label_8.config(text=message)

master = Tk()

slideVar1 = IntVar()
slideVar2 = IntVar()
slideVar3 = IntVar()
slideVar4 = IntVar()
slideVar5 = IntVar()
slideVar6 = IntVar()
slideVar7 = IntVar()
slideVar8 = IntVar()



label_box = Frame(master,  width=200, height=250, bd = 0, highlightbackground="orange", highlightcolor="orange", highlightthickness=1)
label_box.pack(expand=True, side=LEFT)
label_box.pack_propagate(0)

value_label_1 = Label(label_box, text='motor 1 -> 0')
value_label_1.pack()
value_label_2 = Label(label_box, text='motor 2 -> 0')
value_label_2.pack()
value_label_3 = Label(label_box, text='motor 3 -> 0')
value_label_3.pack()
value_label_4 = Label(label_box, text='motor 4 -> 0')
value_label_4.pack()
value_label_5 = Label(label_box, text='motor 5 -> 0')
value_label_5.pack()
value_label_6 = Label(label_box, text='motor 6 -> 0')
value_label_6.pack()
value_label_7 = Label(label_box, text='motor 7 -> 0')
value_label_7.pack()
value_label_8 = Label(label_box, text='motor 8 -> 0')
value_label_8.pack()




slide_box = Frame(master)
slide_box.pack(side=LEFT)

slide_control_1 = Frame(slide_box, bd = 0, highlightbackground="green", highlightcolor="green", highlightthickness=1)
slide_v1 = Scale(slide_control_1, from_=1600, to=0, length=200, variable=slideVar1, command=slider_callback_1)
slide_v1.set(0)
slide_v1.pack()
Label(slide_control_1, text="    Motor 1").pack(side = BOTTOM)
slide_control_1.pack(padx=20, pady=5, side = LEFT)


slide_control_2 = Frame(slide_box, bd = 0, highlightbackground="green", highlightcolor="green", highlightthickness=1)
slide_v2 = Scale(slide_control_2, from_=1600, to=0, length=200, variable=slideVar2, command=slider_callback_2)
slide_v2.set(0)
slide_v2.pack()
Label(slide_control_2, text="    Motor 2").pack(side = BOTTOM)
slide_control_2.pack(padx=20, pady=5, side = LEFT)

slide_control_3 = Frame(slide_box, bd = 0, highlightbackground="green", highlightcolor="green", highlightthickness=1)
slide_v3 = Scale(slide_control_3, from_=1600, to=0, length=200, variable=slideVar3, command=slider_callback_3)
slide_v3.set(0)
slide_v3.pack()
Label(slide_control_3, text="    Motor 3").pack(side = BOTTOM)
slide_control_3.pack(padx=20, pady=5, side = LEFT)

slide_control_4 = Frame(slide_box, bd = 0, highlightbackground="green", highlightcolor="green", highlightthickness=1)
slide_v4 = Scale(slide_control_4, from_=1600, to=0, length=200, variable=slideVar4, command=slider_callback_4)
slide_v4.set(0)
slide_v4.pack()
Label(slide_control_4, text="    Motor 4").pack(side = BOTTOM)
slide_control_4.pack(padx=20, pady=5, side = LEFT)

slide_control_5 = Frame(slide_box, bd = 0, highlightbackground="green", highlightcolor="green", highlightthickness=1)
slide_v5 = Scale(slide_control_5, from_=1600, to=0, length=200, variable=slideVar5, command=slider_callback_5)
slide_v5.set(0)
slide_v5.pack()
Label(slide_control_5, text="    Motor 5").pack(side = BOTTOM)
slide_control_5.pack(padx=20, pady=5, side = LEFT)

slide_control_6 = Frame(slide_box, bd = 0, highlightbackground="green", highlightcolor="green", highlightthickness=1)
slide_v6 = Scale(slide_control_6, from_=1600, to=0, length=200, variable=slideVar6, command=slider_callback_6)
slide_v6.set(0)
slide_v6.pack()
Label(slide_control_6, text="    Motor 1").pack(side = BOTTOM)
slide_control_6.pack(padx=20, pady=5, side = LEFT)

slide_control_7 = Frame(slide_box, bd = 0, highlightbackground="green", highlightcolor="green", highlightthickness=1)
slide_v7 = Scale(slide_control_7, from_=1600, to=0, length=200, variable=slideVar7, command=slider_callback_7)
slide_v7.set(0)
slide_v7.pack()
Label(slide_control_7, text="    Motor 1").pack(side = BOTTOM)
slide_control_7.pack(padx=20, pady=5, side = LEFT)

slide_control_8 = Frame(slide_box, bd = 0, highlightbackground="green", highlightcolor="green", highlightthickness=1)
slide_v8 = Scale(slide_control_8, from_=1600, to=0, length=200, variable=slideVar8, command=slider_callback_8)
slide_v8.set(0)
slide_v8.pack()
Label(slide_control_8, text="    Motor 8").pack(side = BOTTOM)
slide_control_8.pack(padx=20, pady=5, side = LEFT)

button_box = Frame(master)
button_box.pack(side=RIGHT)
Button(button_box, text='Set Full', command=all_full).pack(pady=5)
Button(button_box, text='Set Mid', command=all_mid).pack(pady=5)
Button(button_box, text='All Off', command=all_off).pack(pady=5)


mainloop()

# https://www.python-course.eu/tkinter_sliders.php
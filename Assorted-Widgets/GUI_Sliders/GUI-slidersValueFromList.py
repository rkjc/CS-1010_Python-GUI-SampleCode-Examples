import tkinter as tk

# set slider value based on list values
# https://stackoverflow.com/questions/25745011/how-to-use-tkinter-slider-scale-widget-with-discrete-steps

valuelist = [0,10,30,60,100,150,210,270]

def valuecheck(value):
    newvalue = min(valuelist, key=lambda x:abs(x-float(value)))
    slider.set(newvalue)

root = tk.Tk()

slider = tk.Scale(root, from_=min(valuelist), to=max(valuelist), length=200, command=valuecheck, orient="horizontal")
slider.pack()

root.mainloop()
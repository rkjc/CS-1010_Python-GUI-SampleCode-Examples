
#Could also be used to abort softly if wrong Python version or missing library
 
try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

count = 0
def doBut1():
    global count
    mssg = "pressed " + str(count) + " times"
    label_1.configure(text=mssg)
    count += 1



groot = tk.Tk()
groot.geometry("200x100")

label_1 = tk.Label(groot, text="empty")
label_1.pack()

but1 = tk.Button(groot, text="ONE", command=doBut1, width=10)
but1.pack()



groot.mainloop()

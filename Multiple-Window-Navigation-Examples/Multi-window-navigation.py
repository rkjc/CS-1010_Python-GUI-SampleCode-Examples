
from tkinter import *

groot = Tk()
groot.geometry("400x400")


# ====================== start of window-two code ======================
def open_window_two():
    window_two = Tk()
    window_two.geometry("300x200")
    # hides the root window
    groot.withdraw()

    # functions to be called while running the Top window
    def close_window_two():
        window_two.destroy()
        # unhides the root window
        groot.deiconify()

    # adding widgets to the Top window
    lbl_2 = Label(window_two, text="on window number two")
    lbl_2.pack()

    btn_2 = Button(window_two, text="close and return to root", command=close_window_two)
    btn_2.pack()

    # closes root if the top window is closed with the 'x'
    # groot.protocol("WM_DELETE_WINDOW", top_1.iconify)

    # start the Top window
    window_two.mainloop()

# ====================== end of Top window code ======================

# adding widgets to the main root window
lbl_1 = Label(groot, text="label is on the window-one")
lbl_1.pack()

btn_1 = Button(groot, text="open window two", command=open_window_two)
btn_1.pack()


groot.mainloop()
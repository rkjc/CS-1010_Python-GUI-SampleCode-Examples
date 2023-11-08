
from tkinter import *

groot = Tk()
groot.geometry("400x400")

def exit_program():
    exit()

# ====================== start of window-two code ======================
def open_window_two():

    # ====================== start of window-three code ======================
    def open_window_three():
        window_three = Tk()
        window_three.geometry("300x200")
        # hides the previous window
        window_two.withdraw()

        # functions to be called while running in window three
        def exit_program():
            exit()

        def close_three():
            window_three.destroy()
            # hides the previous window
            window_two.deiconify()

        # adding widgets to the Top window
        lbl_2 = Label(window_three, text="on window number three")
        lbl_2.pack()

        btn_2 = Button(window_three, text="close and return to window-two", command=close_three)
        btn_2.pack()

        btn_4 = Button(window_three, text="exit", command=exit_program)
        btn_4.pack()

        # closes root if the top window is closed with the 'x'
        # groot.protocol("WM_DELETE_WINDOW", window_three.iconify)

        # start the Top window
        window_three.mainloop()
        # ====================== end of window-three code ======================

    # ====================== start of window-four code ======================
    def open_window_four():
        window_four = Tk()
        window_four.geometry("300x200")
        # hides the previous window
        window_two.withdraw()

        # functions to be called while running in window three
        def exit_program():
            exit()

        def close_four():
            window_four.destroy()
            # unhides the root window
            window_two.deiconify()

        # adding widgets to the Top window
        lbl_2 = Label(window_four, text="on window number four")
        lbl_2.pack()

        btn_2 = Button(window_four, text="close and return to window-two", command=close_four)
        btn_2.pack()

        btn_4 = Button(window_four, text="exit", command=exit_program)
        btn_4.pack()

        # closes root if the top window is closed with the 'x'
        # groot.protocol("WM_DELETE_WINDOW", window_three.iconify)

        # start the Top window
        window_four.mainloop()
        # ====================== end of window-four code ======================

    # functions to be called while running window two
    def close_two():
        window_two.destroy()
        # unhides the root window
        groot.deiconify()

    def exit_program():
        exit()

    window_two = Tk()
    window_two.geometry("300x200")
    # hides the root window
    groot.withdraw()

    # adding widgets to the Top window
    lbl_2 = Label(window_two, text="on window number two")
    lbl_2.pack()

    btn_2 = Button(window_two, text="close and return to window-one", command=close_two)
    btn_2.pack()

    btn_3 = Button(window_two, text="open window three", command=open_window_three)
    btn_3.pack()

    btn_5 = Button(window_two, text="open window four", command=open_window_four)
    btn_5.pack()

    btn_4 = Button(window_two, text="exit", command=exit_program)
    btn_4.pack()

    # closes root if the top window is closed with the 'x'
    # groot.protocol("WM_DELETE_WINDOW", window_two.iconify)

    # start the Top window
    window_two.mainloop()

# ====================== end of window-two code ======================

# adding widgets to the main root window
lbl_1 = Label(groot, text="label is on window one")
lbl_1.pack()

btn_1 = Button(groot, text="open window two", command=open_window_two)
btn_1.pack()

btn_2 = Button(groot, text="exit", command=exit_program)
btn_2.pack()

groot.mainloop()
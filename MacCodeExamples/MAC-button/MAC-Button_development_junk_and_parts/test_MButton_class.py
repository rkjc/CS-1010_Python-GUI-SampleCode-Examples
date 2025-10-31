import tkinter as tk
import MAC_button as mbtn

groot = tk.Tk()

bob = mbtn.MButton(groot, text='fun')
bob.mpack()


groot.mainloop()

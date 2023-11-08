import tkinter as tk

groot = tk.Tk()
groot.geometry("300x300")


myFoxImg = tk.PhotoImage(file="foxImage.png")


lbl1 = tk.Label(groot, text="picture of fox", image=myFoxImg)
lbl1.pack()

groot.mainloop()

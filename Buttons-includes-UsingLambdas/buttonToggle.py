import tkinter as tk

main = tk.Tk()
main.geometry("300x100")

but1_state = False
 
def doBut1():
    global but1_state
    but1_state = not(but1_state)
    if but1_state:
       but1.configure(text="ON")
    else:
       but1.configure(text="OFF")
    

but1 = tk.Button(main, text="OFF", command=doBut1, width=10, height=3)
but1.pack()

main.mainloop()

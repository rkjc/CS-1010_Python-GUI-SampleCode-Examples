 
import tkinter as tk
 
def thisButton():
    label_1.configure(bg="red")
    label_2.configure(bg="blue")
    button_1.configure(bg="orange")
 
main = tk.Tk()
 
label_1 = tk.Label(main, text="Label one")
label_2 = tk.Label(main, text="Label two")
button_1 = tk.Button(main, text="Button ONE", command=thisButton)


button_1.pack(side="left", ipadx=50, padx=50, ipady=50)
label_1.pack(side=tk.RIGHT)
label_2.pack(side=tk.LEFT)
 
main.mainloop()

 
import tkinter as tk
 
groot = tk.Tk()
groot.geometry("300x200")

# --------------- function -------------
 
def func_one():
    str_var1 = ent_1.get()
    str_var1 = "Hi there " + str_var1
    lab_2.configure(text=str_var1)

# ------------ widgets ----------------------
 
lab_1 = tk.Label(groot, text = "Enter User Name")
ent_1 = tk.Entry(groot)
but_1 = tk.Button(groot, text="post the entry", command=func_one)
lab_2 = tk.Label(groot, text = "---------------")


# ------------ layout --------------------

lab_1.pack()
but_1.pack()
ent_1.pack()
lab_2.pack()
 
groot.mainloop()

 
import tkinter as tk
 
root = tk.Tk()
root.geometry("500x300")
 
def printText():
    txt_var = myBox.get("1.0","end-1c")
    print(txt_var)
 
myBox = tk.Text(root, width=50, height=10)
myBox.insert(tk.INSERT, "Hello....o\n")
myBox.insert(tk.INSERT, "-and-\n")
myBox.insert(tk.END, "Bye Bye....o")
myBox.pack()
 
B1 = tk.Button(root, text="print to terminal", command=printText)
B1.pack()
 
root.mainloop()

import tkinter as tk

root = tk.Tk()
root.geometry("500x300")

def printText():
    txt_var = txbx.get("1.0","end-1c")
    print(txt_var)

txbx = tk.Text(root, width=50, height=10)
txbx.insert(tk.INSERT, "Hello....o\n")
txbx.insert(tk.INSERT, "-and-\n")
txbx.insert(tk.END, "Bye Bye....o")
txbx.pack()

B1 = tk.Button(root, text="print to terminal", command=printText)
B1.pack()

root.mainloop()

# https://www.geeksforgeeks.org/python-tkinter-text-widget/
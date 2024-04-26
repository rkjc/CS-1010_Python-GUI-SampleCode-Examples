import tkinter as tk

root = tk.Tk()
root.title("root")
root.geometry("400x400")

def doThis(event):
    lbl_1.config(text="button is down", bg="cyan")

def doThat(event):
    lbl_1.config(text="button is up", bg="lightgreen")

lbl_1 = tk.Label(root, height=3, text="Click the left mouse button")
lbl_1.pack(fill=tk.BOTH)

root.bind( "<Button-1>", doThis)
root.bind( "<ButtonRelease-1>", doThat)
root.mainloop()

# http://www.java2s.com/Tutorial/Python/0360__Tkinker/Mouseeventsexample.htm

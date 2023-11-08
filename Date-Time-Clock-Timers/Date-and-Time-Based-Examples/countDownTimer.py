import tkinter as tk

count = 50

def onUpdate():
    global count
    if count >= 0:
        lbl_1.config(text=count)
        count -= 1
        # the function '.after' waits that many millisecs and calls the function
        root.after(100, onUpdate)
    else:
        lbl_1.config(text="FINISHED!")


root = tk.Tk()
root.geometry("200x200")

lbl_1 = tk.Label(root, text="time")
lbl_1.pack()

# this calls the timer function to start it
onUpdate()

root.mainloop()




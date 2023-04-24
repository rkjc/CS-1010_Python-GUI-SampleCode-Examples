 
import tkinter as tk

mainwindow = tk.Tk()
mainwindow.title("Multi-window demo code - 1")
mainwindow.geometry("600x500")

mainwindow.columnconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=1)

def showRed():
    btn_1.config(bg='green', text='clicked')

def showGreen():
    btn_2.config(bg='green', text='clicked')

def showBlue():
    btn_3.config(bg='green', text='clicked')

def doOther():
    btn_4.config(bg='green', text='clicked')

# top Frame --------
top_frame = tk.Frame(mainwindow, bg="cyan", highlightbackground="black", highlightthickness=1)
top_frame.grid(row=0, column=0, columnspan=3, sticky=tk.N+tk.W+tk.E)

# bottom Frame --------
bottom_frame = tk.Frame(mainwindow, bg="yellow", padx=5, pady=5)
bottom_frame.grid_propagate(False)
bottom_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)

#-------------------------------------------

btn_1 = tk.Button(top_frame, text='Button 1', width='7', command=showRed)
btn_1.grid(row=0, column=0)
#btn_1.grid(row=0, column=0, padx=(10), pady=10)

btn_2 = tk.Button(top_frame, text='Button 2', width='7', command=showGreen)
btn_2.grid(row=0, column=1)
#btn_2.grid(row=0, column=1, padx=(10), pady=10)

btn_3 = tk.Button(top_frame, text='Button 3', width='7', command=showBlue)
btn_3.grid(row=0, column=2)
#btn_3.grid(row=0, column=2, padx=(10), pady=10)

btn_4 = tk.Button(top_frame, text='Button 4', width='7', command=doOther)
btn_4.grid(row=0, column=3)
#btn_4.grid(row=0, column=3, padx=(10), pady=10)

#-------------------------------------------

label_1 = tk.Label(bottom_frame, bg="yellow", text="yep, I'm a label in a frame")
label_1.pack(fill = tk.BOTH, expand = True)

mainwindow.mainloop()
#https://stackoverflow.com/questions/50422735/tkinter-resize-frame-and-contents-with-main-window

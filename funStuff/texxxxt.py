import tkinter as tk
 
groot = tk.Tk()
groot.geometry("500x350")
groot.title("Text widget with Scrollbar in Frame")
 
# https://en.wikipedia.org/wiki/Tkinter
pileOtext = """Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python
interface to the Tk GUI toolkit, and is Python's de facto standard GUI.[2]
Tkinter is included with standard Linux, Microsoft Windows and Mac OS X installs of Python.
The name Tkinter comes from Tk interface. Tkinter was written by Fredrik Lundh.[3]
Tkinter is free software released under a Python license.[4]
 
As with most other modern Tk bindings, Tkinter is implemented as a Python wrapper around a complete
Tcl interpreter embedded in the Python interpreter. Tkinter calls are translated into Tcl commands
which are fed to this embedded interpreter, thus making it possible to mix Python and Tcl in a single application.
 
There are several popular GUI library alternatives available, such as wxPython, PyQt, PySide, Pygame, Pyglet, and PyGTK. """
 
# using a Frame to group the Text and Scrollbar together
frame1 = tk.Frame(groot, width=300, height=400, highlightbackground="black", highlightthickness=1)
frame1.pack()
 
scrollbar_tk = tk.Scrollbar(frame1)
 
text_tk = tk.Text(frame1,  height=12, yscrollcommand=scrollbar_tk.set)
text_tk.insert(tk.INSERT, pileOtext)
 
text_tk.pack(side=tk.LEFT)
scrollbar_tk.pack(side=tk.LEFT, fill=tk.Y)
scrollbar_tk.config(command=text_tk.yview)
groot.mainloop()
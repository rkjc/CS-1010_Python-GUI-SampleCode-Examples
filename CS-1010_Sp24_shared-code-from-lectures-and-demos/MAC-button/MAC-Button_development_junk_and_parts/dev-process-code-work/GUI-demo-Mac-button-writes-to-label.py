import tkinter as tk

colorOn = True

"""
On Mac to change the Button background color use the configuration attribute 'highlightbackground='
On Windows and Linux the attribute 'bg=' will change the Button background color.
On Linux to change the color when the mouse is hovering over the Button change the attribute 'activebackground='
For all systems changing the attribute 'fg=' will change the color of the text.
"""
def doButton():
   global colorOn
   colorOn = not colorOn
   if colorOn == True:
      L1.config(text="button is red")
      B1.config(fg='black', bg='red', highlightbackground='red', activebackground='red')
   else:
      L1.config(text="button is blue")
      B1.config(bg='blue', fg='white', highlightbackground='blue', activebackground='blue')

main = tk.Tk()
main.geometry("300x200")

L1 = tk.Label(main, text="This is a Label")
L1.pack()


B1 = tk.Button(main, text='Push the Button', command=doButton)
B1.pack()

main.mainloop( )

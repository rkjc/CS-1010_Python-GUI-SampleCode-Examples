from tkinter import *

class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # method call counter
        self.pack()
        self.afterId = None
        root.bind('<KeyPress-a>', self.key_press)
        root.bind('<KeyRelease-a>', self.key_release)
        
    def key_press(self, event):
        if self.afterId != None:
            self.after_cancel( self.afterId )
            self.afterId = None
        else:
            print ('key pressed %s' % event.time)

    def key_release(self, event):
        self.afterId = self.after_idle( self.process_release, event )

    def process_release(self, event):
        print ('key release %s' % event.time)
        self.afterId = None
        
root = Tk()
root.geometry("400x100+0+0")
app1 = MyFrame(root)
root.mainloop()


'''
https://www.daniweb.com/programming/software-development/threads/70746/keypress-event-with-holding-down-the-key

the original example was written for Python-2
2023-03-07
rkjc - made changes to run on Pyhon-4

opens blank window
listens for 'a' key when window is in focus 
'''

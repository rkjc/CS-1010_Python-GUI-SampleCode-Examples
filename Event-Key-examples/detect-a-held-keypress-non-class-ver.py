from tkinter import *

space_key_down = False

# ------------- hold down key check ------------
afterId = None
def key_hold_press(event):
    global afterId
    global space_key_down
    space_key_down = True
    if afterId != None:
        groot.after_cancel( afterId )
        afterId = None
    else:
        print ('key pressed %s' % event.time)

def key_hold_release(event):
    global afterId
    afterId = groot.after_idle( key_hold_process_release, event )

def key_hold_process_release(event):
    global afterId
    global space_key_down
    space_key_down = False
    print ('key release %s' % event.time)
    afterId = None
        
groot = Tk()
groot.geometry("400x100+0+0")

groot.bind("<KeyPress-space>", key_hold_press)
groot.bind("<KeyRelease-space>", key_hold_release)

groot.mainloop()


'''
source of original code snip
https://www.daniweb.com/programming/software-development/threads/70746/keypress-event-with-holding-down-the-key

the original example was written for Python-2
and used an object class based apprach

rkjc [2023-03-07] - made changes to run on Pyhon-4
and re-wrote so that is is simple procedural code 

opens blank window
listens for 'space' key when window is in focus

I'm not entirely sure how this code works???
but it seems to be non-blocking and works as a
mouse event modifiyer key in a canvas graphics manipulation porgram
'''

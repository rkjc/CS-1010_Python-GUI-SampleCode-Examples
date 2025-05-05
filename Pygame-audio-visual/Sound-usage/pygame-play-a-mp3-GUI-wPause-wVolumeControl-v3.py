from pygame import mixer
from tkinter import *

groot = Tk()
groot.geometry("500x450")

# Starting the mixer
mixer.init()

# Loading the song
song_file_name = "HoldOnTight.mp3"
mixer.music.load(song_file_name)

# Setting the volume
mixer.music.set_volume(0.7)

#paused = mixer.music.get_busy()
paused = False

def play_music():
    global paused
    # Start playing the song
    mixer.music.play()
    mixer.music.unpause()
    paused = False
    btn_3.config(text="pause")

def pause_music():
    global paused
    # Pausing the music
    if paused == True:
        mixer.music.unpause()
        btn_3.config(text="pause")
    else:
        mixer.music.pause()
        btn_3.config(text="unpause")
    paused = not paused

def stop_music():
    global paused
    # Stop the mixer
    mixer.music.stop()
    mixer.music.unpause()
    paused = False
    btn_3.config(text="pause")


lbl_2 = Label(groot, text=song_file_name)
lbl_2.pack()

btn_2 = Button(groot, text="play", command=play_music)
btn_2.pack()

btn_3 = Button(groot, text="pause", command=pause_music)
btn_3.pack()

btn_5 = Button(groot, text="stop", command=stop_music)
btn_5.pack()


# --- vol -----
# Need to use the special tkinter.IntVar() variable
# to connect the radio buttons together as a group
myIntThing = IntVar()

# sets which button will be selected by default
myIntThing.set( 0 )


def doButt():
    temp_var = myIntThing.get()
    L1.configure(text=temp_var)
    vol = float(temp_var) * 0.01
    mixer.music.set_volume(vol)

L2 = Label(groot, text="volume control")
L2.pack()

L1 = Label(groot, text="selection", font=('arial', 20))
L1.pack()


for y in range(0,10):
    aFrame = Frame(groot)
    for x in range(1,10):
        vol = x + (y * 10)
        tempRadButt = Radiobutton(aFrame)
        tempRadButt.config(text=str(vol), variable=myIntThing, value=vol, command=doButt)
        tempRadButt.pack(side='left')
    aFrame.pack()
    
# ------------------------------------

groot.mainloop()

# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/

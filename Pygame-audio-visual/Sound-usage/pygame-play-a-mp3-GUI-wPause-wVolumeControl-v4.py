from pygame import mixer
from tkinter import *
from tkinter import filedialog

groot = Tk()
groot.geometry("550x450")

# Starting the mixer
mixer.init()

# Loading the song (hard coded in this version)
song_file_name = "HoldOnTight.mp3"
mixer.music.load(song_file_name)

# Setting the volume
mixer.music.set_volume(0.2)

store_vol = mixer.music.get_volume()

#paused = mixer.music.get_busy()
paused = False

def openFile():
    global song_file_name
    #global tempstr
    groot.filename =  filedialog.askopenfilename(title = "Select file")
    song_file_name = groot.filename
    mixer.music.load(song_file_name)
    trimmedSongName = song_file_name
    slashLoc = trimmedSongName.rindex('/')
    trimmedSongName = trimmedSongName[slashLoc + 1 : ]
    lbl_2.config(text=trimmedSongName)
    
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


def changeVol():
    global is_mute
    if is_mute:
        mute_music()
    temp_var = currentVol.get()
    L1.configure(text=temp_var)
    vol = float(temp_var) * 0.01
    mixer.music.set_volume(vol)
  
is_mute = False    
def mute_music():
    global is_mute
    global store_vol
    is_mute = not is_mute
    if is_mute:
        btn_6.config(bg="lightblue",highlightbackground='lightblue', activebackground='lightblue')
        store_vol = mixer.music.get_volume()
        mixer.music.set_volume(0)
    else:
        btn_6.config(bg="gray86",highlightbackground='gray72', activebackground='gray86')
        mixer.music.set_volume(store_vol)

now_playing = "Now Playing >>  " + song_file_name
lbl_2 = Label(groot, text=now_playing, font=('arial', 16), highlightbackground="orange", highlightthickness=2)
lbl_2.pack()

controls_frame = Frame(groot, highlightbackground="green", highlightthickness=2)

btn_2 = Button(controls_frame, text="play", command=play_music, font=('arial', 14))
btn_2.pack(side='left')

btn_3 = Button(controls_frame, text="pause", command=pause_music, font=('arial', 14))
btn_3.pack(side='left')

btn_5 = Button(controls_frame, text="stop", command=stop_music, font=('arial', 14))
btn_5.pack(side='left')

space_lbl = Label(controls_frame, bg='gray90', text="   ", font=('arial', 14))
space_lbl.pack(side='left')

btn_6 = Button(controls_frame, text="mute", command=mute_music, font=('arial', 14))
btn_6.pack(side='left')

btn_7 = Button(controls_frame, text="Select song", command=openFile, font=('arial', 14))
btn_7.pack(side='left')

controls_frame.pack()
# --- vol -----
# Need to use the special tkinter.IntVar() variable
# to connect the radio buttons together as a group
currentVol = IntVar()




vol_labl_frm = Frame(groot, highlightbackground="blue", highlightthickness=2)
L2 = Label(vol_labl_frm, text="volume control >>  ", font=('arial', 14))
L2.pack(side='left')

L1 = Label(vol_labl_frm, text="21", font=('arial', 14))
L1.pack(side='left')



volFrame = Frame(groot, highlightbackground="magenta", highlightthickness=2)
first_run = True

# sets which button will be selected by default
currentVol.set(21)

for y in range(0,10):
    aFrame = Frame(volFrame)
   
    for x in range(1,11):
        vol = (y * 10) + x
        if x % 10 == 0:
            vol_str = str(x * (y + 1))
        else:
            vol_str = str(y) + str(x)
        tempRadButt = Radiobutton(aFrame)
        tempRadButt.config(text=vol_str, variable=currentVol, value=vol, command=changeVol)
        tempRadButt.pack(side='left')
    aFrame.pack()
volFrame.pack()

vol_labl_frm.pack()
# ------------------------------------

groot.mainloop()

# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/

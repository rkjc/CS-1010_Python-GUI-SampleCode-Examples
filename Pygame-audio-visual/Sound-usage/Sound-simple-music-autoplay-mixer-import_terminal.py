# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/
from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("HoldOnTight.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

mixer.music.play()

input()



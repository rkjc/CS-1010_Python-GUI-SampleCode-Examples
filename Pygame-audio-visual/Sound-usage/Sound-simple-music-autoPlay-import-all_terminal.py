# https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/
# from pygame import mixer
import pygame

# Starting the mixer
pygame.mixer.init()

# Setting the volume
pygame.mixer.music.set_volume(0.7)

# Loading the song
pygame.mixer.music.load("HoldOnTight.mp3")



pygame.mixer.music.play()

input()



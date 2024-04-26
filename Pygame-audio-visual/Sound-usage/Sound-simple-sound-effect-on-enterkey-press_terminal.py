 
from pygame import mixer
import sys

mixer.init()

while(True):
    cash_sound=mixer.Sound("Various-06.wav")
    mixer.Sound.play(cash_sound)
    input()

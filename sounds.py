import os
import pygame.mixer
from pygame.mixer import Sound
from signal import pause


pygame.mixer.init()

if not os.path.exists("StarWars3.wav"):
    os.system("wget https://www2.cs.uic.edu/~i101/SoundFiles/StarWars3.wav")

sound = Sound("StarWars3.wav")
sound.play()

pause()

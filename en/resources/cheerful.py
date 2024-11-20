import pygame
import time

time.sleep(3)
pygame.init()
my_sound = pygame.mixer.Sound('/home/username/start.mp3')  # Change `username` to your username

my_sound.play()

while pygame.mixer.get_busy():
    time.sleep(0.1)
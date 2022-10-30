# ----------------------------- Healthy Programmer ----------------------

# 9 AM - 5 PM
# Water -Water.mp3 (3.5L) -Drank -Log
# Eyes - Eyes.mp3 ---every 30 min -EyDone -log
# Physical Activity - physical.mp3 every-45 min -ExDone - log

# import pygame
#
# pygame.mixer.init()
# pygame.mixer.music.load('sample.mp3')
# pygame.mixer.music.play()

import pygame
pygame.init()
#pygame.display.set_mode((200,100))
pygame.mixer.music.load("water.mp3")
pygame.mixer.music.play(0)

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)
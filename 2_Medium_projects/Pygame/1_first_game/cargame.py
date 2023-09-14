import pygame
from pygame.locals import *

pygame.init()

# run
running = True
# set screen size
screen = pygame.display.set_mode((800,800))
# set window name
pygame.display.set_caption("Car game")
# set bg color
screen.fill((60,220,0))
# apply changes
pygame.display.update()

# while loop is for setting game do not auto stop, but after pressing "close button"
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
pygame.quit()
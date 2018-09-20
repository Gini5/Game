import pygame
import math
import random

# initilize the game and set display window
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width,height))

# set keys to record if player press down the key: WASD
keys = [False, False, False, False]
# current player position
playerpos = [100, 100]
# accuracy variable, record number of shoots and shooted animals
acc = [0, 0]
# track arrow
arrows = []
# set a timer, after a certain period of time, create a new bad animal
badtimer = 100
badtimer1 = 0
badguys = [[640, 100]]
healthvalue = 194

# initialize sound
pygame.mixer.init()

# load pictures
rabbit_img = pygame.image.load("resources/images/dude.png")
grass_img = pygame.image.load("resources/images/grass.png")
castle_img = pygame.image.load("resources/images/castle.png")

while True:
    # set background to color gray(RGB)
    screen.fill((224,226,229))
    #add grass and castles to backgrounds
    grass_width, grass_height = grass_img.get_width(), grass_img.get_height()
    for x in range(width//grass_width+1):
        for y in range(height//grass_height+1):
            screen.blit(grass_img, (x*grass_width, y*grass_height))
    screen.blit(castle_img, (0, 30))
    screen.blit(castle_img, (0, 135))
    screen.blit(castle_img, (0, 240))
    screen.blit(castle_img, (0, 345))
    # load rabbit pic
    screen.blit(rabbit_img, (100, 100))
    # update screen
    pygame.display.flip()
    # check some events, if has QUIT command, then exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
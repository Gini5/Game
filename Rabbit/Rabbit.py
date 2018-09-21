import pygame
from pygame.locals import *
import math
import random

# initilize the game and set display window
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width,height))

# set keys to record if player press down the key: WASD
WASD = [K_w, K_a, K_s, K_d]
keys = [False, False, False, False]
# current player position
playerpos = [200, 150]
# accuracy variable, record number of shoots and shooted animals
acc = [0, 0]
# track bullet: each bullet contains [clickposition to playerposition tan,playerposition x, playerposition y]]
bullets = []
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
bullet_img = pygame.image.load("resources/images/bullet.png")
badguy_img = pygame.image.load("resources/images/badguy.png")
badguy_img2 = badguy_img

while True:
    # set background to color gray(RGB)
    screen.fill((224,226,229))
    # add grass and castles to backgrounds
    grass_width, grass_height = grass_img.get_width(), grass_img.get_height()
    for x in range(width//grass_width+1):
        for y in range(height//grass_height+1):
            screen.blit(grass_img, (x*grass_width, y*grass_height))
    screen.blit(castle_img, (0, 30))
    screen.blit(castle_img, (0, 135))
    screen.blit(castle_img, (0, 240))
    screen.blit(castle_img, (0, 345))

    # load rabbit pic, rotate according to mouse position
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(rabbit_img, 360 - angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)

    # draw bullet
    for bullet in bullets:
        index = 0
        velx = math.cos(bullet[0])*10   # calculate bullet to player delta x
        vely = math.sin(bullet[0])*10   # calculate bullet to player delta y
        # calculate new bullet position
        bullet[1] += velx
        bullet[2] += vely
        # check if bullet is out of the screen, if yes, stop
        if bullet[1]<-64 or bullet[1]>width or bullet[2]<-64 or bullet[2]>height:
            bullets.pop(index)
        index += 1
        # draw bullet
        # for projectile in bullets:
        if bullets:
            projectile = bullets[0]
            arrow = pygame.transform.rotate(bullet_img, 360-projectile[0]*57.29)
            screen.blit(arrow, (projectile[1], projectile[2]))

    # display bad guys
    # if badtimer is 0, create a badguy and reset timer to 0
    if badtimer == 0:
        badguys.append([640,random.randint(50, 430)])
        badtimer = 100 - (badtimer1*2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5
    index_badguy = 0
    for bg in badguys:
        if bg[0] < -64:
            badguys.pop(index_badguy)
        bg[0] -= 7
        badrect = pygame.Rect(badguy_img.get_rect())
        badrect.top = bg[1]
        badrect.left = bg[0]
        if badrect.left < 64:
            healthvalue -= random.randint(5,20)
            badguys.pop(index_badguy)
        index_arrow = 0
        for bullet in bullets:
            bulletrect = pygame.Rect(bullet_img.get_rect())
            bulletrect.top = bullet[2]
            bulletrect.left = bullet[1]
            if badrect.colliderect(bulletrect):
                acc[0] += 1     #shoots +1
                badguys.pop(index_badguy)
                bullets.pop(index_arrow)
        index_badguy += 1
    for bg in badguys:
        screen.blit(badguy_img, bg)

    # update screen
    pygame.display.flip()

    # check some events
    for event in pygame.event.get():
        # if has QUIT command, then exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # for WASD key press events
        if event.type == pygame.KEYDOWN:
            if event.key in WASD:
                keys[WASD.index(event.key)] = True
        if event.type == pygame.KEYUP:
            if event.key in WASD:
                keys[WASD.index(event.key)] = False
        #  when mouse click, shoot a bullet
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            bullets.append([math.atan2(position[1]-(playerpos1[1]+32), position[0]-(playerpos1[0]+26)),
						   playerpos1[0]+32, playerpos1[1]+26])

    # move the player
    if keys[0]: playerpos[1] -= 5
    elif keys[2]: playerpos[1] += 5
    if keys[1]: playerpos[0] -= 5
    elif keys[3]: playerpos[0] += 5
    badtimer -= 1
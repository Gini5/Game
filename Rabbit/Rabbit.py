import pygame
from pygame.locals import *
import math
import random
import time

def startgame():
    # initilize the game and set display window
    pygame.init()
    t0 = time.time()    # initialize time when game is started
    width, height = 640, 480
    screen = pygame.display.set_mode((width,height))

    # set keys to record if player press down the key: WASD
    WASD = [K_w, K_a, K_s, K_d]
    keys = [False, False, False, False]
    # current player position
    playerpos = [200, 150]
    # accuracy variable, record number of shooted animals and shoots
    acc = [0, 0]
    # track bullet: each bullet contains [clickposition to playerposition tan,playerposition x, playerposition y]]
    bullets = []
    # set a timer, after a certain period of time, create a new bad animal
    badtimer = 100
    badtimer1 = 0
    badguys = [[640, 100]]
    healthvalue = 194   #according to width of health bar image
    # set move speed
    bulletspeed = 10
    badguyspeed = 5

    # initialize sound
    pygame.mixer.init()

    # load pictures
    rabbit_img = pygame.image.load("resources/images/dude.png")
    grass_img = pygame.image.load("resources/images/grass.png")
    castle_img = pygame.image.load("resources/images/castle.png")
    bullet_img = pygame.image.load("resources/images/bullet.png")
    badguy_img = pygame.image.load("resources/images/badguy.png")
    badguy_img2 = badguy_img
    healthbar_img = pygame.image.load("resources/images/healthbar.png")
    health_img = pygame.image.load("resources/images/health.png")
    gameover_img = pygame.image.load("resources/images/gameover.png")
    youwin_img = pygame.image.load("resources/images/youwin.png")

    # load sound
    hit = pygame.mixer.Sound("resources/audio/explode.wav")
    enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
    shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
    hit.set_volume(0.05)
    enemy.set_volume(0.05)
    shoot.set_volume(0.05)

    # load bgm
    pygame.mixer.music.load('resources/audio/moonlight.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)

    running = True
    exitcode = False
    while running:
        t1 = time.time()
        dt = t1 - t0
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
            velx = math.cos(bullet[0])*bulletspeed   # calculate bullet to player delta x
            vely = math.sin(bullet[0])*bulletspeed   # calculate bullet to player delta y
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
            bg[0] -= badguyspeed
            badrect = pygame.Rect(badguy_img.get_rect())
            badrect.top = bg[1]
            badrect.left = bg[0]
            if badrect.left < 64:
                hit.play()
                healthvalue -= random.randint(5,20)
                badguys.pop(index_badguy)
            index_arrow = 0
            for bullet in bullets:
                bulletrect = pygame.Rect(bullet_img.get_rect())
                bulletrect.top = bullet[2]
                bulletrect.left = bullet[1]
                if badrect.colliderect(bulletrect):
                    enemy.play()
                    acc[0] += 1     # animal shooted +1
                    badguys.pop(index_badguy)
                    bullets.pop(index_arrow)
            index_badguy += 1
        for bg in badguys:
            screen.blit(badguy_img, bg)

        #add timer to display time
        font = pygame.font.SysFont('arial', 24)
        survivedtext = font.render(str((90-int(dt))//60)+": "+
                                   str((90-int(dt))%60).zfill(2), True, (0, 0, 0))
        textRect = survivedtext.get_rect()
        textRect.topright = [635,5]
        screen.blit(survivedtext, textRect)
        # add health bar
        screen.blit(healthbar_img, (5, 5))
        for h in range(healthvalue):
            screen.blit(health_img, (h+8, 8))

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
                shoot.play()
                position = pygame.mouse.get_pos()
                acc[1] += 1     #shoots +1
                bullets.append([math.atan2(position[1]-(playerpos1[1]+32), position[0]-(playerpos1[0]+26)),
                               playerpos1[0]+32, playerpos1[1]+26])

        # move the player
        if keys[0]: playerpos[1] -= 5
        elif keys[2]: playerpos[1] += 5
        if keys[1]: playerpos[0] -= 5
        elif keys[3]: playerpos[0] += 5
        badtimer -= 1

        # judge win or lose:
        # if time reaches 90s, stop the game
        if dt >= 90:
            running = False
            exitcode = True
        # if health value is lower than 0, stop the game
        if healthvalue <= 0:
            running = False
            exitcode = False
        # calculate the accuracy
        if acc[1] != 0:
            accuracy = acc[0]/acc[1]*100
            accuracy = ("%.2f" % accuracy)
        else:
            accuracy = 0

    # handle win or lose situation
    if not exitcode:
        pygame.font.init()
        font = pygame.font.SysFont('arial', 24)
        acctext = font.render("Accuracy: " + str(accuracy) + "%", True, (255, 0, 0))
        acctextRect = acctext.get_rect()
        acctextRect.centerx = screen.get_rect().centerx
        acctextRect.centery = screen.get_rect().centery + 24
        screen.blit(gameover_img, (0, 0))
        screen.blit(acctext, acctextRect)
    else:
        pygame.font.init()
        font = pygame.font.SysFont('arial', 24)
        text = font.render("Accuracy: "+accuracy+"%", True, (0, 255, 0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery + 24
        screen.blit(youwin_img, (0, 0))
        screen.blit(text, textRect)

    # add play again text
    againtext = font.render("Play Again(Press Key: P)", True, (255, 255, 0))
    againtextRect = againtext.get_rect()
    againtextRect.centerx = screen.get_rect().centerx
    againtextRect.centery = screen.get_rect().centery + 48
    screen.blit(againtext, againtextRect)


startgame()

while True:
    playagain = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:    # play again
            if event.key == K_p:
                playagain = True
                break
    if playagain:
        startgame()
    pygame.display.flip()
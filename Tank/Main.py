import pygame,sys
import scene, bullet, food, tanks, home
from pygame.locals import *

def show_start_interface(screen, width, height):
	tfont = pygame.font.Font('./font/simkai.ttf', width//4)
	cfont = pygame.font.Font('./font/simkai.ttf', width//20)
	title = tfont.render(u'坦克大战', True, (255, 0, 0))
	content1 = cfont.render(u'按1键进入单人游戏', True, (0, 0, 255))
	content2 = cfont.render(u'按2键进入双人人游戏', True, (0, 0, 255))
	trect = title.get_rect()
	trect.midtop = (width/2, height/4)
	crect1 = content1.get_rect()
	crect1.midtop = (width/2, height/1.8)
	crect2 = content2.get_rect()
	crect2.midtop = (width/2, height/1.6)
	screen.blit(title, trect)
	screen.blit(content1, crect1)
	screen.blit(content2, crect2)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					return 1
				if event.key == pygame.K_2:
					return 2

def show_end_interface(screen, width, height, is_win):
	bg_img = pygame.image.load("./images/others/background.png")
	screen.blit(bg_img, (0, 0))
	if is_win:
		font = pygame.font.Font('./font/simkai.ttf', width//10)
		content = font.render(u'恭喜通关！', True, (255, 0, 0))
		rect = content.get_rect()
		rect.midtop = (width/2, height/2)
		screen.blit(content, rect)
	else:
		fail_img = pygame.image.load("./images/others/gameover.png")
		rect = fail_img.get_rect()
		rect.midtop = (width/2, height/2)
		screen.blit(fail_img, rect)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
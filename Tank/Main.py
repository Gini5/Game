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

def show_switch_stage(screen, width, height, stage):
	bg_img = pygame.image.load("./images/others/background.png")
	screen.blit(bg_img, (0, 0))
	font = pygame.font.Font('./font/simkai.ttf', width//10)
	content = font.render(u'第%d关' % stage, True, (0, 255, 0))
	rect = content.get_rect()
	rect.midtop = (width/2, height/2)
	screen.blit(content, rect)
	pygame.display.update()
	delay_event = pygame.constants.USEREVENT
	pygame.time.set_timer(delay_event, 1000)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == delay_event:
				return

def main():
	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((630, 630))
	pygame.display.set_caption("坦克大战-公众号: Charles的皮卡丘")
	# load resources
	bg_img = pygame.image.load("./images/others/background.png")
	add_sound = pygame.mixer.Sound("./audios/add.wav")
	add_sound.set_volume(1)
	bang_sound = pygame.mixer.Sound("./audios/bang.wav")
	bang_sound.set_volume(1)
	blast_sound = pygame.mixer.Sound("./audios/blast.wav")
	blast_sound.set_volume(1)
	fire_sound = pygame.mixer.Sound("./audios/fire.wav")
	fire_sound.set_volume(1)
	Gunfire_sound = pygame.mixer.Sound("./audios/Gunfire.wav")
	Gunfire_sound.set_volume(1)
	hit_sound = pygame.mixer.Sound("./audios/hit.wav")
	hit_sound.set_volume(1)
	start_sound = pygame.mixer.Sound("./audios/start.wav")
	start_sound.set_volume(1)
	# show start interface
	num_player = show_start_interface(screen, 630, 630)
	# sound
	start_sound.play()
	# stage
	stage = 0
	num_stage = 2
	is_gameover = False
	clock = pygame.time.Clock()
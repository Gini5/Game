import pygame, random
from classes.Obstacle import Obstacle

def create_obstacles(s, e, num=10):
	obstacles = pygame.sprite.Group()
	locations = []
	for i in range(num):
		row = random.randint(s, e)
		col = random.randint(0, 9)
		location  = [col*64+20, row*64+20]
		if location not in locations:
			locations.append(location)
			attribute = random.choice(["tree", "flag"])
			img_path = './images/tree.png' if attribute=="tree" else './images/flag.png'
			obstacle = Obstacle(img_path, location, attribute)
			obstacles.add(obstacle)
	return obstacles

def AddObstacles(obstacles0, obstacles1):
	obstacles = pygame.sprite.Group()
	for obstacle in obstacles0:
		obstacles.add(obstacle)
	for obstacle in obstacles1:
		obstacles.add(obstacle)
	return obstacles

def Show_Start_Interface(Demo, width, height):
	Demo.fill((255, 255, 255))
	tfont = pygame.font.Font('./font/simkai.ttf', width//4)
	cfont = pygame.font.Font('./font/simkai.ttf', width//20)
	title = tfont.render(u'滑雪游戏', True, (255, 0, 0))
	content = cfont.render(u'按任意键开始游戏', True, (0, 0, 255))
	trect = title.get_rect()
	trect.midtop = (width/2, height/10)
	crect = content.get_rect()
	crect.midtop = (width/2, height/2.2)
	Demo.blit(title, trect)
	Demo.blit(content, crect)
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				return
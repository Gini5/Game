import pygame
import random


class Brick(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.brick = pygame.image.load('./images/scene/brick.png')
		self.rect = self.brick.get_rect()
		self.being = False


class Iron(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.iron = pygame.image.load('./images/scene/iron.png')
		self.rect = self.iron.get_rect()
		self.being = False
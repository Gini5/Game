import pygame
import random

# food for tank
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.food_boom = './images/food/food_boom.png'
        self.food_clock = './images/food/food_clock.png'
        self.food_gun = './images/food/food_gun.png'
        self.food_iron = './images/food/food_gun.png'
        self.food_protect = './images/food/food_protect.png'
        self.food_star = './images/food/food_star.png'
        self.food_tank = './images/food/food_tank.png'
        self.foods = [self.food_boom, self.food_clock, self.food_gun, self.food_iron, self.food_protect, self.food_star, self.food_tank]
        self.kind = None
        self.food = None
        self.rect = None
        self.alive = False
        self.time = 1000

    def generate(self):
        self.kind = random.randint(0, 6)
        self.food = pygame.image.load(self.foods[self.kind]).convert_alpha()
        self.rect = self.food.get_rect()
        self.rect.left, self.rect.top = random.randint(100, 500), random.randint(100, 500)
        self.alive = True
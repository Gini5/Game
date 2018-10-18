import pygame
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, img_path, location, attribute):
        super(Obstacle, self).__init__()
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        self.attribute = attribute
        self.passed = False

    def move(self, num):
        self.rect.centery = self.location[1] - num

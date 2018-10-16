import pygame
class Skier(pygame.sprite.Sprite):
    def __init__(self):
        super(Skier, self).__init__()
        # define some parameters(from -2 to 2)
        self.direction = 0
        self.imgs = ["./images/skier_forward.png", "./images/skier_right1.png", "./images/skier_right2.png",
                     "./images/skier_left2.png", "./images/skier_left1.png"]
        self.person = pygame.image.load(self.imgs[self.direction])
        self.rect = self.person.get_rect()
        self.rect.center = [320, 100]
        self.speed = [self.direction, 6-abs(self.direction)*2]

    # change direction of skier
    def turn(self, num):
        self.direction += num
        self.direction = max(-2, self.direction)
        self.direction = min(2, self.direction)
        center = self.rect.center
        self.person = pygame.image.load(self.imgs[self.direction])
        self.rect = self.person.get_rect()
        self.rect.center = center
        self.speed = [self.direction, 6-abs(self.direction)*2]
        return self.speed

    # move skier
    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centerx = max(20, self.rect.centerx)
        self.rect.centerx = min(620, self.rect.centerx)
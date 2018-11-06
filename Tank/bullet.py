import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet,self).__init__()
        # load bullet with 4 direction
        self.bullets = ['./images/bullet/bullet_up.png', './images/bullet/bullet_down.png', './images/bullet/bullet_left.png', './images/bullet/bullet_right.png']
        # bullet direction (default up)
        self.direction_x, self.direction_y = 0, -1
        self.bullet = pygame.image.load(self.bullets[0])
        self.rect = self.bullet.get_rect()
        self.rect.left, self.rect.right = 0, 0
        self.speed = 6
        self.alive = False
        self.stronger = False

    def turn(self, direction_x, direction_y):
        self.direction_x, self.direction_y = direction_x, direction_y
        if self.direction_x == 0 and self.direction_y == -1:
            self.bullet = pygame.image.load(self.bullets[0])
        elif self.direction_x == 0 and self.direction_y == 1:
            self.bullet = pygame.image.load(self.bullets[1])
        elif self.direction_x == -1 and self.direction_y == 0:
            self.bullet = pygame.image.load(self.bullets[2])
        elif self.direction_x == 1 and self.direction_y == 0:
            self.bullet = pygame.image.load(self.bullets[3])
        else:
            raise ValueError('Bullet class -> direction value error.')
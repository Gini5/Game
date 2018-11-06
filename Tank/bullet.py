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
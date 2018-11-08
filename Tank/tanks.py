import pygame
from bullet import Bullet

class myTank(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        if player == 1:
            self.tanks = ['./images/myTank/tank_T1_0.png', './images/myTank/tank_T1_1.png',
                          './images/myTank/tank_T1_2.png']
        elif player == 2:
            self.tanks = ['./images/myTank/tank_T2_0.png', './images/myTank/tank_T2_1.png',
                          './images/myTank/tank_T2_2.png']
        else:
            raise ValueError('myTank class -> player value error.')
        # tank level(initial 0)
        self.level = 0
        # load tank
        self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
        self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
        self.rect = self.tank_0.get_rect()
        # protected mask
        self.protected_mask = pygame.image.load('./images/others/protect.png').convert_alpha()
        self.protected_mask1 = self.protected_mask.subsurface((0, 0), (48, 48))
        self.protected_mask2 = self.protected_mask.subsurface((48, 0), (48, 48))
        # tank direction
        self.direction_x, self.direction_y = 0, -1
        # set players position
        if player == 1:
            self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
        elif player == 2:
            self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24
        else:
            raise ValueError('myTank class -> player value error.')
        # speed
        self.speed = 3
        # if alive
        self.alive = True
        # lives
        self.life = 3
        # is protected
        self.protected = False
        # bullet
        self.bullet = Bullet()

        def shoot(self):
            self.bullet.alive = True
            self.bullet.turn(self.direction_x, self.direction_y)
            if self.direction_x == 0 and self.direction_y == -1:
                self.bullet.rect.left = self.rect.left + 20
                self.bullet.rect.bottom = self.rect.top - 1
            elif self.direction_x == 0 and self.direction_y == 1:
                self.bullet.rect.left = self.rect.left + 20
                self.bullet.rect.top = self.rect.bottom + 1
            elif self.direction_x == -1 and self.direction_y == 0:
                self.bullet.rect.right = self.rect.left - 1
                self.bullet.rect.top = self.rect.top + 20
            elif self.direction_x == 1 and self.direction_y == 0:
                self.bullet.rect.left = self.rect.right + 1
                self.bullet.rect.top = self.rect.top + 20
            else:
                raise ValueError('myTank class -> direction value error.')
            if self.level == 0:
                self.bullet.speed = 8
                self.bullet.stronger = False
            elif self.level == 1:
                self.bullet.speed = 12
                self.bullet.stronger = False
            elif self.level == 2:
                self.bullet.speed = 12
                self.bullet.stronger = True
            elif self.level == 3:
                self.bullet.speed = 16
                self.bullet.stronger = True
            else:
                raise ValueError('myTank class -> level value error.')

        def up_level(self):
            if self.level < 3:
                self.level += 1
            try:
                self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
            except:
                self.tank = pygame.imageload(self.tanks[-1]).convert_alpha()

        def down_level(self):
            if self.level > 0:
                self.level -= 1
            self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
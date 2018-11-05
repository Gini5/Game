import pygame

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
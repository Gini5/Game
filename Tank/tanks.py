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
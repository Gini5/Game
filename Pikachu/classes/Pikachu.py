import cocos
import os
class Pikachu(cocos.sprite.Sprite):
    def __init__(self):
        # initialize pikachu instance with its image
        super(Pikachu, self).__init__('pikachu.png')
        self.able_jump = False
        self.speed = 0
        self.image_anchor = 0, 0
        self.position = 80, 280
        self.schedule(self.update)  # call update function for every frame

    # control jump by voice
    def jump(self, h):
        if self.able_jump:
            self.y += 1
            self.speed -= max(min(h, 10), 7)
            self.able_jump = False

    # after landing it stops
    def land(self, y):
        if self.y > y-25:
            self.able_jump = True
            self.speed = 0
            self.y = y

    # means every frame pikachu will go down due to gravity
    def update(self, delta):
        self.speed += delta*10
        self.y -= self.speed
        if self.y < -85:
            # if pikachu fall down, restart the game
            self.reset()

    def reset(self):
        self.parent.reset()
        self.able_jump = False
        self.speed = 0
        self.position = 80, 280
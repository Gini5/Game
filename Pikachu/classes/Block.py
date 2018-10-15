import cocos, random
class Block(cocos.sprite.Sprite):
    def __init__(self, position):
        super(Block, self).__init__('block.png')
        self.image_anchor = 0, 0
        x, y = position
        if x == 0:
            # self.position is (0,0), to right and up scale
            self.scale_x = 4.5      # flat land with length 450 pixels
            self.scale_y = 1        # flat land with height 100 pixels
        else:       # generate block at random
            self.scale_x = 0.5 + random.random()*1.5
            self.scale_y = min(max(y-50+random.random()*100, 50), 300)/100
            self.position = x+50+random.random()*100, 0
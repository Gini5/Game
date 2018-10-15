import cocos, random
class Block(cocos.sprite.Sprite):
    def __init__(self, position):
        super(Block, self).__init__('block.png')
        self.image_anchor = 0, 0
        x, y = position
        if x == 0:
            self.scale_x = 4.5      # flat land with length 4.5
            self.scale_y = 1        # flat land with height 1
        else:       # generate block at random
            self.scale_x = 0.5 + random.random()*1.5
            self.scale_y = min(max(y-50+random.random()*100, 50), 300)/100

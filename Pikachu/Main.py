import os, cocos, struct
from cocos.sprite import Sprite
from classes.Pikachu import Pikachu
from classes.Block import Block

class JumpPikachu(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        #initialize canvas
        super(JumpPikachu, self).__init__(255, 255, 255, 255, 800, 1000)

        self.numSamples = 1000

        #voice control bar
        self.vbar = Sprite('block.png')
        self.vbar.position = 20,450
        self.vbar.scale_y = 0.1     #bar height
        self.vbar.image_anchor = 0,0
        self.add(self.vbar)
        #Pikachu instance
        self.pikachu = Pikachu()
        # self.add(self.pikachu)
        #cocosnode
        self.floor = cocos.cocosnode.CocosNode()
        self.add(self.floor)
        position = 0, 100
        for i in range(1, 3):
            block = Block(position)
            self.floor.add(block)
            position = block.x + block.width, block.height

if __name__ == '__main__':
    cocos.director.director.init(caption="Pikachu")
    cocos.director.director.run(cocos.scene.Scene(JumpPikachu()))

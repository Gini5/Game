import os, cocos,struct
from cocos.sprite import Sprite
from classes.Pikachu import Pikachu
from classes.Block import Block

class JumpPikachu(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        super(JumpPikachu, self).__init__(255, 255, 255, 255, 800, 600)

if __name__ == '__main__':
    cocos.director.director.init(caption="Pikachu")
    cocos.director.director.run(cocos.scene.Scene(JumpPikachu()))

import os, cocos, struct
from cocos.sprite import Sprite
from pyaudio import PyAudio, paInt16
from classes.Pikachu import Pikachu
from classes.Block import Block

class JumpPikachu(cocos.layer.ColorLayer):
    is_event_handler = True
    def __init__(self):
        #initialize canvas
        super(JumpPikachu, self).__init__(255, 255, 255, 255, 800, 1000)
        # frames per buffer
        self.numSamples = 1000

        #voice control bar
        self.vbar = Sprite('block.png')
        self.vbar.position = 20,450
        self.vbar.scale_y = 0.1     #bar height
        self.vbar.image_anchor = 0,0
        self.add(self.vbar)
        #Pikachu instance
        self.pikachu = Pikachu()
        self.add(self.pikachu)

        #cocosnode, draw blocks
        self.floor = cocos.cocosnode.CocosNode()
        self.add(self.floor)
        position = 0, 100
        for i in range(10):
            block = Block(position)
            self.floor.add(block)
            position = block.x + block.width, block.height

        # audio input
        audio = PyAudio()
        SampleRate = int(audio.get_device_info_by_index(0)['defaultSampleRate'])
        self.stream = audio.open(format = paInt16,
                                 channels = 1,
                                 rate = SampleRate,
                                 input = True,
                                 frames_per_buffer = self.numSamples)
        self.schedule(self.update)

    def collide(self):
        # check if pikachu hit the floor
        currentx = self.pikachu.x - self.floor.x
        for b in self.floor.get_children():
            # check which block is pikachu current at
            if b.x <= currentx + self.pikachu.width*0.8 and currentx + self.pikachu.width*0.2<= b.x+b.width:
                if self.pikachu.y < b.height:
                    self.pikachu.land(b.height)
                    break

    def update(self, delta):
        # get audio data of every frame
        audio_data = self.stream.read(self.numSamples)
        k = max(struct.unpack('1000h', audio_data))
        self.vbar.scale_x = k / 10000
        if k > 3000:
            self.floor.x -= min((k/20), 150) * delta
        if k > 8000:
            self.pikachu.jump((k-8000)/1000)
        self.collide()

    def reset(self):
        self.floor.x = 0

if __name__ == '__main__':
    cocos.director.director.init(caption="Pikachu")
    cocos.director.director.run(cocos.scene.Scene(JumpPikachu()))

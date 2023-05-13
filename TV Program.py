class TV:
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self,channel):
        return channel

    def setChannel(self,channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel
   
    def getChannel(self,volume):
        return volume
    
    def setVolume(self,volume):
        if self.on and 1 <= volume <= 7:
            self.volume = volume

    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1
            
    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volumeUp(self,volume):
        if self.on and self.volume < 7:
            self.volume += 1

    def volumeDown(self):
        if self.on and self.volume > 1:
            self.volume -= 1

class TestTv:
    def main(self):
        tv1 = TV()
        tv2 = TV()
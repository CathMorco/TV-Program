class TV:
    #Initializes intances
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False

    #Function that turns on the TV object
    def turnOn(self):
        self.on = True

    #Function that turns off the TV object
    def turnOff(self):
        self.on = False

    #Function that displays/returns the channel on the TV object
    def getChannel(self,channel):
        self.channel = channel
        return channel

    #Function that changes the channel on the TV object
    def setChannel(self,channel):
        try:
            if self.on and 1 <= channel <= 120:
                self.channel = channel

            else:
                raise OverflowError("ERROR: You must only choose between the numbers 1-120")
        except TypeError:
            print("ERROR: Please input an integer")
        except OverflowError as e:
            print(e)

    #Function that displays/returns the volume on the TV object
    def getVolume(self,volume):
        self.volume = volume
        return volume

    #Function that changes the volulme on the TV object  
    def setVolume(self,volume):
        try:
            if self.on and 1 <= volume <= 7:
                self.volume = volume

            else:
                raise OverflowError("ERROR: You must only choose between the numbers 1-7")
        except TypeError:
            print("ERROR: Please input an integer")
        except OverflowError as e:
            print(e)

    #Function that increases the channel on the TV object by 1
    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    #Function that decrease the channel on the TV object by 1
    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    #Function that increases the volume on the TV object by 1
    def volumeUp(self):
        if self.on and self.volume < 7:
            self.volume += 1

    #Function that decreases the volume on the TV object by 1
    def volumeDown(self):
        if self.on and self.volume > 1:
            self.volume -= 1

class TestTv:
    def main(self):
        tv1 = TV()
        tv2 = TV()
from PyQt5.QtWidgets import QComboBox, QLabel, QApplication, QWidget, QVBoxLayout
import sys


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
    def getChannel(self):
        return self.channel

    #Function that changes the channel on the TV object
    def setChannel(self,channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    #Function that displays/returns the volume on the TV object
    def getVolume(self):
        return self.volumeLevel

    #Function that changes the volulme on the TV object  
    def setVolume(self,volume):
        if self.on and 1 <= volume <= 7:
            self.volume = volume

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
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    #Function that decreases the volume on the TV object by 1
    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1

class TestTv:
    def main():
        tv1 = TV()
        tv1.turnOn()
        tv1.setChannel(1000)
        tv1.setVolume(1000)
        print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
        
        tv2 = TV()
        tv2.turnOn()
        tv2.setChannel(3)
        tv2.setVolume(2)
        print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())      

class TVWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tv = TV()
        self.initUI()

    def initUI(self):
        self.channel_label = QLabel(f"Current Channel: {self.tv.getChannel()}")
        self.channel_combo = QComboBox()
        for channel in range(1, 121):
            self.channel_combo.addItem(str(channel))
        self.channel_combo.setCurrentIndex(self.tv.getChannel() - 1)
        self.channel_combo.currentIndexChanged.connect(self.changeChannel)

        vbox = QVBoxLayout()
        vbox.addWidget(self.channel_label)
        vbox.addWidget(self.channel_combo)
        self.setLayout(vbox)

        self.setWindowTitle('TV Widget')
        self.show()

    def changeChannel(self, index):
        self.tv.setChannel(index+1)
        self.channel_label.setText(f"Current Channel: {self.tv.getChannel()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tv_widget = TVWidget()
    sys.exit(app.exec_())
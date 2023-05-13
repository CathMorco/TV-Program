from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        combobox1 = QComboBox()
        combobox1.addItems([str(e) for e in range(1, 121)])
        layout = QVBoxLayout()
        layout.addWidget(combobox1)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def current_text_changed(self, s):
        print("Current text: ", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()


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
        else:
            print ("ERROR: You must only choose between the numbers 1-120")
    #Function that displays/returns the volume on the TV object
    def getVolume(self):
        return self.volumeLevel

    #Function that changes the volulme on the TV object  
    def setVolume(self,volume):
        if self.on and 1 <= volume <= 7:
            self.volume = volume
        else:
            print ("ERROR: You must only choose between the numbers 1-7")

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

TestTv.main()
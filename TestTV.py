from TVProgram import TV

class TestTv:
    def main(Channelnum1,Volumenum1,Channelnum2,Volumenum2):
        tv1 = TV()
        tv1.turnOn()
        tv1.setChannel(Channelnum1)
        tv1.setVolume(Volumenum1)
        print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
        
        tv2 = TV()
        tv2.turnOn()
        tv2.setChannel(Channelnum2)
        tv2.setVolume(Volumenum2)
        print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())      

TestTv.main(30,3,3,2)
from TestProgram import TV

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
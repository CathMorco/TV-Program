#Imports necessary elements
from TVProgram import TV
import sys


class TestTv:
    def main(Channelnum1,Volumenum1,Channelnum2,Volumenum2):
        tv1.turnOn()
        tv1.setChannel(Channelnum1)
        tv1.setVolume(Volumenum1)
        print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
        

        tv2.turnOn()
        tv2.setChannel(Channelnum2)
        tv2.setVolume(Volumenum2)
        print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())

    def channelFunction():
        choice=input("Would you like to adjust the channel number?(Y/N): ")
        choice= choice.lower()
        if choice[0]=="y":
            choice2=input("Would you like to increase or decrease the channel number?(Increase/Decrease): ")
            choice2=choice2.lower()            
            if choice2[0] == "i":
                choice3 = input("Which tv's channel would you like to increase?(1/2): ")
                choice3 = choice3.lower()
                if choice3[0] == "1":
                    tv1.channelUp()
                    print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
                elif choice3[0] == "2":
                    tv2.channelUp()
                    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())
                else:
                    print("Invalid input. Please try again.")
                    TestTv.channelFunction()
            elif choice2[0] == "d":
                choice3 = input("Which tv's channel would you like to decrease?:(1/2)")
                choice3 = choice3.lower()
                if choice3[0] == "1":
                    tv1.channelDown()
                    print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
                elif choice3[0] == "2":
                    tv2.channelDown()
                    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())
                else:
                    print("Invalid input. Please try again.")
                    TestTv.channelFunction()
            else:
                print("Invalid input. Please try again.")
                TestTv.channelFunction()
        elif choice[0] == "n":
            sys.exit()

        choice4=input("Would you like to adjust the volume?(Y/N): ")
        choice4= choice4.lower()
        if choice4[0]=="y":
            choice5=input("Would you like to increase or decrease the volume?(Increase/Decrease): ")
            choice5=choice5.lower()            
            if choice5[0] == "i":
                choice6 = input("Which tv's volume would you like to increase?(1/2): ")
                choice6 = choice6.lower()
                if choice6[0] == "1":
                    tv1.volumeUp()
                    print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
                elif choice6[0] == "2":
                    tv2.volumeUp()
                    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())
                else:
                    print("Invalid input. Please try again.")
                    TestTv.channelFunction()
            elif choice5[0] == "d":
                choice6 = input("Which tv's volume would you like to decrease?:(1/2)")
                choice6 = choice6.lower()
                if choice6[0] == "1":
                    tv1.volumeDown()
                    print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
                elif choice6[0] == "2":
                    tv2.volumeDown()
                    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())
                else:
                    print("Invalid input. Please try again.")
                    TestTv.channelFunction()
            else:
                print("Invalid input. Please try again.")
                TestTv.channelFunction()
        elif choice4[0] == "n":
            sys.exit()
        again = input("Would you like to try again?(Y/N): ")
        again = again.lower()
        if again[0] == "y":
            num1= int(input("From 1-120, what channel would you like for tv1?:"))
            num2= int(input("From 1-7, what volume level would you like for tv1?:"))
            num3= int(input("From 1-120, what channel would you like for tv2?:"))
            num4= int(input("From 1-7, what volume level would you like for tv2?:"))
            TestTv.main(num1,num2,num3,num4)
            TestTv.channelFunction()
        else:
            sys.exit()


tv1 = TV()
tv2 = TV()
num1= int(input("From 1-120, what channel would you like for tv1?:"))
num2= int(input("From 1-7, what volume level would you like for tv1?:"))
num3= int(input("From 1-120, what channel would you like for tv2?:"))
num4= int(input("From 1-7, what volume level would you like for tv2?:"))
TestTv.main(num1,num2,num3,num4)
TestTv.channelFunction()

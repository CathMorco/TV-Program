#Imports necessary elements
from TVProgram import TV
import sys
import pygame


class TestTv:
    def main(Channelnum1,Volumenum1,Channelnum2,Volumenum2):
        tv1.turnOn()
        tv1.setChannel(Channelnum1)
        tv1.setVolume(Volumenum1)
        channel = str(tv1.getChannel())
        volume= str(tv1.getVolume())
        text1 = ("tv1's channel is " + channel + " and volume level is " + volume)
        
        tv2.turnOn()
        tv2.setChannel(Channelnum2)
        tv2.setVolume(Volumenum2)
        channel2 = str(tv2.getChannel())
        volume2= str(tv2.getVolume())
        text2 = ("tv2's channel is " + channel2 + " and volume level is " + volume2)

        text = text1 + text2
        print("Check the window screen :D If you would like to proceed with the program, click the exit button on the window display screen :D")
        TestTv.mainProgram(text)
        TestTv.channelFunction(text1, text2)

    def channelFunction(text1, text2):
        choice=input("Would you like to adjust the channel number?(Y/N): ")
        choice= choice.lower()
        while choice not in ['y', 'n']:
            print("ERROR: You must only choose between Y or N")
            choice = input("Enter your choice: ").lower()
        if choice[0]=="y":
            choice2=input("Would you like to increase or decrease the channel number?(Increase/Decrease): ")
            choice2=choice2.lower()
            while choice2 not in ['i', 'd']:
                print("ERROR: You must only choose between Increase or Decrease")
                choice2 = input("Enter your choice: ").lower()            
            if choice2[0] == "i":
                choice3 = input("Which tv's channel would you like to increase?(1/2): ")
                choice3 = choice3.lower()
                while choice3 not in ["1", "2"]:
                    print("ERROR: You must only choose between 1 or 2")
                    choice3 = input("Enter your choice: ").lower()
                if choice3[0] == "1":
                    tv1.channelUp()
                    channel = str(tv1.getChannel())
                    volume= str(tv1.getVolume())
                    text1 = ("tv1's channel is " + channel + " and volume level is " + volume)
                elif choice3[0] == "2":
                    tv2.channelUp()
                    channel2 = str(tv2.getChannel())
                    volume2= str(tv2.getVolume())
                    text2 = ("tv2's channel is " + channel2 + " and volume level is " + volume2)
            elif choice2[0] == "d":
                choice3 = input("Which tv's channel would you like to decrease?:(1/2)")
                choice3 = choice3.lower()
                while choice3 not in ["1", "2"]:
                    print("ERROR: You must only choose between 1 or 2")
                    choice3 = input("Enter your choice: ").lower()
                if choice3[0] == "1":
                    tv1.channelDown()
                    channel = str(tv1.getChannel())
                    volume= str(tv1.getVolume())
                    text1= ("tv1's channel is " + channel + " and volume level is " + volume)
                elif choice3[0] == "2":
                    tv2.channelDown()
                    channel2 = str(tv2.getChannel())
                    volume2= str(tv2.getVolume())
                    text2 = ("tv2's channel is " + channel2 + " and volume level is " + volume2)
                else:
                    print("Invalid input. Please try again.")
                    TestTv.channelFunction()
        elif choice[0] == "n":
            pass
        else:
            print("Invalid input. Please try again.")
            TestTv.channelFunction(text1, text2)
        choice4=input("Would you like to adjust the volume?(Y/N): ")
        choice4= choice4.lower()
        while choice4 not in ['y', 'n']:
            print("ERROR: You must only choose between Y or N")
            choice4 = input("Enter your choice: ").lower()
        if choice4[0]=="y":
            choice5=input("Would you like to increase or decrease the volume?(Increase/Decrease): ")
            choice5=choice5.lower()
            while choice5 not in ['i', 'd']:
                print("ERROR: You must only choose between Increase or Decrease")
                choice5 = input("Enter your choice: ").lower()            
            if choice5[0] == "i":
                choice6 = input("Which tv's volume would you like to increase?(1/2): ")
                choice6 = choice6.lower()
                while choice6 not in ['1', '2']:
                    print("ERROR: You must only choose between 1 or 2")
                    choice6 = input("Enter your choice: ").lower()
                if choice6[0] == "1":
                    tv1.volumeUp()
                    channel = str(tv1.getChannel())
                    volume= str(tv1.getVolume())
                    text1= ("tv1's channel is " + channel + " and volume level is " + volume)
                elif choice6[0] == "2":
                    tv2.volumeUp()
                    channel2 = str(tv2.getChannel())
                    volume2= str(tv2.getVolume())
                    text2 = ("tv2's channel is " + channel2 + " and volume level is " + volume2)
                else:
                    print("Invalid input. Please try again.")
                    TestTv.channelFunction()
            elif choice5[0] == "d":
                choice6 = input("Which tv's volume would you like to decrease?:(1/2)")
                choice6 = choice6.lower()
                while choice6 not in ['1', '2']:
                    print("ERROR: You must only choose between 1 or 2")
                    choice6 = input("Enter your choice: ").lower()
                if choice6[0] == "1":
                    tv1.volumeDown()
                    channel = str(tv1.getChannel())
                    volume= str(tv1.getVolume())
                    text1= ("tv1's channel is " + channel + " and volume level is " + volume)
                elif choice6[0] == "2":
                    tv2.volumeDown()
                    channel2 = str(tv2.getChannel())
                    volume2= str(tv2.getVolume())
                    text2 = ("tv2's channel is " + channel2 + " and volume level is " + volume2)
                else:
                    print("Invalid input. Please try again.")
                    TestTv.channelFunction(text1, text2)
            else:
                print("Invalid input. Please try again.")
                TestTv.channelFunction(text1, text2)
        elif choice4[0] == "n":
            pass
        else:
            print("Invalid input. Please try again.")
            TestTv.channelFunction(text1, text2)
        text = text1 + text2
        print("Check the window screen :D If you would like to proceed with the program, click the exit button on the window display screen :D")
        TestTv.mainProgram(text)
        again = input("Would you like to try again?(Y/N): ")
        again = again.lower()
        while again not in ['y', 'n']:
            print("ERROR: You must only choose between Y or N")
            again = input("Enter your choice: ").lower()
        if again[0] == "y":
            num1= int(input("From 1-120, what channel would you like for tv1?:"))
            num2= int(input("From 1-7, what volume level would you like for tv1?:"))
            num3= int(input("From 1-120, what channel would you like for tv2?:"))
            num4= int(input("From 1-7, what volume level would you like for tv2?:"))
            TestTv.main(num1,num2,num3,num4)
        else:
            sys.exit()


    #Creates the main program
    def mainProgram(newText):

        #Sets the value for the width and height of the display screen
        W, H = 800, 600

        #Creates the display screen
        display = pygame.Surface ((W, H))
        screen = pygame.display.set_mode ((W, H))
        pygame.display.set_caption("Results")
        clock = pygame.time.Clock()

        #RGB example values
        black = (0,0,0)
        white = (255,255,255)

        #The rate of change in colors
        col_spd = 1

        #The color directory & its values
        col_dir =[[-1,1,1],[-1,1,-1]]
        def_col = [[120,120,240],[140,140,240]]

        #Initialized values for functions
        minimum = 0
        maximum = 255

        #Draws the text
        def draw_text(text, size, col, x, y):
            font = pygame.font.get_default_font()
            font = pygame.font.Font(font, size)
            text_surface = font.render(text, True, col)
            text_rect=text_surface.get_rect()
            text_rect.center = (x,y)
            screen.blit(text_surface, text_rect)

        #Creates the color change
        def col_change(col,dir):
            for i in range(1):
                col[i] += col_spd * dir[i]
                if col[i] >=maximum or col[i] <=minimum:
                    dir[i] *= -1

        #Combines the color change and draw text into one function
        def array_func(col,dir,text,size,x,y):
            for i in range(len(col)):
                draw_text(text[i],size,col[i],x,y + i*50)
                col_change(col[i],dir[i])

        # Initialising pygame
        pygame.init()

        # Split into words
        words = newText.split()

        # Calculate number of words per line
        num_words = len(words)
        words_per_line = num_words // 2

        # Divide into 3 lines
        line1 = " ".join(words[:words_per_line])
        line2 = " ".join(words[words_per_line:])

        #Combines the 3 lines into one list
        texts= [line1,line2]

        #Runs the program
        run=True

        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            array_func(def_col,col_dir,texts,40, W / 2 , 200)

            clock.tick()

            display.blit(screen,(0,0))
            pygame.display.update()


tv1 = TV()
tv2 = TV()

while True:
    try:
        num1= int(input("From 1-120, what channel would you like for tv2?:"))
        if 1 <= num1 <= 120:
            break
        else:
            print("Please enter a valid channel number between 1 and 120.")
    except ValueError:
        print("Please enter a valid integer.")

while True:
    try:
        num2= int(input("From 1-7, what volume level would you like for tv1?:"))
        if 1 <= num2 <= 7:
            break
        else:
            print("Please enter a valid volume level between 1 and 7.")
    except ValueError:
        print("Please enter a valid integer.")

while True:
    try:
        num3= int(input("From 1-120, what channel would you like for tv2?:"))
        if 1 <= num3 <= 120:
            break
        else:
            print("Please enter a valid channel number between 1 and 120.")
    except ValueError:
        print("Please enter a valid integer.")

while True:
    try:
        num4= int(input("From 1-7, what volume level would you like for tv2?:"))
        if 1 <= num4 <= 7:
            break
        else:
            print("Please enter a valid volume level between 1 and 7.")
    except ValueError:
        print("Please enter a valid integer.")

TestTv.main(num1,num2,num3,num4)
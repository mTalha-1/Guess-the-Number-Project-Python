import random
import time
from pygame import mixer
import winsound
def guess_by_user(x,y):
    mixer.music.load("gamemusic-6082.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()
    random_number = random.randint(1,x)
    while True:
        if y==0:
            mixer.music.stop()
            time.sleep(1)
            mixer.music.load("game-over.mp3")
            mixer.music.set_volume(0.5)
            mixer.music.play()
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("OOPs! You lost your all chances")
            print("*********Game is Over!*********")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            time.sleep(4)
            break
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess<random_number:
            print(f"Sorry! The guess number {guess} is too low.")
            print("")
            y-=1
        elif guess>random_number:
            print(f"Sorry! The guess number {guess} is too high.")
            print("")
            y-=1
        else:
            mixer.music.stop()
            time.sleep(1)
            mixer.music.load("game-win-36082.mp3")
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print("")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><>")
            print(f"Yay! Congrats, You guessed the number {random_number} perfectly.")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><>")
            time.sleep(4)
            mixer.music.stop()
            break
def guess_by_computer():
    mixer.music.load("gamemusic-6082.mp3")
    mixer.music.set_volume(0.2)
    mixer.music.play()
    number = int(input("Enter the number you want to guess by computer in range between 1 and 10: "))
    random_num = random.randint(1,10)
    if random_num == number:
        mixer.music.stop()
        time.sleep(1)
        mixer.music.load("game-over.mp3")
        mixer.music.set_volume(0.5)
        mixer.music.play()
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
        print("Yay! I guess the number and you lost the game ")
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
        time.sleep(3)
    elif random_num != number:
        mixer.music.stop()
        time.sleep(1)
        mixer.music.load("game-win-36082.mp3")
        mixer.music.set_volume(0.2)
        mixer.music.play()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Oh no! I fail to guess number and You win")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        time.sleep(3)
mixer.init()
mixer.music.load('game_sound.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("Welcome! The most intresting \"Guess The Number\" Game ")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
time.sleep(2)
while True:
    print("")
    print("There are two type of games. Plz! select one ")
    print("Press 1 for to play Guess by user\nPress 2 for to play Guess by computer")
    type = int(input())
    winsound.Beep(500,1000)
    if type == 1:
        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Please! Select the mode of game")
            print("1)Easy\n2)Medium\n3)Difficult")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            mode = int(input())
            winsound.Beep(500,1000)
            if mode == 1:
                print("The game will start,soon.")
                time.sleep(2)
                print("In easy mode, There are some conditions!\n1)You have to guess number from range 1 to 15\n2)You have only 9 chances to guess the number")
                time.sleep(4)
                print("The game has been start. Go, Play and Enjoy!")
                guess_by_user(15,9)
                break
            elif mode == 2:
                print("The game will start,soon.")
                time.sleep(2)
                print("In Medium mode, There are some conditions!\n1)You have to guess number from range 1 to 20\n2)You have only 6 chances to guess the number")
                time.sleep(4)
                print("The game has been start. Go, Play and Enjoy!")
                guess_by_user(20,6)
                break
            elif mode == 3:
                print("The game will start,soon.")
                time.sleep(2)
                print("In Medium mode, There are some conditions!\n1)You have to guess number from range 1 to 25\n2)You have only 4 chances to guess the number")
                time.sleep(4)
                print("The game has been start. Go, Play and Enjoy!")
                guess_by_user(25,4)
                break
            else:
                print("Invalid option! Plz select valid mood again")
                continue
        break
    elif type == 2:
        print("In this game, Computer  has only one chance to guess number  in range between 1 and 10. ")
        guess_by_computer()
        break
    else:
        print("Invalid type! Plz choose valid option.")
        continue
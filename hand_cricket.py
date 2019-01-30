import random

def game():

    min = 1
    max = 6
    
    play = "yes"
    score = 0

    while play == "yes" or play == "":
        print("")
        print("Throwing the bowl...")
        bat = int(input("Enter the runs: "))
        if bat > 6:
            print("You Cheater!!!")
            break
        else:
            pass
        bowl = random.randint(min, max)
        score = score+bat
        if bat != bowl:
            print("That's a",bat)
            print("The score is",score)
            play = input("Next ball?? ")
        elif score-bat == 0:
            print("Out!!!")
            print("Duck!!!")
        else:
            print("Out!!!")
            print("The final score is:",score-bat)
            break

game()
input()
        

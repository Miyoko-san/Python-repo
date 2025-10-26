''' 
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file 'Hi-score.txt' which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore
whenever the game() function breaks the Hi-score.

'''

import random 


def game():
    print("You are playing the game ...")
    score = random.randint(1,50)            # random.randomint(1,100) : it will choose a random integer in the range of 1 to 100

    # fetch the hi-score
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
        
    print(f"Your score : {score}")
    if(hiscore > score):
        # write this hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    
    return score

game()


# Note : the program does not add the hiscore to the file !!! WHY ??
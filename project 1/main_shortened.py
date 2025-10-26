import random 


computer = random.choice([-1,0,1])
yourstr = input("Enter your choice : ")

youDict = {"s":1 , "w":-1 ,"g":0}
reversedDict = {1:"Snake" , -1:"Water" , 0:"Gun"}

you = youDict[yourstr]

print(f"You chose {reversedDict[you]}\nComputer chose {reversedDict[computer]}")


'''

else:
    if(computer == -1 and you == 1):        computer - you = -2
        print("You won !")  
    elif(computer == -1 and you == 0):      computer - you = -1
        print("You loose !")  
    elif(computer == 0 and you == -1):      computer - you = 1
        print("You won !")  
    elif(computer == 0 and you == 1):       computer - you = -1
        print("You loose !")  
    elif(computer == 1 and you == -1):      computer - you = 2
        print("You won !")  
    elif(computer == 1 and you == 0):       computer - you = 1
        print("You loose !")  
    else:
        print("Something went wrong !")

        the below logic is written on the basis of calculation of computer - you

'''

if(computer == you):
    print("Its a draw")
else:
    if(computer - you == -2 or computer - you == 1):
        print("You won !")
    elif(computer - you == 2 or computer - you == -1):
        print("You lost !")
    else:
        print("Print something went wrong.")  



import random 

# random is a module in pyhton which will choose random values when asked to 
#  to ask : random.choice(Give the choices) 

'''
1 for snake 
-1 for water 
0 for gun

'''

computer = random.choice([-1,0,1])
yourstr = input("Enter your choice : ")

youDict = {"s":1 , "w":-1 ,"g":0}
reversedDict = {1:"Snake" , -1:"Water" , 0:"Gun"}

you = youDict[yourstr]

# till now we have two numbers (variables), computer and you


print(f"You chose {reversedDict[you]}\nComputer chose {reversedDict[computer]}")

# nested if-else :


if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("You won !")  
    elif(computer == -1 and you == 0):
        print("You loose !")  
    elif(computer == 0 and you == -1):
        print("You won !")  
    elif(computer == 0 and you == 1):
        print("You loose !")  
    elif(computer == 1 and you == -1):
        print("You won !")  
    elif(computer == 1 and you == 0):
        print("You loose !")  
    else:
        print("Something went wrong !")


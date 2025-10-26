#Write a program to find whether a given username contains less than 10
# characters or not.

user_name = input("Please enter your user name : ")

if(len(user_name)<10):
    print("Minimum 10 characters are required !")
else:
    print("Welcome", user_name)

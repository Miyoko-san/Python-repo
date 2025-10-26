# Write a program to find the greatest of four numbers entered by the user

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if(a>b and a>c and a>d):
    print("Greatest of the entered number is: ",a)

elif(b>a and b>c and b>d):
    print("Greatest of the entered number is: ",b)

elif(c>a and c>b and c>d):
    print("Greatest of the entered number is: ",c)

else:
    print("Greatest of the entered number is: ",d)




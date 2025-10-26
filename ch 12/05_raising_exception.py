'''
a = int(input("Please enter the first number : "))
b = int(input("Please enter the second number : "))

print(f"The division a/b is {a/b}")

# If entered zero as the scond number => shows 'ZeroDivisionError'

'''


#To overcome this we use :


a = int(input("Please enter the first number : "))
b = int(input("Please enter the second number : "))

if (b==0):
    raise ZeroDivisionError("Hey, our programm is not meant to divide numbers by zero")

else:
    print(f"The division a/b is {a/b}")
    
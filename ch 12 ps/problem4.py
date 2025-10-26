# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.


try:
    a = int(input("Please enter the first number : "))
    b = int(input("Please enter the second number : "))
    print(a/b)

except ZeroDivisionError as z:
    print("Infinite")


    
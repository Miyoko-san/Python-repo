# Write a program to find whether a given number is prime or not.

n = int(input("Please enter the number : "))

for i in range(2,n):
    if(n%i != 0):
        print("The entered number is a prime.")
        break
    else:
        print("The entered number is NOT a prime")
        break


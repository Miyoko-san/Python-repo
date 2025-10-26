# Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter the number : "))

i = 1 
factorial = 1 

for i in range(1,(n+1)):
    factorial *= i   ##
    i += 1

print(factorial)

# alter :

n = int(input("Enter the number : "))
product = 1
for i in range(1,n+1):
    product = product*i
print(f"The factorial of the given number is : {product}")
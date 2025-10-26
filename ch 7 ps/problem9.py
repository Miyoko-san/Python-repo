'''
Write a program to print the following star pattern.
***
* *    for n = 3
*** 
'''

# we will print n stars in first and last line of the pattern 
# in the remaining lines we will print only first and last star.


n = int(input("Please enter number : "))

i = 1

'''

while i == 1 or i == n :
    print(i * "*" , end = "")
    print("")
    i += 1
    while i != n :
        print("*", (n-2) * " ", "*")
        break
'''

for i in range (1, n+1):
    if (i == 1 or i == n):
        print("*" * n , end = "")
    else:
        print("*" , end = "")
        print(" " * (n-2) , end = "")
        print("*", end = "")
    print("")
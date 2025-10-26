'''
Write a program to print the following star pattern:
*
**
*** for n = 3
'''

n = int(input("Please enter number : "))
i = 1
while(i <= n):
    print(i * "*" , end = "")
    print("")
    i += 1

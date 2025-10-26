'''Write a program to print the following star pattern.
  *
 ***
***** for n = 3
'''


# n = 1 
# while(n <= 3):
#     print(n*"*")
#     n += 1
   

n = int(input("Please enter number : "))

for i in range (1, n+1):
    print(" " * (n-i), end = "")  # end = "" is an argument of print command which won't add a space between line
    print("*" * (2*i-1), end = "") ##
    print("")

# to just print an in next line use print("")
# it is different than print("\n") : as it does not add any extra line 
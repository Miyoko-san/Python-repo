# Write a program to find the sum of first n natural numbers using while loop

n = int(input("Please enter the number : "))
if(n<0):
    print("Please enter a natural number !")
else:
    while(n>0):
        print(int(n*(n+1)/2))
        break
    

# if you do not remeber the formula

n = int(input("Please enter the number : "))

i = 1
sum = 0 

while(i<=n):
    sum += i  ##
    i += 1

print(sum)
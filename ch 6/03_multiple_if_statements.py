a = int(input("Please enter your age : "))

# If statement 1
if(a%2 == 0):
    print("Entered number is even.")
# End of if statement 1 

#If statement 2 
if(a>=18):
    print("You are above age of consent")
elif(a<=0):
    print("Please enter a valid age !")
else:
    print("You are below age of consent")
# End of if statement 2

#  Write a program to input name, marks and phone number of a student and format it using the format function like below: “The name of the student is Harry, his marks are 72 and phone number is 99999888” 



a = str(input("Please enter the name : "))
b = int(input("Please enter the marks : "))
c = int(input("Please enter the mobile number : "))

final = "The name of the student is {}, his marks are {} and phone number is {} ".format(a,b,c)

print(final)

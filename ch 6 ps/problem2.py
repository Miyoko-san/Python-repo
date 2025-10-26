# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

a1 = int(input("Enter marks obatined in sunject 1: "))
a2 = int(input("Enter marks obatined in sunject 2: "))
a3 = int(input("Enter marks obatined in sunject 3: "))

s = ((a1 + a2 + a3)/300)*100
print("You scored : ",s,"%")

if(s>40 and a1>= 33 and a2>= 33 and a3 >= 33):
    print("You passed !")
else:
    print("You failed !")

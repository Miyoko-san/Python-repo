# #Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter scored marks : "))

if(100 >= marks > 90):
    print("Excellent")
elif(90 >= marks > 80):
    print("A")
elif(80 >= marks >70):
    print("B")
elif(70 >= marks > 60):
    print("C")
elif(60 >= marks > 50):
    print("D")
else:
    print("F")



#Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

# s1 = input("Enter marks of student 1: ")
# marks.append(s1)
# s2 = input("Enter marks of student 2: ")
# marks.append(s2)
# s3 = input("Enter marks of student 3: ")
# marks.append(s3)
# s4 = input("Enter marks of student 4: ")
# marks.append(s4)
# s5 = input("Enter marks of student 5: ")
# marks.append(s5)
# s6 = input("Enter marks of student 6: ")
# marks.append(s6)

# marks.sort() #this will not sort numerically but alphabtically , since it acts ike a sting
# print(marks)
 
 # to tackle this use int(input())

s1 = int(input("Enter marks of student 1: "))
marks.append(s1)
s2 = int(input("Enter marks of student 2: "))
marks.append(s2)
s3 = int(input("Enter marks of student 3: "))
marks.append(s3)
s4 = int(input("Enter marks of student 4: "))
marks.append(s4)
s5 = int(input("Enter marks of student 5: "))
marks.append(s5)
s6 = int(input("Enter marks of student 6: "))
marks.append(s6)

marks.sort()
print(marks)

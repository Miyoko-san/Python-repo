#  Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input("Please enter the number here : "))

table = [n*i for i in range(1,11)]
print(table)


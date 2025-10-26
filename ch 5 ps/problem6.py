# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter friend's name : ")
language = input("Enter favourite language : ")
d.update({name:language})

name = input("Enter friend's name : ")
language = input("Enter favourite language : ")
d.update({name:language})

name = input("Enter friend's name : ")
language = input("Enter favourite language : ")
d.update({name:language})

name = input("Enter friend's name : ")
language = input("Enter favourite language : ")
d.update({name:language})

print(d)

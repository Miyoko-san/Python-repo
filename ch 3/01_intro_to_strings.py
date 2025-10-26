# string is a data type in python
#sequence of characters enclosed in quotes.

name = 'Miyoko' # Single quote string 
b = "Luffy" #Double quote string
c = '''Zoro''' # Triple quotes string : used for multi line strings

# String is immutable

#Slicing a string : Indexing starts from 0 and -1 (directions)

name_short = name[0:2] # excludes 2nd character (technically the 3rd character)
print(name_short)

character1 = name[1]
print(character1)

print(name[-4: -1])

print(name[:4]) # no first index => 0 
print(name[0:]) # no last index => length
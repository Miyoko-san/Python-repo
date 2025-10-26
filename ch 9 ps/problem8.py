# Write a program to make a copy of a text file “this. txt”

with open("this.txt") as f:
    content = f.read()

with open("copy.txt","w") as f:     # will create a "copy.txt" file if not already present
    f.write(content)      

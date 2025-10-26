# readlines : read all the lines of a file and returns them in a list

f = open("file.txt")

lines = f.readlines()
print(lines, type(lines))


# readline() : reads single line at once and return in string form 

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5, type(line5))

# the above can also be written in loop as : 

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()


f.close()

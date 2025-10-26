# Arithmaethic operators + - * /
a = 1 
b = 6
c = a + b # here a and b are operands + is the operator and c is the result

print(c)

# Assignment operators 
a = 4-2 # assign 4-2 in a
print(a)
b=6 
# b += 3 #Increment the value of b by 3 and then assign it to b 
# print(b)
#  So now b = 6+3 i.e. 9

# b -= 3 #Decrement the value of b by 3 and then assign it to b 
# print(b)

b *= 3
print(b)


# comparision operators < ,>, ==, <=, >= and != (not equal to)
# they always return boolean values

d = 5>=4
print(d) #this yields true


# logical operators or and not

e = True or False #for 'or' logic operator either or both shpuld be true to 
# return true otherwise false

print(e)

# Truth table of logical operator OR: similar to logic gates in semiconductors
print("True or False is" , True or False)
print("True or True is" , True or True)
print("False or True is" , False or True)
print("False or False is" , False or False)


f = True and False #For and operator to yield True both should be true otherwise will yield False 

print(f)


# Truth table of logical operator AND: similar to logic gates in semiconductors
print("True and False is" , True and False)
print("True and True is" , True and True)
print("False and True is" , False and True)
print("False and False is" , False and False)

print(not(True)) # not logic operators works on single boolean varible and yield its opposite value

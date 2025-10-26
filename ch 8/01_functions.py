# fn is a group of statements performing a specific task 

'''
a = int(input("Enter the number : ))
b = int(input("Enter the number : ))
c = int(input("Enter the number : ))
print(a + b + c)/3

'''

# if we have to do this for 50 sets of defferent values ! 

# def fn_name():
    # fn logic / syntax of fn


# fn definition : 
def avg():
    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))
    c = int(input("Enter the number : "))
    average = (a + b + c)/3
    print(average)


# to run this fn :  fn call
avg()
avg()
avg()


# write a program to greet user with good day using fns 

def greet():
    name = input("Please eneter your name : ")
    print(f"Good Day {name} !") 

greet()

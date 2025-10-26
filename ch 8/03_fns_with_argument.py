# arguments are parametes or variables in a fn on which fns can work

def greet(name):  # here name is argument in fn greet()
    print(f"Good Day, " + name ) 

greet("Miyoko")  # Miyoko goes inside name varible in greet()
greet("Luffy")



# # we can also have multiple arguments in a single fn 
def greet(name, ending):  # here name and ending are two different arguments in fn greet()
    print(f"Good Day, " + name ) 
    print(ending)

greet("Miyoko", "Thank You")
greet("Luffy", "Thank You")
greet("Nami", "Thanks")  ##


# return value of the fn 

def greet(name, ending):  # here name and ending are two different arguments in fn greet()
    print(f"Good Day, " + name ) 
    print(ending)

a = greet("Miyoko", "Thank You")
print(a)  # prints None => by default there is no return value of a fn


# to get some return value of the fn use return 

def greet(name, ending):  # here name and ending are two different arguments in fn greet()
    print(f"Good Day, " + name ) 
    print(ending)
    return "Done"   # return value of the fn is Done

a = greet("Miyoko", "Thank You")
print(a) # prints Done
'''
# a = 80      # global varibale  : can be used anywhere in the code


# def fun():
#     a = 3   # local variable
#     print(a)


# print(a)    # => output : 80
# fun()       # => output : 3

'''


a = 80     

def fun():
    global a
    a = 3   # this will change the global variable 'a'
    print(a)


fun()       # => output : 3
print(a)    # => output : 3 


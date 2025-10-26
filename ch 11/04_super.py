# SYNTAX : for super method

'''
class Super_Class:
    fn1():       # we want this fn to be called in the child class as well
        code

class Child_Class(Super_Class):
    super().Name_of_fn_to_be_called_from_Super_class(arguments)
    fn2():
        code 
'''


class Employee:
    def __init__(self):
        print("Constructor of Emoloyee class")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer class")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager class")
    c = 3


# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a , o.b)

o = Manager()
print(o.a , o.b , o.c)



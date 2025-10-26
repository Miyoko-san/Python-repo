class Employee:
    a = 1

class Programmer(Employee):   # child class 1
    b = 2

class Manager(Programmer):   # child class 2
    c = 3


o = Employee()
m = Programmer()
n = Manager()

print(o.a)

print(m.a)
print(m.b)

print(n.a)
print(n.b)
print(n.c)
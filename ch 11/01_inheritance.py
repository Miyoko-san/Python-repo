#  Single Inhertiance 

class Employee:   # Base/Parent Class
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")



'''
class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
        print(f"The name of the employee is {self.name} and he/she is good with {self.langage} language")


a = Employee()
b = Programmer()

print(a.company , b.company)


'''

# An efficient way to do this is : 

# Inherited/Derived/Child Class:

class Programmer(Employee):   # Inheritance : will take everything from class Employee and can also take methods n attributes of its own in it.
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name of the employee is {self.name} and he/she is good with {self.langage} language")

a = Employee()
b = Programmer()

print(a.company , b.company)

# if we change anything in class Employee every inherited class will automatically gets modified.
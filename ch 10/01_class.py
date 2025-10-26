# a class is blueprint to create an object
# class contains valid information to create an object

class Employee:
    language = "Python"   # lang and salary are class attributes of the class E
    salary = 1200000

# in the below line of code, miyoko is object 
miyoko = Employee()     # object is instantiation of class
print(miyoko.salary , miyoko.language)

luffy = Employee()
luffy.name = "Monkey D. Luffy"  # instance attribute : specific to object
print(luffy.name , luffy.salary)
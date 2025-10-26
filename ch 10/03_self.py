'''
class Employee:
    language = "Python"   
    salary = 1200000

    def getInfo():
        print(f"The language is {language} and salary is {salary}")


miyoko = Employee()
miyoko.language = "Java Script"

miyoko.getInfo()

# Error : Employee.getInfo() takes 0 positional arguments but 1 was given

this is because the line 12 is read as :

Employee.getInfo("miyoko")

'''

# to counter this we use slef-parameter 


class Employee:
    language = "Python"   
    salary = 1200000

    def getInfo(self):   # instead of self we can use any other name as well but its the general case
        print(f"The language is {self.language} and salary is {self.salary}")
    @staticmethod    # when u dont want to pass the obj to a fn 
    def greet():
        print("Hello")


miyoko = Employee()
miyoko.language = "Java Script"

miyoko.getInfo()
miyoko.greet()

Employee.getInfo(miyoko)

# 37 and 39 is the exact same 
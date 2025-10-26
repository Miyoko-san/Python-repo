# Create a class ‘Employee’ and add salary and increment properties to it

#Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.


# Attempt 1 :

'''
class Employee:
    company = "Microsoft"
    salary = 30000
    increment = 5

    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    @property
    def salaryAfterIncrement(self):
        print(f"As {self.name} has worked outstandingly at {self.company} at the salary of {self.salary}. We are happy to announce an increment !")


    @salaryAfterIncrement.setter
    def new_salary(self , appreciation):
        appreciation = (self.salary * 0.05) + self.salary
        return appreciation

e = Employee()
e.name = "Miyoko"

print(Employee(e))

'''
# code doesnt work


# Attempt 2:

class Employee:
    salary = 234
    increment = 20 

    @property
    def salaryAfterIncrement(self):
        return ( + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self , salary):
        self.increment = ((salary/self.salary) - 1)*100 

    

e = Employee()
print(e.salaryAfterIncrement)

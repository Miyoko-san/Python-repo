# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,number):
        self.number = number
        
    def calc(self):
        print(f"The entered number is {self.number} \nThe square of the numebe is {self.number**2} \nThe cube of the number is {self.number**3} \nThe square root of the number is {self.number**(1/2)}")
    @staticmethod
    def greet():
        print("Hello User.")

number = Calculator(4)
number.greet()
number.calc()
# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self,number):
        self.number = number
        print("I am calculating ...")

    def calc(self):
        print(f"The entered number is {self.number} \nThe square of the numebe is {self.number**2} \nThe cube of the number is {self.number**3} \nThe square root of the number is {self.number**(1/2)}")

number = Calculator(4)
number.calc()


# ALTERNATE : 


class Calculator:
    def __init__(self):
        print("I am calculating ...")

    def calc(self):
        print(f"The entered number is {self} \nThe square of the numebe is {self**2} \nThe cube of the number is {self**3} \nThe square root of the number is {self**(1/2)}")

Calculator.calc(1)

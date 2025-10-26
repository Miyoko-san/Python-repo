#  Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.


class Complex:
    def __init__(self , r , i):
        self.r = r
        self.i = i

    def __add__(self , c2):
        return Complex(self.r + c2.r , self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    


n = Complex(1,2)
m = Complex(3,4)

print(n+m)

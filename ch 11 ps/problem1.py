# Create a class (2-D vector) and use it to create another class representing a 3-D vector. 

'''
class vector1:
    i = 4
    j = 9

class vector2(vector1):
    k = 8

print(vector2.i , vector2.j , vector2.k)
'''

# Better way to do this :

class TwoDVector:
    def __init__(self , i , j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self , i , j , k):
        super().__init__(i , j)
        self.k = k
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


a = TwoDVector(2,3)
a.show()
b = ThreeDVector(2,3,4)
b.show()

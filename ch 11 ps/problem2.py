# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.


class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    
    @staticmethod    # since we do not want to use self here
    def bark():
        print("Bow Bow !")



d = Dog()
d.bark()

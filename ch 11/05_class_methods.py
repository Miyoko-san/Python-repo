'''
class Employee:
    a = 1
    def show(self):
        print(f"The class attribute of a is {self.a}")


e = Employee()
e.a = 45 

e.show()            # this will give '45' but we want the class attribute not the instance attribute

'''
# class decorator: @classmethod


class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


e = Employee()
e.a = 45 

e.show()
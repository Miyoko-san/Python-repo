class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):         # it is a fn but with the help of @property we made it a property (attribute) of the class
        return f"{self.fname} {self.lname}"
    
    @name.setter                # name_of_the_fn/property_defined_in_@property.setter
    def name (self , value):
        self.fname = value.split(" ")[0]   ##
        self.lname = value.split(" ")[1]   ##



e = Employee()
e.a = 45 

e.name = "Miyoko Sharma"
print(e.fname)
print(e.lname)


# string.split("") :  this will split the given string into parts whenever the character in betweeen the double quotes appear in the string and will return them in a list.

'''
e.g. :
string = "Miyoko Sharma"
string1 = string.split(" ")[0] # space  # first element of the list => Returns : Miyoko 
string2 = string.split(" ")[1] => Returns : Sharma 

final result : 
    ["Miyoko" , "Sharma"]

'''
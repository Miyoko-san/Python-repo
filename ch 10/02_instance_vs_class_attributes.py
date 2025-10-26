# Note: Instance attributes, take preference over class attributes during assignment & retrieval.

class Employee:
    language = "Python"   
    salary = 1200000


miyoko = Employee()
miyoko.name = "Miyoko"
miyoko.language = "Java Script"  ##
print(miyoko.salary , miyoko.language , miyoko.name)
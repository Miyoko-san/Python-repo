class Employee:
    language = "Python"   
    salary = 1200000

    def __init__(self , name , salary , language): # Dunder method which is automatically called
        self.name = name    # cretes instantse attributes
        self.salary = salary
        self.language = language
        print("I am creating an object.")

    def getInfo(self):  
        print(f"The language is {self.language} and salary is {self.salary}")



miyoko = Employee("Miyoko", 1300000 , "Java Script")

print(miyoko.name,miyoko.salary,miyoko.language)
# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer():
    company = "Microsoft"

    def __init__(self, name , language , salary):
        self.name = name
        self.language = language 
        self.salary = salary
        print("I am creating an object ...")

    def getInfo(self):
        print(f"{self.name} is an employee at {self.company} for {self.language} at a salary of {self.salary}")


miyoko = Programmer("Miyoko","Python","80k")
luffy = Programmer("Luffy","C","50k")
zoro = Programmer("Zoro","Python","80k")

Programmer.getInfo(miyoko)
Programmer.getInfo(luffy)
Programmer.getInfo(zoro)
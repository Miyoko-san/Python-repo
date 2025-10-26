class Employee:
    company = "ITC"
    name = "Miyoko"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")


class Coder:
    language = "Python"
    def printLanguages(self):
         print(f"Out of all the languages here is your language : {self.language}")


class Programmer(Employee , Coder):
    company = "Itc Infotech"
    def shouLanguage(self):
        print(f"he name of the employee is {self.name} and he/she is good with {self.language} language.")


a = Employee()
b =Programmer()

b.show()            # method of class Employee
b.printLanguages()          # method of class Coder
b.shouLanguage()            # method of class Programmer


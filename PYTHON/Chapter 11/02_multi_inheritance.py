class Employee():
    company = "TCS"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    name = "Jojo"
    def printLanguage(self):
        print(f"Out of the all language here is your language : {self.language}")
              


class Programmer(Employee, Coder):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")



a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()

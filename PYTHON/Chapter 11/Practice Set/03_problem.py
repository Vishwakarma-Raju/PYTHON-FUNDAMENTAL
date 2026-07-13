class Employee:
    salary = 50000
    increment = 20

    @property
    def SalaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @SalaryAfterIncrement.setter
    def SalaryAfterIcrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100

a = Employee()
print(a.SalaryAfterIncrement)
a.SalaryAfterIcrement = 60000
print(a.increment)


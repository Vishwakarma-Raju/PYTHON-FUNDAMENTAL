class Employee:
    language = "Java" # This is Class Attributes
    salary = 2000000

    def getInfo(self):
        print(f"This is language {self.language}. This is salaary {self.salary}.")


    @staticmethod        # yaha par self argument ki need nhi hoti hai hum ise without object ke run kar sakte hai 
    def greet():
        print("Good Morning")


raju = Employee()
# raju.name = "Raju Don" # This is Instance Attributes
print (raju.language, raju.salary)

# raju.getInfo()   # Here raju.getInfo is automatically convert into Employee.getInfo(raju)

Employee.getInfo(raju)
Employee.greet()
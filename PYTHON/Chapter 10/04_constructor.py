class Employee:
    language = "Java" # This is Class Attributes
    salary = 2000000

    def __init__(self , name , salary ,language):
        self.name = name 
        self.salary = salary
        self.language = language
        print("I am creating a object") # This is a dunder method which is called a function automatically

    def getInfo(self):
        print(f"This is language {self.language}. This is salaary {self.salary}.")


    @staticmethod        # yaha par self argument ki need nhi hoti hai hum ise without object ke run kar sakte hai 
    def greet():
        print("Good Morning")


raju = Employee("Jojo", 1500000 , "Python")
# raju.name = "Raju Don" # This is Instance Attributes
print (raju.name, raju.salary, raju.language)

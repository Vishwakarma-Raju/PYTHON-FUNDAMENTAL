class Employee:
    def __init__(self):
        print("Constructor of the Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of the Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of the Manager")
    c = 3

# o = Employee()
# print(o.a) # print the a attribute
# # print(o.b) # show an error as there is no b attribute in Employee class 

# o = Programmer()
# print( o.a,o.b)

o = Manager()
print( o.a , o.b ,o.c)
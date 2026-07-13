class Employee:
    a = 1 

    @classmethod
    def show(cls):
        print(f"The Class Attribute of a is {cls.a}")

e = Employee()
e.a = 69

e.show()
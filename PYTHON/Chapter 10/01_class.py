class Employee:
    language = "Java" # This is Class Attributes
    salary = 2000000

raju = Employee()
raju.name = "Raju Don" # This is Instance Attributes
print (raju.name, raju.language, raju.salary)

jojo = Employee()
jojo.name = "Jojo Jonh Jini"
print (jojo.name, jojo.language, jojo.salary)   

# Here Name is Object Attribute , Salary and Language are Class Attribute as they directly belong to the class
class demo :
    a = 69

o = demo()
print(o.a) # print the class attributes becoz instance attribute is not present
o.a = 0 # instance attribute is set 
print(o.a) # print the instance attribute becoz instance attribute is present

print(demo.a) # print the class attribute
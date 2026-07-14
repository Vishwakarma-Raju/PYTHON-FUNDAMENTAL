a = int(input("Enter No.1: "))
b = int(input("Enter No.2: "))

if ( b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide number by zero")
else:
    print(f"The division of a/b is {a/b}")
# x = int(input("Enter the No.1 : "))
# y = int(input("Enter the No.2 : "))
                                                #Type 1
# if (y == 0):
#     raise ZeroDivisionError("Infinite")
# else:
#     print(f"The division of x/y is {x/y}")

try:
    x = int(input("Enter the No.1 : "))
    y = int(input("Enter the No.2 : "))
    print(x/y)
                                                #Type 2
except ZeroDivisionError as e:
    print("Infinite")
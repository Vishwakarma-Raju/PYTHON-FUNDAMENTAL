num1 = int(input("Enter No.1: "))
num2 = int(input("Enter No.2: "))
num3 = int(input("Enter No.3: "))
num4 = int(input("Enter No.4: "))

if(num1>num2 and num1>num3 and num1>num4):
    print("Num1 is Greater")
elif(num2>num3 and num2>num4 and num2>num1):
    print("Num2 is Greater")
elif(num3>num4 and num3>num2 and num3>num1):
    print("Num3 is Greater")
else:
    print("Num4 is Greater")

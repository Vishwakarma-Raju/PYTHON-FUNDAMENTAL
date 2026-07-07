def GreatestNum():
    a = int(input("Enter the no.1: "))
    b = int(input("Enter the no.2: "))
    c = int(input("Enter the no.3: "))

    if(a>b and a>c):
        print("Number 1 is Greater")
    elif(b>a and b>c):
        print("Number 2 is Greater")
    else:
        print("Number 3 is Greater")
GreatestNum()
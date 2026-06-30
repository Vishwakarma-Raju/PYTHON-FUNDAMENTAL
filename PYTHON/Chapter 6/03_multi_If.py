a = int(input("Enter your age: "))

# start of If statement No.1 

if(a%2==0):
    print("a is even")
# End of If statement No.1

# start of If statement No.2 

if(a>=18):
    print("You are above the age of consent ")
    print("Good for you")
elif(a<0):
    print("You are entered negative age which is next to impossible")    
elif(a==0):
    print("You are entered 0 age which is impossible")    
else:
    print("You are below the age of consent")

# End of If statement No.2

print("End of program")
a = int(input("Enter your age: "))

    # if elif else ladder

if(a>=18):
    print("You are above the age of consent ")
    print("Good for you")
elif(a<0):
    print("You are entered negative age which is next to impossible")    
elif(a==0):
    print("You are entered 0 age which is impossible")    
else:
    print("You are below the age of consent")

print("End of program")
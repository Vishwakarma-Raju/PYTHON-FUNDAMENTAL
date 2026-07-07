s1 = int(input("Enter Maths Mark: "))
s2 = int(input("Enter Physics Mark: "))
s3 = int(input("Enter Chemistry Mark: "))

avg = ((s1+s2+s3)/300)*100
print("Percentage is: ",avg)

if(avg<=100):
    print("You are Passed with A+ Grade")
elif(avg>=80):
    print("You are Passed with A Grade")
elif(avg>=60):
    print("You are Passed with B Grade")
elif(avg>=40):
    print("You are Passed with C Grade")
elif(avg>=33):
    print("You are Passed with D Grade")
else:
    print("You are Failed")
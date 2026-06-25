sci = int(input("Enter Science Marks:"))
maths = int(input("Enter Maths Marks:"))
hindi = int(input("Enter Hindi Marks:"))
gk = int(input("Enter GK Marks:"))

T = ((sci+maths+hindi+gk)/400)*100

if T >= 80 and T < 100:
    print("Grade A")

elif T >= 60 and T < 80:
    print("Grade B")

elif T >= 40 and T <60:
     print("Grade C")

else:
    print("Grade D")

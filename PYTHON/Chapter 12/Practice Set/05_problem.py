n = int(input("Enter the no. : "))

table = [ n*i for i in range(1,11)]
with open("Table.txt", "a") as f:
    f.write(f"The Table of {n} : {str(table)} \n")
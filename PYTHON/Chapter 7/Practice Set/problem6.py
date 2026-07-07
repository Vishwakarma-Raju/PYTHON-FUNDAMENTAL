n = int(input("Enter the No.: "))
product = 1
for i in range(1,n+1):
    product *= i

print(f"Factorial of {n} is {product}")

# def pattern(n):
#     for i in range(0,n):
#         print("*"*(n-i))

# n = int(input("Enter the no.: "))
# pattern(n)

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(5) 
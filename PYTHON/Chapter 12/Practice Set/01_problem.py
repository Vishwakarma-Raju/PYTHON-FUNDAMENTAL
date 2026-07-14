try:
    with open("f1.txt") as f1:
        print(f1.read())

except Exception as e:
    print(e)

try:
    with open("f2.txt") as f2:
        print(f2.read())

except Exception as e:
    print(e)

try:
    with open("f3.txt") as f3:
        print(f3.read())

except Exception as e:
    print(e)

print("Thank You")
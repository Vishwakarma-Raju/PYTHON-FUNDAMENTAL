import os

path = "/"

contents = os.listdir(path)

print("Directory Contents:")
for item in contents:
    print(item)
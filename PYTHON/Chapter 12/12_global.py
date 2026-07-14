a = 69 # this is a global value

def local():
    # global a  # yaha par ye global a ki value 67 ho jayegi
    a = 67   # this is local value for function
    print(a)


local()
print(a)
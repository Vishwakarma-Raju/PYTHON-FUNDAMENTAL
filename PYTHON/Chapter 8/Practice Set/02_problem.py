def fahTocel(f):
    return 5*(f-32)/9

f = int(input("Enter temparature in fahrenheit : "))
print(f"{round(fahTocel(f),2)} ° C ")

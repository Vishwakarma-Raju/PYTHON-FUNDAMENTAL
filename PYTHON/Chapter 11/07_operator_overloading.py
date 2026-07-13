class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(6)
m = Number(9)

print(n+m)
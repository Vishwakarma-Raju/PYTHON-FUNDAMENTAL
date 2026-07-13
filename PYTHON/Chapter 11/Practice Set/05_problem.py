class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    # Vector Addition
    def __add__(self, other):
        return Vector(
            self.i + other.i,
            self.j + other.j,
            self.k + other.k
        )

    # Dot Product
    def __mul__(self, other):
        return self.i * other.i + self.j * other.j + self.k * other.k

    # String Representation
    def __str__(self):
        return f"Vector({self.i}i + {self.j}j + {self.k}k)"



v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v3 = Vector(7,8,9)
 
print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)
class Vector:
    x = 0
    y = 0

    def __add__(self, other):  # +
        new_v = Vector()
        new_v.x = self.x + other.x
        new_v.y = self.y + other.y
        return new_v

    def __mul__(self, num: int):  # *
        new_v = Vector()
        new_v.x = self.x
        new_v.y = self.y
        new_v.x *= num
        new_v.y *= num
        return new_v

    def __ge__(self, other):  # >=
        return (self.x ** 2 + self.y ** 2) ** 0.5 >= (other.x ** 2 + other.y ** 2) ** 0.5

    def __str__(self):  # str
        return f"({self.x}; {self.y})"


v1 = Vector()
v1.x = 2
v1.y = -4


v2 = Vector()
v2.x = -2
v2.y = -1


v3 = v1 * 2

print(v3.x, v3.y)

print(v1 >= v2)

print(v1)
print(v2)
print(v3)

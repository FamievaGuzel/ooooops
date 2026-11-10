class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


# Ваш код

triangle = Triangle(3, 4, 5)
equilateral = EquilateralTriangle(5)
print(triangle.perimeter(), equilateral.perimeter())
print(isinstance(equilateral, Triangle))     
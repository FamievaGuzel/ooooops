class Shape:
    pass

class Polygon(Shape):
    pass

class Triangle(Polygon):
    pass

class IsoscelesTriangle(Triangle):
    pass

class EquilateralTriangle(IsoscelesTriangle):
    pass

class Quadrilateral(Polygon):
    pass

class Parallelogram(Quadrilateral):
    pass

class Rectangle(Parallelogram):
    pass

class Square(Rectangle):
    pass

# Ваш код

print(issubclass(Polygon, Shape), issubclass(Triangle, Polygon),
      issubclass(IsoscelesTriangle, Triangle), issubclass(EquilateralTriangle, IsoscelesTriangle))
print(issubclass(Quadrilateral, Polygon), issubclass(Parallelogram, Quadrilateral),
      issubclass(Rectangle, Parallelogram), issubclass(Square, Rectangle))
print(issubclass(Square, Shape), issubclass(EquilateralTriangle, Polygon))
print(issubclass(Square, Triangle), issubclass(Triangle, Quadrilateral), issubclass(Shape, Polygon))

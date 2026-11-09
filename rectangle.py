class BoundingRectangle:
    def __init__(self):
        self.xs = []
        self.ys = []

    def add_point(self, x, y):
        self.xs.append(x)
        self.ys.append(y)

    def left_x(self):
        return min(self.xs)

    def right_x(self):
        return max(self.xs)

    def bottom_y(self):
        return min(self.ys)

    def top_y(self):
        return max(self.ys)

    def width(self):
        return self.right_x() - self.left_x()

    def height(self):
        return self.top_y() - self.bottom_y()
    
# Ваш код

rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())



rect = BoundingRectangle()
rect.add_point(10, 20)
rect.add_point(5, 7)
rect.add_point(6, 3)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())

# Ваш код

rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())


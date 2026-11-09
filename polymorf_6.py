class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    def intersection(self, other):

        x1, y1 = self.x, self.y
        x2, y2 = x1 + self.w, y1 + self.h
        

        ox1, oy1 = other.x, other.y
        ox2, oy2 = ox1 + other.w, oy1 + other.h
        
        left = max(x1, ox1)
        bottom = max(y1, oy1)
        right = min(x2, ox2)
        top = min(y2, oy2)
        
    
        new_w = right - left
        new_h = top - bottom
        
        if new_w > 0 and new_h > 0:
            return Rectangle(left, bottom, new_w, new_h)
        else:
            return None
        
# Ваш код

rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(5, 5, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())


# Ваш код

rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(10, 0, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())


# Ваш код

rect1 = Rectangle(3, 5, 2, 1)
rect2 = Rectangle(1, 2, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())



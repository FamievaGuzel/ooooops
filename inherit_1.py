class BaseObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return [self.x, self.y, self.z]


class Block(BaseObject):
    def shatter(self):
        self.x = None
        self.y = None
        self.z = None


class Entity(BaseObject):
    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Thing(BaseObject):
    pass


block = Block(10, 20, 30)
print(block.get_coordinates()) 
block.shatter()
print(block.get_coordinates())

ent = Entity(1, 2, 3)
ent.move(4, 5, 6)
print(ent.get_coordinates())
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

# Ваш код

block = Block(1, 2, 3)
entity = Entity(4, 5, 6)
thing = Thing(7, 8, 9)
print(block.get_coordinates())
block.shatter()
print(block.get_coordinates())
entity.move(10, 11, 12)
print(entity.get_coordinates())
print(thing.get_coordinates())
print(issubclass(Block, BaseObject), issubclass(Entity, BaseObject), issubclass(Thing, BaseObject))



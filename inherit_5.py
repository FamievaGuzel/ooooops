class Animal:
    def breathe(self):
        pass

    def eat(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Bird(Animal):
    def lay_eggs(self):
        pass


class FlyingBird(Bird):
    def fly(self):
        pass

# Ваш код

print(issubclass(Fish, Animal), issubclass(Bird, Animal), issubclass(FlyingBird, Bird))
print(hasattr(Fish, 'breathe'), hasattr(Fish, 'swim'), hasattr(Fish, 'lay_eggs'))
print(hasattr(Bird, 'eat'), hasattr(Bird, 'lay_eggs'), hasattr(Bird, 'fly'))
print(hasattr(FlyingBird, 'lay_eggs'), hasattr(FlyingBird, 'fly'), hasattr(FlyingBird, 'swim'))


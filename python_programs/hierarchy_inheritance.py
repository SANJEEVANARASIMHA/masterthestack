class Animal:

    def __init__(self, name):
        self.name = name

    def shout(self):
        return f"sounds"


# derived class1
class Dog(Animal):

    def shout(self):
        return f"{self.name} says bow bow"


class Cat(Animal):
    def shout(self):
        return f"{self.name} says meow meow"


dog = Dog("Shizu")
print(dog.shout())
cat = Cat("Kitty")
print(cat.shout())

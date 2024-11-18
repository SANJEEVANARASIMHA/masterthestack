# Base class 1
class Flyer:

    def __init__(self, height):
        self.height = height

    def fly(self):
        print(f"This creature can fly for height.{self.height}")


# Base class 2
class Swimmer:

    def __init__(self, distance):
        self.distance = distance

    def swim(self):
        print(f"This creature can swim for distance {self.distance}.")


# Derived class
class Duck(Flyer, Swimmer):

    def __init__(self, height, distance):
        Flyer.__init__(self, height)
        Swimmer.__init__(self, distance)

    def quack(self):
        print("The duck quacks.")


# Example usage
duck = Duck("120 cm", "200 cm")
duck.fly()  # From Flyer
duck.swim()  # From Swimmer
duck.quack()  # Specific to Duck



duck1 = Duck("100 cm", "150 cm")
duck1.fly()  # From Flyer
duck1.swim()  # From Swimmer
duck1.quack()  # Specific to Duck

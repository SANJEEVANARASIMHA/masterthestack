# Base class

"""
Definition:
    Hierarchical inheritance occurs when multiple derived classes inherit from a single base class.
    This type of inheritance allows the base class to define common properties and methods that are shared among all the derived classes,
    while each derived class can also have its unique functionality.

Key Characteristics:
    Single Parent, Multiple Children: One base class acts as the parent for multiple derived classes.
    Code Reusability: The derived classes reuse common functionalities of the base class.
    Customization: Each derived class can have its own specific behavior in addition to inheriting from the base class.
"""


class Animal:
    def eat(self):
        print("This animal eats food.")


# Derived class 1
class Dog(Animal):
    def bark(self):
        print("The dog barks.")


# Derived class 2
class Cat(Animal):
    def meow(self):
        print("The cat meows.")


# Derived class 3
class Rabbit(Animal):
    def hop(self):
        print("The rabbit hops.")


# Example usage
dog = Dog()
dog.eat()  # Inherited from Animal
dog.bark()  # Unique to Dog

cat = Cat()
cat.eat()  # Inherited from Animal
cat.meow()  # Unique to Cat

rabbit = Rabbit()
rabbit.eat()  # Inherited from Animal
rabbit.hop()  # Unique to Rabbit

# Base class
class Animal:
    def eat(self):
        print("This animal eats food.")


# Derived class
class Dog(Animal):
    def bark(self):
        print("The dog barks.")


# Example usage
dog = Dog()
dog.eat()  # Inherited from Animal
dog.bark()  # Specific to Dog

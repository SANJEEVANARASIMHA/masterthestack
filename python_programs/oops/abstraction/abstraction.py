"""
In Python, abstraction is a concept from object-oriented programming (OOP) that allows you to hide unnecessary details
and show only the essential features of an object or a class.
This makes code more modular, reusable, and easier to understand.
By focusing only on the core functionality and hiding complex logic, abstraction makes it simpler for users to interact
with a class without needing to understand its internal workings.

How Abstraction Works:
    Abstraction in Python is typically implemented using:
        Abstract Classes: Classes that serve as a blueprint for other classes.
        Abstract Methods: Methods that have no implementation in the base (abstract) class and must be implemented in
                        derived classes.
        Implementing Abstraction in Python: Python provides the abc (Abstract Base Class) module to implement abstraction.
                                            This module lets you create abstract classes and methods,
                                            which cannot be instantiated and must be inherited by subclasses to provide
                                            concrete implementations.

Key Points:
        Abstract Class: A class that contains one or more abstract methods and cannot be instantiated directly.
        Abstract Method: A method that is declared but contains no implementation.
        Subclasses of an abstract class must implement all abstract methods.

Benefits of Abstraction
        Encapsulation of Complexity: Abstraction hides the details and exposes only the essential functionality,
                                     making code simpler and less error-prone.
        Standard Interface: By defining abstract methods, you enforce that subclasses implement these methods,
                            ensuring a standard interface.
        Encourages Reuse: Abstract classes act as blueprints, promoting code reuse and standardizing the design of classes
                          in a project.
        Abstraction in Python encourages clean, modular code by focusing on essential behavior and hiding complex details.
        It provides a way to define a common interface and forces derived classes to provide specific implementations,
        making code more organized and maintainable.
"""

from abc import ABC, abstractmethod


class AbstractClassName(ABC):
    @abstractmethod
    def abstract_method_name(self):
        pass


#########################################

from abc import ABC, abstractmethod


class Animal(ABC):  # Abstract base class
    @abstractmethod
    def sound(self):
        pass  # Abstract method with no implementation


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


# Creating instances of subclasses
dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow

"""
In Python, method overloading (defining multiple methods with the same name but different arguments) is not natively supported
because Python does not enforce method signatures like some statically typed languages (e.g., Java or C++).
However, we can simulate method overloading using techniques such as:

Default Arguments
Variable-Length Arguments (*args and **kwargs)
Explicit Method Overloading via a utility function.
Here’s a proper example of achieving method overloading in Python:
"""

# 1. Using Default Arguments
class Calculator:
    def multiply(self, a, b=1):  # Default value for `b`
        return a * b

# Example usage
calc = Calculator()
print(calc.multiply(5))       # Single argument (5 * 1 = 5)
print(calc.multiply(5, 10))   # Two arguments (5 * 10 = 50)


# 2. Using Variable-Length Arguments (*args)
class Calculator:
    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

# Example usage
calc = Calculator()
print(calc.multiply(5))            # Single argument (5)
print(calc.multiply(5, 10))        # Two arguments (5 * 10 = 50)
print(calc.multiply(5, 10, 2))     # Three arguments (5 * 10 * 2 = 100)


# 3. Explicit Method Overloading via Dispatching
class Calculator:
    def multiply(self, *args):
        if len(args) == 1:
            return args[0] ** 2  # Square if one argument
        elif len(args) == 2:
            return args[0] * args[1]  # Multiply if two arguments
        else:
            raise ValueError("Unsupported number of arguments!")

# Example usage
calc = Calculator()
print(calc.multiply(5))         # Single argument (5 * 5 = 25)
print(calc.multiply(5, 10))     # Two arguments (5 * 10 = 50)
# print(calc.multiply(5, 10, 2))  # Raises ValueError


"""
4. Using @singledispatch from functools
The most Pythonic way to achieve method overloading is by using @singledispatch, 
which enables function overloading based on argument types.
"""
from functools import singledispatch

@singledispatch
def greet(arg):
    print("Hello!")

@greet.register
def _(arg: str):
    print(f"Hello, {arg}!")

@greet.register
def _(arg: int):
    print(f"You entered the number {arg}!")

# Example usage
greet("Alice")   # Hello, Alice! (overload for str)
greet(42)        # You entered the number 42! (overload for int)
greet(3.14)      # Hello! (default implementation)


"""
Best Practice for Method Overloading in Python
While Python does not directly support method overloading, these approaches allow you to achieve similar functionality:

Use default arguments or variable-length arguments for straightforward cases.
For advanced scenarios, prefer @singledispatch, which is clean and leverages Python’s dynamic typing.
Avoid unnecessary complexity, as Python encourages writing clear and simple code.
"""

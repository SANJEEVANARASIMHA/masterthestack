"""
Encapsulation is one of the fundamental principles of object-oriented programming.
It involves bundling data (attributes) and methods (functions) that operate on the data into a single unit, i.e., a class.
It also provides controlled access to these attributes and methods, usually by defining them as public, protected, or private.
"""


# Key Concepts
# Public Members: Accessible from anywhere.

class Example:
    def __init__(self):
        self.public_attribute = "I am public"


obj = Example()
print(obj.public_attribute)  # Accessible


# Protected Members: Accessible within the class and its subclasses.
class Example:
    def __init__(self):
        self._protected_attribute = "I am protected"


obj = Example()
print(obj._protected_attribute)  # Accessible but with a warning to not access directly


# Private Members: Accessible only within the class.
class Example:
    def __init__(self):
        self.__private_attribute = "I am private"


obj = Example()
# print(obj.__private_attribute)  # Raises an AttributeError
"""
Real-Time Example of Encapsulation
Let’s consider a banking system where sensitive information like account balance must not be directly accessible 
or modifiable by users.
"""


class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = initial_balance  # Private attribute

    # Public method to get balance
    def get_balance(self):
        return f"The balance for {self.account_holder} is ${self.__balance}"

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"${amount} deposited successfully. Updated balance: ${self.__balance}"
        else:
            return "Invalid deposit amount!"

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"${amount} withdrawn successfully. Remaining balance: ${self.__balance}"
        elif amount > self.__balance:
            return "Insufficient balance!"
        else:
            return "Invalid withdrawal amount!"


# Create an instance of BankAccount
account = BankAccount("John Doe", 1000)

# Access the public attribute
print(account.account_holder)  # Output: John Doe

# Access balance through getter method (indirect access)
print(account.get_balance())  # Output: The balance for John Doe is $1000

# Deposit money
print(account.deposit(500))  # Output: $500 deposited successfully. Updated balance: $1500

# Attempt to access private balance directly (should raise error)
# print(account.__balance)     # Uncommenting this will raise an AttributeError

# Withdraw money
print(account.withdraw(200))  # Output: $200 withdrawn successfully. Remaining balance: $1300

# Try invalid operations
print(account.withdraw(2000))  # Output: Insufficient balance!

"""
Why Encapsulation?
    Data Security: Prevent unauthorized access to sensitive information.
    Control: Provides control over the modification of attributes.
    Code Maintenance: Easier to modify and maintain encapsulated classes.
    Abstraction: Hides unnecessary details and exposes only essential information.
    Encapsulation ensures that only validated and intended changes are made to the data, providing robustness to the application.
"""


# 1. Data Security,  Encapsulation restricts direct access to sensitive data, ensuring it’s modified only through
# controlled methods.
# Example: Securing a password in a user management system.
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private attribute

    def get_username(self):
        return self.username

    def update_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            return "Password updated successfully."
        else:
            return "Incorrect old password!"


# Creating a user
user = User("john_doe", "secure123")

# Accessing username
print(user.get_username())  # Output: john_doe

# Trying to access password directly (not allowed)
# print(user.__password)  # Uncommenting will raise AttributeError

# Updating the password securely
print(user.update_password("secure123", "newsecure456"))  # Output: Password updated successfully.


# 2. Control Encapsulation allows validation and controlled access to attributes, ensuring they remain consistent.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:  # Validate age
            self.__age = age
            return "Age updated successfully."
        else:
            return "Invalid age!"


# Creating a person
person = Person("Alice", 25)

# Accessing age through getter
print(person.get_age())  # Output: 25

# Updating age with validation
print(person.set_age(30))  # Output: Age updated successfully.
print(person.set_age(-5))  # Output: Invalid age!


# 3. Code Maintenance Encapsulation makes code modular and easy to maintain.
# Changes to internal implementation don’t affect external code.
# Example: A calculator class where methods hide complex logic from users.

class Calculator:
    def __init__(self):
        self.__history = []  # Private attribute to maintain calculation history

    def add(self, a, b):
        result = a + b
        self.__history.append(f"Added {a} and {b}: {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.__history.append(f"Subtracted {b} from {a}: {result}")
        return result

    def get_history(self):
        return self.__history


# Using the calculator
calc = Calculator()
print(calc.add(10, 5))  # Output: 15
print(calc.subtract(20, 5))  # Output: 15

# Access calculation history
print(calc.get_history())  # Output: ['Added 10 and 5: 15', 'Subtracted 5 from 20: 15']


# 4. Abstraction Encapsulation helps hide unnecessary implementation details, exposing only essential parts of the
# functionality.

class ATM:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def check_balance(self):
        return f"Your account balance is ${self.__balance}"

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Successfully withdrawn ${amount}. Remaining balance: ${self.__balance}"
        else:
            return "Insufficient funds!"


# Using the ATM
atm = ATM(1000)

# Checking balance
print(atm.check_balance())  # Output: Your account balance is $1000

# Withdrawing money
print(atm.withdraw(200))  # Output: Successfully withdrawn $200. Remaining balance: $800

# Internal details (like `__balance`) are hidden
# print(atm.__balance)  # Uncommenting will raise AttributeError

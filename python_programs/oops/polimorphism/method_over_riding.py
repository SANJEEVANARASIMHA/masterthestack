# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print(f"This is a vehicle from {self.brand}.")

# Intermediate derived class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call the base class initializer
        self.model = model

    def display_info(self):  # Override the base class method
        print(f"This is a {self.model} car from {self.brand}.")

# Further derived class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call the intermediate class initializer
        self.battery_capacity = battery_capacity

    def display_info(self):  # Override the intermediate class method
        print(f"This is an electric car ({self.model}) from {self.brand} with a {self.battery_capacity} kWh battery.")

# Example usage
vehicle = Vehicle("Generic Brand")
vehicle.display_info()  # From Vehicle

car = Car("Toyota", "Camry")
car.display_info()  # From Car (overridden method)

electric_car = ElectricCar("Tesla", "Model S", 100)
electric_car.display_info()  # From ElectricCar (overridden method)
    

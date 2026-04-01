# exercise.py - Practice OOP inheritance

# Given base class:
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f"{self.year} {self.make} {self.model}"

    def fuel_type(self):
        return "Unknown"


# TODO 1: Create a class 'Car(Vehicle)' with an extra attribute 'num_doors'.
# Call super().__init__() properly.
# class Car(Vehicle):
#     ...

# TODO 2: Override 'fuel_type()' in Car to return "Gasoline".

# TODO 3: Create a class 'ElectricCar(Car)' with an attribute 'battery_kwh'.
# Override 'fuel_type()' to return "Electric".
# class ElectricCar(Car):
#     ...

# TODO 4: Add a method 'range_estimate()' to ElectricCar that returns
# battery_kwh * 6 (a rough km estimate).

# TODO 5: Create a list of one Car and one ElectricCar.
# Print their describe() and fuel_type() using a for loop (polymorphism).

# TODO 6: Check and print whether your ElectricCar is an instance of
# Vehicle, Car, and ElectricCar.

# CHALLENGE: Add a '__repr__' to Vehicle that includes make, model, year.
# Verify that repr() works on Car and ElectricCar automatically.

# --- Verification ---
print("--- Results ---")
try:
    c = Car("Toyota", "Camry", 2022, 4)
    e = ElectricCar("Tesla", "Model 3", 2024, 4, 82)
    print(c.describe(), "|", c.fuel_type())
    print(e.describe(), "|", e.fuel_type(), "| Range:", e.range_estimate(), "km")
except NameError as e_:
    print(f"Error: {e_} — fill in all TODOs")

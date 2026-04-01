# solution.py - OOP inheritance answers

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f"{self.year} {self.make} {self.model}"

    def fuel_type(self):
        return "Unknown"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.make!r}, {self.model!r}, {self.year})"


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def fuel_type(self):
        return "Gasoline"


class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_kwh):
        super().__init__(make, model, year, num_doors)
        self.battery_kwh = battery_kwh

    def fuel_type(self):
        return "Electric"

    def range_estimate(self):
        return self.battery_kwh * 6


# Verification
c = Car("Toyota", "Camry", 2022, 4)
e = ElectricCar("Tesla", "Model 3", 2024, 4, 82)

print("--- Verification ---")
for v in [c, e]:
    print(f"{v.describe()} | Fuel: {v.fuel_type()}")

print(f"\nRange estimate: {e.range_estimate()} km")

print("\n--- isinstance checks ---")
print(f"ElectricCar is Vehicle? {isinstance(e, Vehicle)}")
print(f"ElectricCar is Car? {isinstance(e, Car)}")
print(f"ElectricCar is ElectricCar? {isinstance(e, ElectricCar)}")

print(f"\nrepr(c): {repr(c)}")
print(f"repr(e): {repr(e)}")

print("\n--- Why it works ---")
print("1. super().__init__() propagates up the chain: ElectricCar -> Car -> Vehicle.")
print("2. Polymorphism: same .describe()/.fuel_type() call works on all subclass instances.")
print("3. isinstance() checks entire MRO (method resolution order), so ElectricCar is also a Vehicle.")
print("4. __repr__ on Vehicle is inherited automatically by all subclasses.")

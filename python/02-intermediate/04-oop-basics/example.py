# example.py - Defining and using classes

# 1. Basic class with __init__ and methods
class Dog:
    # Class attribute — shared by all instances
    species = "Canis familiaris"

    def __init__(self, name, breed, age):
        # Instance attributes — unique to each object
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."

    # __repr__ — unambiguous string representation (used in debugging)
    def __repr__(self):
        return f"Dog(name={self.name!r}, breed={self.breed!r}, age={self.age})"

    # __str__ — friendly string representation (used by print())
    def __str__(self):
        return self.describe()


# 2. Creating instances
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Rex", "German Shepherd", 5)

print("--- Instances ---")
print(dog1)            # calls __str__
print(repr(dog2))      # calls __repr__
print(dog1.bark())

# 3. Accessing attributes
print("\n--- Attributes ---")
print(f"Name: {dog1.name}")
print(f"Species (class attr): {Dog.species}")
print(f"Same species? {dog1.species == dog2.species}")

# 4. @property — computed read-only attribute
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2


c = Circle(5)
print("\n--- @property ---")
print(f"Radius: {c.radius}")
print(f"Diameter: {c.diameter}")
print(f"Area: {c.area:.2f}")

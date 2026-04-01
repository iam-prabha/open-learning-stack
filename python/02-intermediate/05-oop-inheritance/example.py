# example.py - Inheritance, super(), polymorphism

# 1. Base class
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return f"Animal({self.name!r})"


# 2. Subclass — inherits and extends
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, sound="Woof")   # call parent __init__
        self.breed = breed

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

    def __str__(self):
        return f"Dog({self.name!r}, breed={self.breed!r})"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, sound="Meow")
        self.indoor = indoor

    def speak(self):
        # Override — add to parent behaviour
        base = super().speak()
        return base + " (softly)"


# 3. Using instances
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers")

print("--- Inheritance ---")
print(dog)
print(dog.speak())     # inherited from Animal
print(dog.fetch("ball"))

print()
print(cat)
print(cat.speak())     # overridden in Cat

# 4. Polymorphism — treat all Animals uniformly
animals = [dog, cat, Dog("Rex", "Husky"), Cat("Luna")]
print("\n--- Polymorphism ---")
for animal in animals:
    print(animal.speak())

# 5. isinstance and issubclass checks
print("\n--- isinstance checks ---")
print(f"dog is Animal? {isinstance(dog, Animal)}")
print(f"cat is Dog? {isinstance(cat, Dog)}")
print(f"Dog is subclass of Animal? {issubclass(Dog, Animal)}")

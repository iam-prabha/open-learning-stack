# example.py - Demonstration of defining and calling functions

# 1. Defining a simple function
def greet():
    print("Hello from a function!")

# Calling the function
print("--- Simple function ---")
greet()

# 2. Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

print("\n--- Parameters ---")
greet_user("Alice")
greet_user("Bob")

# 3. function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print("\n--- Return Value ---")
print(f"5 + 10 = {result}")

# 4. function with default arguments
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

print("\n--- Default Arguments ---")
describe_pet("Buddy")              # Uses default "dog"
describe_pet("Whiskers", "cat")    # Overrides default

# 5. Multiple return values (using tuples implicitly)
def get_user_stats():
    # Imagine fetching from a database
    return "Alice", 1500, 10

name, score, level = get_user_stats()
print("\n--- Multiple Returns ---")
print(f"Player: {name}, Score: {score}, Level: {level}")

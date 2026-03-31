# example.py - Demonstration of variable assignment and re-assignment

# 1. Assignment: Giving a name to a value
score = 10
player_name = "Alice"
is_active = True

print(f"Player: {player_name}")
print(f"Score: {score}")
print(f"Status: {is_active}")

# 2. Re-assignment: Changing the value a name points to
score = 25
print(f"\nNew Score: {score}")

# 3. Multiple Assignment: Assigning values to multiple variables at once
x, y, z = 5, 10, 15
print(f"\nx: {x}, y: {y}, z: {z}")

# 4. Swapping values: A Pythonic way to swap two variables
a = "Primary"
b = "Secondary"
print(f"\nBefore swap: a={a}, b={b}")

a, b = b, a
print(f"After swap: a={a}, b={b}")

# 5. Dynamic Typing: Checking the type of a variable
price = 99.99
print(f"\nValue: {price}, Type: {type(price)}")

price = "Ninety-nine"  # Re-assigning to a different type
print(f"Value: {price}, Type: {type(price)}")

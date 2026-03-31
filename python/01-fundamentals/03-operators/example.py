# example.py - Demonstration of common Python operators

# 1. Arithmetic Operators
a, b = 10, 3
print("--- Arithmetic ---")
print(f"a + b = {a + b}")   # Addition
print(f"a - b = {a - b}")   # Subtraction
print(f"a * b = {a * b}")   # Multiplication
print(f"a / b = {a / b}")   # Division (always returns float)
print(f"a // b = {a // b}") # Floor Division (removes decimal)
print(f"a % b = {a % b}")   # Modulo (returns remainder)
print(f"a ** b = {a ** b}") # Exponentiation (a to the power of b)

# 2. Comparison Operators
x, y = 5, 10
print("\n--- Comparison ---")
print(f"x == y: {x == y}")   # Equal to
print(f"x != y: {x != y}")   # Not equal to
print(f"x > y: {x > y}")     # Greater than
print(f"x < y: {x < y}")     # Less than
print(f"x >= 5: {x >= 5}")   # Greater than or equal to

# 3. Logical Operators
is_student = True
has_discount = False
print("\n--- Logical ---")
print(f"Student AND Discount: {is_student and has_discount}")
print(f"Student OR Discount: {is_student or has_discount}")
print(f"NOT Student: {not is_student}")

# 4. Assignment (Shortcut) Operators
count = 0
count += 1   # Same as count = count + 1
count *= 5   # Same as count = count * 5
print("\n--- Assignment Shortcut ---")
print(f"Count: {count}")

# 5. Membership Operators
fruits = ["apple", "banana", "cherry"]
print("\n--- Membership ---")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

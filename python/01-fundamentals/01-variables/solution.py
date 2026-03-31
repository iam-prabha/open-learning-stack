# solution.py - Answers and explanations for variables exercises

# TODO 1: Create a variable named 'city' and assign it your home city name
city = "Bengaluru"

# TODO 2: Create a variable named 'year' and assign it the current year
year = 2026

# TODO 3: Create a variable named 'is_learning_python' and assign it a boolean value
is_learning_python = True

# TODO 4: Now, update 'city' to be a different city name
city = "Mysuru"

# TODO 5: Create three variables 'a', 'b', and 'c' using multiple assignment.
# Assign them 10, 20, and 30 respectively.
a, b, c = 10, 20, 30

# TODO 6: Swap the values of 'a' and 'b' using the Pythonic way.
a, b = b, a

# CHALLENGE:
# Variables cannot start with numbers!
# first_place = "Gold" is the correct way.

first_place = "Gold"

# --- Verification ---
print("--- Verification ---")
print(f"City: {city}")
print(f"Year: {year}")
print(f"Learning Python: {is_learning_python}")
print(f"a: {a}, b: {b}, c: {c}")

print("\n--- Why it works ---")
print("1. Python knows your variable type from the value you provide.")
print("2. 'city' was re-assigned, so the old value is gone.")
print("3. 'a, b = b, a' swaps values without needing a temporary variable!")

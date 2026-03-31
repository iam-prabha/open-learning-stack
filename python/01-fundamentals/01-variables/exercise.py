# exercise.py - Practice with variable assignment and naming

# TODO 1: Create a variable named 'city' and assign it your home city name
# city = ...

# TODO 2: Create a variable named 'year' and assign it the current year
# year = ...

# TODO 3: Create a variable named 'is_learning_python' and assign it a boolean value
# is_learning_python = ...

# TODO 4: Now, update 'city' to be a different city name
# ...

# TODO 5: Create three variables 'a', 'b', and 'c' using multiple assignment.
# Assign them 10, 20, and 30 respectively.
# ...

# TODO 6: Swap the values of 'a' and 'b' using the Pythonic way.
# ...

# CHALLENGE: 
# Create a variable named '1st_place' and try to assign it a value. 
# Why does this fail? (Read about variable naming rules in README.md)
# Then, rename it to follow PEP 8 standards.
# ...

# --- DON'T CHANGE ANYTHING BELOW THIS LINE ---
print("--- Results ---")
try:
    print(f"City: {city}")
    print(f"Year: {year}")
    print(f"Learning Python: {is_learning_python}")
    print(f"a: {a}, b: {b}, c: {c}")
except NameError as e:
    print(f"Error: {e} - Make sure you filled in all TODOs!")

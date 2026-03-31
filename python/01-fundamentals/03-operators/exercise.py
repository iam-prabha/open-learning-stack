# exercise.py - Practice with operators

# TODO 1: Create two variables x=15 and y=4. Calculate the remainder of x divided by y.
# remainder = ...

# TODO 2: Use an assignment shortcut to add 5 to 'remainder'.
# ...

# TODO 3: Create a boolean 'is_equal' that checks if 10 * 2 is equal to 40 / 2.
# ...

# TODO 4: Create a boolean 'is_valid' that is True if (10 > 5) AND (20 < 30).
# ...

# TODO 5: Use a membership operator to check if "Python" is in the string "Learning Python".
# contains_python = ...

# TODO 6: Calculate the result of 2 + 3 * 4. 
# Did you expect 20 or 14? (Python follows PEMDAS/BODMAS)
# result = ...

# CHALLENGE: 
# Using only operators, swap x and y WITHOUT using y, x = x, y.
# Hint: Use addition and subtraction (be careful!)
# ...

# --- Verification ---
print("--- Results ---")
try:
    print(f"Remainder: {remainder}")
    print(f"Is Equal: {is_equal}")
    print(f"Is Valid: {is_valid}")
    print(f"Contains Python: {contains_python}")
    print(f"Result: {result}")
except NameError as e:
    print(f"Error: {e} - Make sure you filled in all TODOs!")

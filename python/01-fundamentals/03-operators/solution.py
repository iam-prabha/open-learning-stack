# solution.py - Answers and explanations for operators exercises

# TODO 1: Create two variables x=15 and y=4. Calculate the remainder of x divided by y.
x, y = 15, 4
remainder = x % y  # 15 / 4 = 3 with a remainder of 3

# TODO 2: Use an assignment shortcut to add 5 to 'remainder'.
remainder += 5  # now it's 8

# TODO 3: Create a boolean 'is_equal' that checks if 10 * 2 is equal to 40 / 2.
is_equal = (10 * 2) == (40 / 2)  # 20 == 20.0, which is True

# TODO 4: Create a boolean 'is_valid' that is True if (10 > 5) AND (20 < 30).
is_valid = (10 > 5) and (20 < 30)  # True and True is True

# TODO 5: Use a membership operator to check if "Python" is in the string "Learning Python".
contains_python = "Python" in "Learning Python"

# TODO 6: Calculate the result of 2 + 3 * 4. 
result = 2 + 3 * 4  # 14 (Multiplication happens before addition)

# CHALLENGE: Swap x and y without a temporary variable
# x = 15, y = 4
x = x + y  # x = 19
y = x - y  # y = 19 - 4 = 15
x = x - y  # x = 19 - 15 = 4
# Now x = 4, y = 15

# --- Verification ---
print("--- Verification ---")
print(f"Remainder: {remainder}")
print(f"Is Equal: {is_equal}")
print(f"Is Valid: {is_valid}")
print(f"Contains Python: {contains_python}")
print(f"Result: {result}")
print(f"Swapped: x={x}, y={y}")

print("\n--- Why it works ---")
print("1. % (modulo) is the best way to get a remainder.")
print("2. x += 5 is cleaner than x = x + 5.")
print("3. Comparison operators always return a boolean (True/False).")
print("4. Python handles operator precedence (PEMDAS) automatically.")
print("5. The addition/subtraction swap is a classic programming trick (but use x, y = y, x in real Python code!)")

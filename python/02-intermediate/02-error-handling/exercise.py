# exercise.py - Practice error handling

# TODO 1: Write a function 'safe_divide(a, b)' that returns a/b,
# but catches ZeroDivisionError and returns None instead.
# def safe_divide(a, b):
#     ...

# TODO 2: Write a function 'read_int(prompt_value)' that converts a
# string to int, catches ValueError, and returns -1 on failure.
# def read_int(prompt_value):
#     ...

# TODO 3: Wrap both a risky conversion AND a print in try/except/else/finally.
# - try: convert "hello" to float
# - except ValueError: print "Bad input"
# - else: print the converted value
# - finally: print "Done"
# ...

# TODO 4: Define a custom exception 'NegativeNumberError(Exception)'
# that stores the offending number.
# class NegativeNumberError(Exception):
#     ...

# TODO 5: Write a function 'square_root(n)' that raises NegativeNumberError
# if n is negative, else returns n ** 0.5.
# def square_root(n):
#     ...

# TODO 6: Catch the NegativeNumberError from calling square_root(-9) and
# print a user-friendly message.
# ...

# CHALLENGE: Write a function 'load_config(path)' that opens a file,
# reads JSON from it, and handles FileNotFoundError and json.JSONDecodeError
# separately, returning a dict or None.
# import json
# def load_config(path):
#     ...

# --- Verification ---
print("--- Results ---")
try:
    print("safe_divide(10, 2):", safe_divide(10, 2))
    print("safe_divide(10, 0):", safe_divide(10, 0))
    print("read_int('42'):", read_int("42"))
    print("read_int('abc'):", read_int("abc"))
except NameError as e:
    print(f"Error: {e} — fill in all TODOs")

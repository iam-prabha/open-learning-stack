# solution.py - Error handling answers

import json
import math

# TODO 1
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

# TODO 2
def read_int(prompt_value):
    try:
        return int(prompt_value)
    except ValueError:
        return -1

# TODO 3
try:
    val = float("hello")
except ValueError:
    print("Bad input")
else:
    print(f"Converted: {val}")
finally:
    print("Done")

# TODO 4
class NegativeNumberError(Exception):
    def __init__(self, number):
        super().__init__(f"Expected non-negative, got {number}")
        self.number = number

# TODO 5
def square_root(n):
    if n < 0:
        raise NegativeNumberError(n)
    return math.sqrt(n)

# TODO 6
try:
    square_root(-9)
except NegativeNumberError as e:
    print(f"Cannot compute square root: {e}")

# CHALLENGE
def load_config(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found: {path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None

# --- Verification ---
print("\n--- Verification ---")
print("safe_divide(10, 2):", safe_divide(10, 2))
print("safe_divide(10, 0):", safe_divide(10, 0))
print("read_int('42'):", read_int("42"))
print("read_int('abc'):", read_int("abc"))
print("square_root(9):", square_root(9))
print("load_config('missing.json'):", load_config("missing.json"))

print("\n--- Why it works ---")
print("1. Specific exceptions (ZeroDivisionError) are caught before broad ones.")
print("2. 'else' only runs if NO exception was raised in the 'try' block.")
print("3. 'finally' always runs — perfect for cleanup (close file, release lock).")
print("4. Custom exceptions inherit from Exception and carry structured data.")

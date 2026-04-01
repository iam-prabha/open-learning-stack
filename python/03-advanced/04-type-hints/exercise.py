# exercise.py - Practice Type Hints

from typing import List, Dict, Optional, Union, Callable, Any

# TODO 1: Annotate this function to accept a list of integers and
# return their sum as an integer.
# def sum_list(nums):
#     return sum(nums)

# TODO 2: Annotate a variable 'user_data' as a dictionary with
# string keys and 'Any' values.
# user_data = ...

# TODO 3: Write a function 'get_first_element' that takes a list of strings
# and returns the first element, or None if the list is empty.
# (Hint: use Optional[str] for return type)
# def get_first_element(items):
#     ...

# TODO 4: Use Union to annotate a function 'parse_id' that accepts either
# an integer or a string and returns an integer.
# def parse_id(val):
#     ...

# TODO 5: Annotate a function 'apply_math' that takes:
# - an integer 'x'
# - a callable that takes one integer and returns one integer
# And returns the result of the callable on x.
# def apply_math(x, func):
#     ...

# TODO 6: Annotate an __init__ method for a 'User' class that takes
# 'username' (str) and an optional 'age' (int).
# class User:
#     ...

# CHALLENGE: Create a Protocol called 'Flyable' with a method 'fly() -> str'.
# Create a function 'launch(item: Flyable)' that prints the result of item.fly().

# --- Verification ---
print("--- Results ---")
# To verify, you would normally run 'mypy exercise.py'
print("Type hinting is mostly for static analysis.")

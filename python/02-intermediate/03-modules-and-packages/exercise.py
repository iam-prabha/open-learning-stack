# exercise.py - Practice with modules and packages

import math
import random
import os
import json
from datetime import datetime

# TODO 1: Use the 'math' module to calculate the hypotenuse
# of a right triangle with sides a=3 and b=4.
# hypotenuse = ...

# TODO 2: Use 'random' to pick 3 unique numbers from range(1, 10).
# sample = ...

# TODO 3: Use 'os.path' to check if a file "README.md" exists
# in the current directory. Store the result in 'readme_exists'.
# readme_exists = ...

# TODO 4: Use the 'datetime' module to compute how many days
# are left until New Year's Day (Jan 1, 2027).
# days_left = ...

# TODO 5: Use 'json.dumps' to convert a Python dict into a JSON string.
data = {"name": "Alice", "score": 95, "active": True}
# json_str = ...

# TODO 6: Use 'json.loads' to parse that JSON string back into a dict
# and access the 'name' field.
# parsed = ...
# name = ...

# CHALLENGE: Write a one-liner that lists all .py files in the current
# directory using os.listdir() and a list comprehension.
# py_files = ...

# --- Verification ---
print("--- Results ---")
try:
    print(f"Hypotenuse: {hypotenuse}")
    print(f"Sample: {sample}")
    print(f"README exists: {readme_exists}")
    print(f"Days left: {days_left}")
    print(f"JSON string: {json_str}")
    print(f"Parsed name: {name}")
    print(f"Python files: {py_files}")
except NameError as e:
    print(f"Error: {e} — fill in all TODOs")

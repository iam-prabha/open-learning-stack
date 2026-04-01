# solution.py - Modules and packages answers

import math
import random
import os
import json
from datetime import datetime

# TODO 1
hypotenuse = math.hypot(3, 4)   # Equivalent to sqrt(3**2 + 4**2)

# TODO 2
sample = random.sample(range(1, 10), 3)  # 3 unique values from [1, 9]

# TODO 3
readme_exists = os.path.exists("README.md")

# TODO 4
new_year = datetime(2027, 1, 1)
days_left = (new_year - datetime.now()).days

# TODO 5
data = {"name": "Alice", "score": 95, "active": True}
json_str = json.dumps(data)

# TODO 6
parsed = json.loads(json_str)
name = parsed["name"]

# CHALLENGE
py_files = [f for f in os.listdir(".") if f.endswith(".py")]

# --- Verification ---
print("--- Verification ---")
print(f"Hypotenuse: {hypotenuse}")
print(f"Sample: {sample}")
print(f"README exists: {readme_exists}")
print(f"Days to 2027: {days_left}")
print(f"JSON string: {json_str}")
print(f"Parsed name: {name}")
print(f"Python files: {py_files}")

print("\n--- Why it works ---")
print("1. math.hypot() is cleaner than writing sqrt(a**2 + b**2) manually.")
print("2. random.sample() guarantees no duplicates; random.choices() can repeat.")
print("3. os.path.exists() works cross-platform; don't hardcode path separators.")
print("4. json.dumps() -> str, json.loads() -> dict. The 's' stands for string.")

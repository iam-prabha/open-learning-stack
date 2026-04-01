# example.py - Importing modules and using the standard library

# 1. Importing a whole module
import math
print("--- math module ---")
print(f"pi: {math.pi:.5f}")
print(f"sqrt(16): {math.sqrt(16)}")
print(f"ceil(4.2): {math.ceil(4.2)}")

# 2. Importing specific names
from datetime import datetime, timedelta
print("\n--- datetime module ---")
now = datetime.now()
print(f"Now: {now.strftime('%Y-%m-%d %H:%M')}")
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

# 3. Aliasing
import random as rnd
print("\n--- random (aliased as rnd) ---")
print(f"Random int 1-10: {rnd.randint(1, 10)}")
print(f"Random choice: {rnd.choice(['apple', 'banana', 'cherry'])}")

# 4. Inspecting a module
import os
print("\n--- os module ---")
print(f"Current directory: {os.getcwd()}")
print(f"Path separator: {os.sep!r}")

# 5. The __name__ guard — prevents code running on import
print("\n--- __name__ guard ---")
# When this file is run directly, __name__ is "__main__"
# When imported by another module, __name__ is "example"
if __name__ == "__main__":
    print("Running as main script — not imported")

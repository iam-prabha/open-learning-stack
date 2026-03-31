# example.py - Demonstration of common Python string operations

# 1. Creation and Multi-line strings
title = "Python Programming"
description = """This is a multi-line 
string that spans 
multiple lines."""

# 2. Concatenation and Repetition
first, last = "Jane", "Doe"
full_name = first + " " + last
greeting = "Hello! " * 3
print("--- Concatenation & Repetition ---")
print(f"Name: {full_name}")
print(f"Greeting: {greeting}")

# 3. Indexing and Slicing (The Bead Necklace)
# P y t h o n
# 0 1 2 3 4 5
s = "Python"
print("\n--- Indexing & Slicing ---")
print(f"First character: {s[0]}")
print(f"Last character: {s[-1]}")
print(f"First 3 chars: {s[0:3]}")  # Stop index is exclusive
print(f"Step by 2: {s[::2]}")      # Every second character

# 4. String Methods
text = "  python code is fun  "
print("\n--- String Methods ---")
print(f"Uppercase: {text.upper()}")
print(f"Stripped: {text.strip()}")
print(f"Replace: {text.replace('fun', 'powerful')}")
print(f"Starts with '  py': {text.startswith('  py')}")

# 5. f-strings (The modern way to format)
name, age = "Alice", 30
formatted = f"{name} is {age} years old."
print("\n--- f-strings ---")
print(formatted)

# example.py - Demonstration of reading and writing files

filename = "test_file.txt"

# 1. Writing to a file (creates if it doesn't exist, overwrites if it does)
print("--- Writing to file ---")
with open(filename, "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a line of text.\n")
print(f"Successfully wrote to {filename}")

# 2. Appending to a file
print("\n--- Appending to file ---")
with open(filename, "a") as f:
    f.write("This line was added later.\n")
print(f"Successfully appended to {filename}")

# 3. Reading the whole file
print("\n--- Reading the whole file ---")
with open(filename, "r") as f:
    content = f.read()
    print(content)

# 4. Reading line by line (more memory-efficient)
print("--- Reading line by line ---")
with open(filename, "r") as f:
    for line in f:
        print(f"Line: {line.strip()}")  # strip() removes the newline char

# 5. Cleaning up (optional but good practice to delete the test file)
import os
if os.path.exists(filename):
    os.remove(filename)
    print(f"\nDeleted {filename} for cleanup.")

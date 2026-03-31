# solution.py - Answers and explanations for file IO exercises

import os

filename = "my_notes.txt"
copy_filename = "my_notes_copy.txt"

# TODO 2: Write lines
with open(filename, "w") as f:
    f.write("My favorite language is Python.\n")
    f.write("I am learning File IO today.\n")
    f.write("The date is 2026-03-31.\n")

# TODO 3: Append line
with open(filename, "a") as f:
    f.write("This line was appended!\n")

# TODO 4: Read all
print("--- Reading All ---")
with open(filename, "r") as f:
    print(f.read())

# TODO 5: Read first 2 lines
print("--- Reading First 2 Lines ---")
with open(filename, "r") as f:
    count = 0
    for line in f:
        print(line.strip())
        count += 1
        if count == 2:
            break

# TODO 6: Count words
with open(filename, "r") as f:
    content = f.read()
    words = content.split()
    word_count = len(words)
print(f"\nWord count: {word_count}")

# CHALLENGE: Copy file
with open(filename, "r") as source:
    content = source.read()
    with open(copy_filename, "w") as dest:
        dest.write(content)

# Cleanup (optional for this exercise)
if os.path.exists(filename):
    os.remove(filename)
if os.path.exists(copy_filename):
    os.remove(copy_filename)

print("\n--- Why it works ---")
print("1. 'with open(...)' is a context manager - it closes files automatically.")
print("2. 'w' mode overwrites; 'a' mode adds to the end.")
print("3. Iterating over the file object ('for line in f') is memory efficient for large files.")
print("4. .split() by default splits by whitespace, perfect for counting simple words.")

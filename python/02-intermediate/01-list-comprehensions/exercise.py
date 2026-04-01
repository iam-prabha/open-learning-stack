# exercise.py - Practice list comprehensions

# TODO 1: Use a list comprehension to create a list of cubes for numbers 1-5.
# cubes = ...

# TODO 2: Given words = ["Apple", "Banana", "Cherry", "Date"]
# create a list containing only words with more than 5 characters.
words = ["Apple", "Banana", "Cherry", "Date"]
# long_words = ...

# TODO 3: Given nums = [1, -2, 3, -4, 5]
# create a list of absolute values.
nums = [1, -2, 3, -4, 5]
# abs_vals = ...

# TODO 4: Use a list comprehension with an if-else to replace negative numbers
# in 'nums' with 0, and keep positives as-is.
# clamped = ...

# TODO 5: Create a list of tuples (n, n**2) for n in range(1, 6).
# pairs = ...

# TODO 6: Flatten this 2D list using a list comprehension.
grid = [[10, 20], [30, 40], [50, 60]]
# flat = ...

# CHALLENGE: Given a sentence, use a list comprehension to get the
# first letter of each word (that is longer than 3 characters).
sentence = "The quick brown fox jumps over the lazy dog"
# initials = ...

# --- Verification ---
print("--- Results ---")
try:
    print("Cubes:", cubes)
    print("Long words:", long_words)
    print("Abs vals:", abs_vals)
    print("Clamped:", clamped)
    print("Pairs:", pairs)
    print("Flat:", flat)
    print("Initials:", initials)
except NameError as e:
    print(f"Error: {e} — fill in all TODOs")

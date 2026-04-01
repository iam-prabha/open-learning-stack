# solution.py - Answers for list comprehensions

cubes = [x ** 3 for x in range(1, 6)]

words = ["Apple", "Banana", "Cherry", "Date"]
long_words = [w for w in words if len(w) > 5]

nums = [1, -2, 3, -4, 5]
abs_vals = [abs(n) for n in nums]

clamped = [n if n >= 0 else 0 for n in nums]

pairs = [(n, n ** 2) for n in range(1, 6)]

grid = [[10, 20], [30, 40], [50, 60]]
flat = [num for row in grid for num in row]

sentence = "The quick brown fox jumps over the lazy dog"
initials = [word[0] for word in sentence.split() if len(word) > 3]

print("--- Verification ---")
print("Cubes:", cubes)
print("Long words:", long_words)
print("Abs vals:", abs_vals)
print("Clamped:", clamped)
print("Pairs:", pairs)
print("Flat:", flat)
print("Initials:", initials)

print("\n--- Why it works ---")
print("1. [expr for x in iterable] — basic form.")
print("2. [expr for x in iterable if cond] — filter form.")
print("3. [a if cond else b for x in iterable] — ternary inside comprehension.")
print("4. Nested: [expr for row in matrix for item in row] — reads left-to-right like nested loops.")

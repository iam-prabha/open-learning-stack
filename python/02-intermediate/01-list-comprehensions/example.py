# example.py - List comprehensions in action

# 1. Basic: transform every item
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

# 2. With a filter condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Evens:", evens)

# 3. Transform AND filter together
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

# 4. String transformation
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print("Upper:", upper)

# 5. Nested list comprehension (flatten a 2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print("Flat:", flat)

# 6. With if-else (ternary) — labelling
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 7)]
print("Labels:", labels)

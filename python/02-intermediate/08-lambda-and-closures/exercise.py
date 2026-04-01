# exercise.py - Practice Lambda and Closures

# TODO 1: Create a lambda function 'square' that takes one argument and returns its square.
# square = ...

# TODO 2: Given a list of dictionaries, sort them by the 'age' key using a lambda.
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
# sorted_users = ...

# TODO 3: Use 'filter()' and a lambda to extract even numbers from this list.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = ...

# TODO 4: Write a closure factory 'make_power(p)' that returns a function
# which raises its input to the power of 'p'.
# def make_power(p):
#     ...

# TODO 5: Create 'cube' using make_power(3) and test it with cube(3).
# cube = ...

# TODO 6: Write a closure 'make_averager()' that keeps track of the sum and count
# of numbers passed to it, and returns the current average.
# (Hint: use 'nonlocal' for sum and count variables)
# def make_averager():
#     ...

# CHALLENGE: Fix this broken closure factory so each lambda uses its OWN value of 'i'.
def broken_factory():
    funcs = []
    for i in range(3):
        funcs.append(lambda x: x + i)
    return funcs

# --- Verification ---
print("--- Results ---")
try:
    print(f"Square 4: {square(4)}")
    print(f"Sorted users: {sorted_users}")
    print(f"Evens: {list(evens)}")
    print(f"Cube 3: {cube(3)}")
    avg = make_averager()
    print(f"Avg 10: {avg(10)}")
    print(f"Avg 20: {avg(20)}")
except NameError as e:
    print(f"Error: {e} — fill in all TODOs")

# exercise.py - Practice generators

# TODO 1: Write a generator function 'even_numbers(limit)' that yields
# even numbers from 2 up to 'limit' (inclusive).
# def even_numbers(limit):
#     ...

# TODO 2: Write a generator function 'fibonacci()' that yields the
# Fibonacci sequence indefinitely (0, 1, 1, 2, 3, 5, 8, ...).
# def fibonacci():
#     ...

# TODO 3: Using your fibonacci() generator, collect the first 10 values into a list.
# fib_list = ...

# TODO 4: Write a generator expression that yields squares of odd numbers
# from 1 to 20. (Generator expression, not a function)
# odd_squares_gen = ...

# TODO 5: Write a generator function 'chunk(iterable, size)' that yields
# successive non-overlapping chunks of 'size' from the iterable.
# e.g. chunk([1,2,3,4,5], 2) -> [1,2], [3,4], [5]
# def chunk(iterable, size):
#     ...

# TODO 6: Demonstrate that a generator is exhausted after one full iteration.
# Create a generator, iterate it once with list(), then iterate again.
# Show that the second list() call returns [].

# CHALLENGE: Write a generator 'running_average()' that accepts values
# via send() and yields the running average after each sent value.
# def running_average():
#     ...

# --- Verification ---
print("--- Results ---")
try:
    print("Even up to 10:", list(even_numbers(10)))
    print("First 10 fib:", fib_list)
    print("Odd squares:", list(odd_squares_gen))
    print("Chunks:", list(chunk([1,2,3,4,5,6,7], 3)))
except NameError as e:
    print(f"Error: {e} — fill in all TODOs")

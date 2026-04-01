# exercise.py - Practice decorators

import functools

# TODO 1: Write a decorator 'logger' that prints "[CALL] func_name" before
# calling the function and "[DONE] func_name" after. Use functools.wraps.
# def logger(func):
#     ...

# TODO 2: Apply @logger to a function 'add(a, b)' that returns a + b.
# @logger
# def add(a, b):
#     ...

# TODO 3: Write a decorator 'validate_positive' that raises ValueError
# if the first argument is negative, before calling the function.
# def validate_positive(func):
#     ...

# TODO 4: Apply @validate_positive to 'square_root(n)' which returns n**0.5.
# import math
# @validate_positive
# def square_root(n):
#     ...

# TODO 5: Write a decorator factory 'prefix(text)' that prepends 'text' to
# the string result of the wrapped function.
# def prefix(text):
#     ...

# TODO 6: Apply @prefix("RESULT: ") to function 'describe(x)' that returns str(x).
# @prefix("RESULT: ")
# def describe(x):
#     ...

# CHALLENGE: Write a 'cache' decorator that stores results in a dict
# keyed by the arguments. Call the wrapped function only if args not cached.
# def cache(func):
#     ...

# --- Verification ---
print("--- Results ---")
try:
    print(add(3, 5))
    print(square_root(16))
    try:
        square_root(-4)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    print(describe(42))
except NameError as e:
    print(f"Error: {e} — fill in all TODOs")

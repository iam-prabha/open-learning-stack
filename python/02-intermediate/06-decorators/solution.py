# solution.py - Decorators answers

import functools
import math

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[CALL] {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[DONE] {func.__name__}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b


def validate_positive(func):
    @functools.wraps(func)
    def wrapper(n, *args, **kwargs):
        if n < 0:
            raise ValueError(f"Expected non-negative, got {n}")
        return func(n, *args, **kwargs)
    return wrapper

@validate_positive
def square_root(n):
    return math.sqrt(n)


def prefix(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return text + str(func(*args, **kwargs))
        return wrapper
    return decorator

@prefix("RESULT: ")
def describe(x):
    return str(x)


def cache(func):
    _cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in _cache:
            _cache[args] = func(*args)
        return _cache[args]
    return wrapper

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# --- Verification ---
print("--- Verification ---")
print(add(3, 5))
print(square_root(16))
try:
    square_root(-4)
except ValueError as e:
    print(f"Caught: {e}")
print(describe(42))
print(f"fib(10): {fib(10)}")

print("\n--- Why it works ---")
print("1. functools.wraps copies __name__, __doc__ etc so debugging stays sane.")
print("2. *args, **kwargs in wrapper lets the decorator work on any function signature.")
print("3. A decorator factory (prefix) returns a decorator which returns a wrapper — 3 levels deep.")
print("4. The cache dict lives in the closure of 'wrapper' — persists across calls.")

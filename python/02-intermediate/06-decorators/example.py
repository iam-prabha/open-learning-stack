# example.py - Decorators in Python

import functools
import time

# 1. Basic decorator
def shout(func):
    @functools.wraps(func)  # preserves original func metadata
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet(name):
    """Return a greeting."""
    return f"hello, {name}"

print("--- Basic decorator ---")
print(greet("world"))
print(f"Function name preserved: {greet.__name__}")

# 2. Timing decorator (practical use case)
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[{func.__name__}] ran in {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print("\n--- Timer decorator ---")
result = slow_sum(1_000_000)
print(f"Sum: {result}")

# 3. Decorator with arguments (factory pattern)
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say(msg):
    print(f"  > {msg}")

print("\n--- Parameterised decorator ---")
say("Hello!")

# 4. Stacking decorators
@timer
@shout
def loud_greeting(name):
    return f"hi, {name}"

print("\n--- Stacked decorators ---")
print(loud_greeting("Python"))

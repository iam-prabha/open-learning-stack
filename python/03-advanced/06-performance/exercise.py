# exercise.py - Practice Performance

import timeit

# TODO 1: Compare the speed of 'a + b' (string concatenation) 
# vs '"".join([a, b])' for 1000 iterations.
# s1 = "hello"
# s2 = "world"
# ...

# TODO 2: Write a function 'sum_loop(n)' that uses a for loop to sum range(n).
# def sum_loop(n):
#     ...

# TODO 3: Write a function 'sum_builtin(n)' that uses the built-in 'sum()' function.
# def sum_builtin(n):
#     ...

# TODO 4: Use timeit to compare sum_loop(1000) and sum_builtin(1000).

# TODO 5: Create a large list of 100,000 numbers.
# data = list(range(100000))

# TODO 6: Measure how long it takes to find if -1 (not in list) 
# is in the list versus a set containing the same numbers.
# (Hint: use timeit.timeit(..., number=100))

# CHALLENGE: Profile this function using cProfile and identify which part
# is taking the longest.
# def mystery_task():
#     [x**2 for x in range(1000000)]
#     [x**3 for x in range(1000000)]

# --- Verification ---
print("--- Results ---")
# Print your benchmark results here

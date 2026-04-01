# example.py - Performance Profiling and Optimization

import timeit
import cProfile
import pstats
import io

# 1. Using timeit for micro-benchmarks
# Comparing loop vs list comprehension
print("--- micro-benchmark (timeit) ---")
loop_code = """
result = []
for i in range(1000):
    result.append(i * i)
"""
comp_code = "[i * i for i in range(1000)]"

loop_time = timeit.timeit(loop_code, number=10000)
comp_time = timeit.timeit(comp_code, number=10000)

print(f"Loop time: {loop_time:.4f}s")
print(f"Comprehension time: {comp_time:.4f}s")
print(f"Comprehension is {loop_time / comp_time:.2f}x faster")

# 2. Performance: list search vs set search
print("\n--- list vs set search ---")
data_list = list(range(10000))
data_set = set(data_list)

def search_list():
    return 9999 in data_list

def search_set():
    return 9999 in data_set

# number=1000 — sets are so fast we need many calls to see a difference
t_list = timeit.timeit(search_list, number=1000)
t_set = timeit.timeit(search_set, number=1000)
print(f"List search: {t_list:.6f}s")
print(f"Set search:  {t_set:.6f}s")
print(f"Set is {t_list / t_set:.1f}x faster!")

# 3. Using cProfile to find bottlenecks
def slow_function():
    # Simulate a bottleneck
    total = 0
    for i in range(1_000_000):
        total += i
    return total

def fast_function():
    return sum(range(1_000_000))

def main():
    slow_function()
    fast_function()

print("\n--- Profiling with cProfile ---")
pr = cProfile.Profile()
pr.enable()
main()
pr.disable()

# Print the report
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
ps.print_stats()
print(s.getvalue())

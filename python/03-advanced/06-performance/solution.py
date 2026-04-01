# solution.py - Performance answers

import timeit
import cProfile

# TODO 1
s1, s2 = "hello", "world"
t_concat = timeit.timeit(lambda: s1 + s2, number=10000)
t_join = timeit.timeit(lambda: "".join([s1, s2]), number=10000)

# TODO 2 & 3
def sum_loop(n):
    total = 0
    for i in range(n):
        total += i
    return total

def sum_builtin(n):
    return sum(range(n))

# TODO 4
t_loop = timeit.timeit(lambda: sum_loop(1000), number=10000)
t_builtin = timeit.timeit(lambda: sum_builtin(1000), number=10000)

# TODO 5 & 6
data_list = list(range(100000))
data_set = set(data_list)
t_list = timeit.timeit(lambda: -1 in data_list, number=100)
t_set = timeit.timeit(lambda: -1 in data_set, number=100)

# CHALLENGE
def mystery_task():
    print("Squaring...")
    [x**2 for x in range(1000000)]
    print("Cubing...")
    [x**3 for x in range(1000000)]

# --- Verification ---
print("--- Verification ---")
print(f"String + vs Join: {t_concat:.6f}s vs {t_join:.6f}s")
print(f"Loop vs Builtin sum: {t_loop:.4f}s vs {t_builtin:.4f}s")
print(f"List vs Set search:  {t_list:.6f}s vs {t_set:.6f}s")

print("\nRunning cProfile on mystery_task:")
cProfile.run('mystery_task()')

print("\n--- Why it works ---")
print("1. Built-ins are faster: sum() is implemented in C; a Python loop is slower.")
print("2. Memory vs Speed: Sets use more memory than lists but search in O(1) time instead of O(n).")
print("3. timeit: Essential for small code snippets; ignores background CPU noise.")
print("4. cProfile: Essential for large programs; shows 'tottime' (time in that function) vs 'cumtime' (time including calls).")

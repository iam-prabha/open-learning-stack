# example.py - Lambda functions and Closures

# 1. Lambda basics
add = lambda x, y: x + y
print("--- Lambda basics ---")
print(f"10 + 20 = {add(10, 20)}")

# 2. Lambda in sorting
pairs = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
# Sort by the second element of the tuple
pairs.sort(key=lambda pair: pair[1])
print("\n--- Sorting with lambda ---")
print(f"Sorted by name: {pairs}")

# 3. Simple Closure
def make_multiplier(n):
    # n is "captured" by the inner function
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print("\n--- Basic Closure ---")
print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")

# 4. Using 'nonlocal' in closures
def make_counter():
    count = 0
    def counter():
        nonlocal count  # allows modification of outer scope variable
        count += 1
        return count
    return counter

my_counter = make_counter()
print("\n--- Nonlocal in Closure ---")
print(f"First call: {my_counter()}")
print(f"Second call: {my_counter()}")
print(f"Third call: {my_counter()}")

# 5. The "Late Binding" Gotcha
def create_multipliers():
    return [lambda x: x * i for i in range(3)]

# You might expect this to return [0, 2, 4] for x=2
# But it returns [4, 4, 4] because 'i' is shared!
print("\n--- Late Binding Gotcha ---")
for m in create_multipliers():
    print(f"m(2) = {m(2)}")

# Fix: capture value using default argument
def create_fixed_multipliers():
    return [lambda x, i=i: x * i for i in range(3)]

print("\n--- Fixed Binding ---")
for m in create_fixed_multipliers():
    print(f"m(2) = {m(2)}")

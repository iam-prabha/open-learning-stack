# solution.py - Lambda and Closures answers

# TODO 1
square = lambda x: x**2

# TODO 2
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_users = sorted(users, key=lambda u: u["age"])

# TODO 3
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, nums)

# TODO 4
def make_power(p):
    def power(x):
        return x ** p
    return power

# TODO 5
cube = make_power(3)

# TODO 6
def make_averager():
    total = 0
    count = 0
    def averager(new_value):
        nonlocal total, count
        total += new_value
        count += 1
        return total / count
    return averager

# CHALLENGE FIX
def fixed_factory():
    funcs = []
    for i in range(3):
        # Capture the current value of i by making it a default argument
        funcs.append(lambda x, i=i: x + i)
    return funcs

# --- Verification ---
print("--- Verification ---")
print(f"Square 4: {square(4)}")
print(f"Sorted users: {sorted_users}")
print(f"Evens: {list(evens)}")
print(f"Cube 3: {cube(3)}")

avg = make_averager()
print(f"Avg 10: {avg(10)}")
print(f"Avg 20: {avg(20)}")

print("\n--- Why it works ---")
print("1. Lambda: lambda arguments: expression. It's an anonymous expression.")
print("2. Closure: The inner function 'power' references 'p' which is in the outer scope.")
print("3. nonlocal: Required when the closure needs to MODIFY a variable from the outer scope.")
print("4. Late Binding Fix: Default arguments are evaluated at definition time, 'snapping' the current value.")

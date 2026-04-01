# solution.py - Generators answers

# TODO 1
def even_numbers(limit):
    n = 2
    while n <= limit:
        yield n
        n += 2

# TODO 2
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# TODO 3
gen = fibonacci()
fib_list = [next(gen) for _ in range(10)]

# TODO 4
odd_squares_gen = (x ** 2 for x in range(1, 21) if x % 2 != 0)

# TODO 5
def chunk(iterable, size):
    lst = list(iterable)
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

# TODO 6 (demonstration)
g = even_numbers(6)
first_pass = list(g)   # consumes generator
second_pass = list(g)  # exhausted — returns []

# CHALLENGE
def running_average():
    total = 0.0
    count = 0
    while True:
        value = yield (total / count) if count else 0
        if value is not None:
            total += value
            count += 1

# --- Verification ---
print("--- Verification ---")
print("Even up to 10:", list(even_numbers(10)))
print("First 10 fib:", fib_list)
print("Odd squares:", list(odd_squares_gen))
print("Chunks:", list(chunk([1,2,3,4,5,6,7], 3)))
print(f"First pass: {first_pass}, Second pass: {second_pass}")

avg_gen = running_average()
next(avg_gen)  # prime
print("Running avg after 10:", avg_gen.send(10))
print("Running avg after 20:", avg_gen.send(20))
print("Running avg after 30:", avg_gen.send(30))

print("\n--- Why it works ---")
print("1. yield suspends the function; next() resumes it — no list built in memory.")
print("2. Fibonacci generator is infinite — only compute as many as you request.")
print("3. Generator expressions use () not [] — lazy, not eager.")
print("4. Once exhausted a generator raises StopIteration; list() returns [].")

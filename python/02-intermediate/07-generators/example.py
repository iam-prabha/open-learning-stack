# example.py - Generators in Python

# 1. Basic generator function
def countdown(n):
    while n > 0:
        yield n          # suspends here and sends n to caller
        n -= 1

print("--- Basic generator ---")
for num in countdown(5):
    print(num, end=" ")
print()

# 2. Infinite generator
def integers_from(start=0):
    n = start
    while True:
        yield n
        n += 1

print("\n--- Infinite generator (first 5) ---")
gen = integers_from(10)
for _ in range(5):
    print(next(gen), end=" ")
print()

# 3. Generator expression (lazy list comprehension)
squares_gen = (x ** 2 for x in range(1, 6))
print("\n--- Generator expression ---")
print(f"Type: {type(squares_gen)}")
print(list(squares_gen))   # consume into list

# 4. Generators as data pipelines
def read_numbers(limit):
    for i in range(1, limit + 1):
        yield i

def square_gen(gen):
    for n in gen:
        yield n ** 2

def filter_even(gen):
    for n in gen:
        if n % 2 == 0:
            yield n

print("\n--- Generator pipeline ---")
pipeline = filter_even(square_gen(read_numbers(10)))
print(list(pipeline))  # [4, 16, 36, 64, 100]

# 5. send() and two-way communication
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

print("\n--- send() ---")
acc = accumulator()
next(acc)         # prime the generator
print(acc.send(10))
print(acc.send(20))
print(acc.send(5))

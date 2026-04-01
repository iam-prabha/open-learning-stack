# solution.py - Concurrency answers

import threading
import multiprocessing
import asyncio
import time

# TODO 1 & 2: Threading
def print_numbers():
    for i in range(1, 6):
        time.sleep(0.5)
        print(f"Number: {i}")

def run_threaded():
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_numbers)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# TODO 3: Multiprocessing
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def count_primes(limit):
    return sum(1 for i in range(limit) if is_prime(i))

def run_proc():
    with multiprocessing.Pool() as pool:
        results = pool.map(count_primes, [100000, 100000, 100000])
    print(f"Primes counted: {results}")

# TODO 4: Locks
counter = 0
counter_lock = threading.Lock()
def increment():
    global counter
    with counter_lock:
        temp = counter
        time.sleep(0.01) # increase chance of race condition
        counter = temp + 1

# TODO 5 & 6: Asyncio
async def fetch_data(id):
    await asyncio.sleep(1)
    return f"Data for id {id}"

async def main_async():
    results = await asyncio.gather(fetch_data(1), fetch_data(2), fetch_data(3))
    print(f"Async results: {results}")

# --- Verification ---
print("--- Verification ---")
print("Starting threads...")
run_threaded()

print("\nStarting multiprocessing...")
run_proc()

print("\nStarting asyncio...")
asyncio.run(main_async())

print("\n--- Why it works ---")
print("1. Threading: Useful for I/O but the GIL means only one thread runs bytecode at a time.")
print("2. Multiprocessing: Bypasses cases the GIL by using separate memory and Python instances.")
print("3. Asyncio: Efficient single-threaded concurrency where tasks 'yield' during wait times.")
print("4. Locks: Essential for thread-safe access to shared data.")

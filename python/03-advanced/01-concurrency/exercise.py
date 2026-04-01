# exercise.py - Practice Concurrency

import threading
import multiprocessing
import asyncio
import time

# TODO 1: Write a function 'print_numbers()' that prints numbers 1-5 with a 0.5s delay.
# def print_numbers():
#     ...

# TODO 2: Start two threads that both run 'print_numbers()' concurrently.
# Wait for both to finish.

# TODO 3: Write a CPU-heavy function 'find_primes(n)' and run it across
# multiple processes using multiprocessing.Pool.
# def find_primes(n):
#     ...

# TODO 4: Use a Lock to prevent two threads from modifying the same
# global variable 'counter' at the same time.
# counter = 0
# counter_lock = threading.Lock()
# def increment():
#     ...

# TODO 5: Create an async function 'fetch_data(id)' that sleeps (simulates network)
# for 1 second and then returns a string like "Data for id {id}".
# async def fetch_data(id):
#     ...

# TODO 6: Run fetch_data for IDs 1, 2, and 3 concurrently using asyncio.gather().

# CHALLENGE: Compare the execution time of running a CPU-heavy task sequentially
# vs with threading vs with multiprocessing. Explain why threading might 
# not be faster for CPU-bound tasks in Python.

# --- Verification ---
print("--- Results ---")
try:
    # Test your code here
    pass
except NameError as e:
    print(f"Error: {e} — fill in all TODOs")

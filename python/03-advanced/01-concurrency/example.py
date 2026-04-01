# example.py - Threading, Multiprocessing, and Asyncio

import threading
import multiprocessing
import asyncio
import time

# 1. Threading (I/O Bound task simulation)
def thread_task(name):
    print(f"  [Thread {name}] starting...")
    time.sleep(1)  # Simulate I/O
    print(f"  [Thread {name}] done.")

def run_threads():
    threads = []
    for i in range(3):
        t = threading.Thread(target=thread_task, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

print("--- Running Threads ---")
run_threads()

# 2. Multiprocessing (CPU Bound task simulation)
def cpu_task(n):
    return sum(i * i for i in range(n))

def run_multiprocessing():
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(cpu_task, [1_000_000, 2_000_000, 3_000_000])
    return results

print("\n--- Running Multiprocessing ---")
start = time.perf_counter()
res = run_multiprocessing()
end = time.perf_counter()
print(f"Results: {res}")
print(f"Multiprocessing time: {end - start:.4f}s")

# 3. Asyncio (Cooperative I/O)
async def async_task(name, delay):
    print(f"  [Async {name}] sleeping for {delay}s")
    await asyncio.sleep(delay)
    print(f"  [Async {name}] finished")

async def run_asyncio():
    # Run tasks concurrently
    await asyncio.gather(
        async_task("A", 1),
        async_task("B", 0.5),
        async_task("C", 0.7)
    )

print("\n--- Running Asyncio ---")
asyncio.run(run_asyncio())

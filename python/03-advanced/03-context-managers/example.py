# example.py - Context Managers in Python

import contextlib

# 1. Class-based Context Manager
class TempFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print(f"--- [__enter__] Opening {self.filename}")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"--- [__exit__] Closing {self.filename}")
        self.file.close()
        if exc_type:
            print(f"      Caught error: {exc_val}")
        # Return False to let the exception propagate, True to swallow it
        return False

print("--- Using Class-based Context Manager ---")
with TempFile('test.txt') as f:
    f.write("Hello context managers!")
    # Raising an error to see if __exit__ still runs
    # 1/0 

# 2. Function-based Context Manager (@contextlib)
@contextlib.contextmanager
def simple_timer(label):
    import time
    start = time.perf_counter()
    try:
        yield  # control returns to the code inside the 'with' block
    finally:
        # Code after yield/finally runs during __exit__
        end = time.perf_counter()
        print(f"[{label}] Elapsed: {end - start:.4f}s")

print("\n--- Using @contextmanager decorator ---")
with simple_timer("Computation"):
    sum(i*i for i in range(1_000_000))

# 3. Context manager for Indentation/Output
@contextlib.contextmanager
def indented_print():
    print(">>> {")
    try:
        yield
    finally:
        print("} <<<")

with indented_print():
    print("  Inside the block")
    print("  Still inside")

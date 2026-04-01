# solution.py - Context Managers answers

import contextlib
import decimal

# TODO 1: ListBuffer
class ListBuffer:
    def __init__(self, target_list):
        self.target = target_list
        self.buffer = []

    def __enter__(self):
        return self.buffer

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.target.extend(self.buffer)
            print("Buffer committed to list.")
        else:
            print("Error detected; buffer discarded.")
        return False # let error propagate

# TODO 2: tag()
@contextlib.contextmanager
def tag(name):
    print(f"<{name}>", end="")
    yield
    print(f"</{name}>")

# TODO 3 & 4: suppress_errors
class suppress_errors:
    def __init__(self, *exceptions):
        self.exceptions = exceptions
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.exceptions)

# TODO 5: ChangingPrecision
@contextlib.contextmanager
def changing_precision(p):
    original = decimal.getcontext().prec
    decimal.getcontext().prec = p
    try:
        yield
    finally:
        decimal.getcontext().prec = original

# CHALLENGE: DatabaseTransaction
@contextlib.contextmanager
def db_transaction():
    print("BEGIN")
    try:
        yield
        print("COMMIT")
    except Exception as e:
        print(f"ROLLBACK (Reason: {e})")
        raise

# --- Verification ---
print("--- Verification ---")

print("Testing tag manager:")
with tag("h1"): print("Hello World", end="")
print()

print("\nTesting ListBuffer (success):")
mylist = [1, 2]
with ListBuffer(mylist) as b:
    b.append(3)
    b.append(4)
print(f"List after success: {mylist}")

print("\nTesting ListBuffer (failure):")
try:
    with ListBuffer(mylist) as b:
        b.append(99)
        raise ValueError("Something went wrong")
except ValueError:
    pass
print(f"List after failure: {mylist}")

print("\nTesting suppress_errors:")
with suppress_errors(ZeroDivisionError):
    res = 1 / 0
    print("This won't print")
print("Error was suppressed successfully.")

print("\n--- Why it works ---")
print("1. __enter__: Prepares the resource and optionally returns it to the 'as' variable.")
print("2. __exit__: Receives exception details. Returning True 'swallows' the error.")
print("3. @contextmanager: Converts a generator into a context manager — code before 'yield' is __enter__, after is __exit__.")
print("4. finally block: Crucial in generator managers to ensure cleanup runs even if 'yield' triggers an error.")

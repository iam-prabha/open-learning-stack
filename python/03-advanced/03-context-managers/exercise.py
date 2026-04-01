# exercise.py - Practice Context Managers

import contextlib

# TODO 1: Create a class-based context manager 'ListBuffer' that 
# accepts a list, appends items to a temporary internal list during
# the 'with' block, and ONLY extends the original list in __exit__
# if NO exception occurred.
# class ListBuffer:
#     ...

# TODO 2: Write a function-based context manager 'tag(name)' using
# @contextlib.contextmanager that prints "<name>" on enter and "</name>" on exit.
# @contextlib.contextmanager
# def tag(name):
#     ...

# TODO 3: Write a context manager 'suppress_errors(*exceptions)' that
# swallows specific exceptions provided as arguments.
# (Hint: __exit__ should return check 'exc_type' and return True/False)
# class suppress_errors:
#     ...

# TODO 4: Use your 'suppress_errors' to ignore a ZeroDivisionError.

# TODO 5: Create a context manager 'ChangingPrecision' for the 'decimal' module
# that temporarily sets a specific precision and restores it in __exit__.
# import decimal
# ...

# TODO 6: Demonstrate 'ListBuffer' failing to commit if an error occurs.

# CHALLENGE: Create a context manager 'DatabaseTransaction' that 
# prints "BEGIN", "COMMIT" on success, and "ROLLBACK" on error.

# --- Verification ---
print("--- Results ---")
try:
    # Test your code here
    pass
except Exception as e:
    print(f"Error: {e}")

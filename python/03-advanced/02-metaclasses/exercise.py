# exercise.py - Practice Metaclasses

# TODO 1: Create a class 'MyDynamicClass' dynamically using the 'type()' function.
# It should have one method 'hello()' that returns "Greetings!".
# MyDynamicClass = ...

# TODO 2: Write a metaclass 'PrefixMeta' that automatically adds a prefix "attr_"
# to all user-defined attributes in the class.
# (Hint: modify the 'attrs' dictionary in __new__)
# class PrefixMeta(type):
#     ...

# TODO 3: Create a class 'Simple' that uses PrefixMeta and define a variable 'test = 42'.
# Verify that it is accessible as 'Simple.attr_test'.
# class Simple(metaclass=PrefixMeta):
#     test = 42

# TODO 4: Write a metaclass 'Singleton' that ensures only ONE instance
# of a class can ever be created.
# (Hint: override __call__ in the metaclass to return a stored instance)
# class Singleton(type):
#     ...

# TODO 5: Create a class 'DatabaseConnection' that uses the Singleton metaclass.
# class DatabaseConnection(metaclass=Singleton):
#     ...

# TODO 6: Check if two instances of DatabaseConnection are the same object.

# CHALLENGE: Create a metaclass 'TraceMeta' that wraps all methods of a class
# to print "Entering method: {name}" before execution.

# --- Verification ---
print("--- Results ---")
try:
    # Test your code here
    pass
except NameError as e:
    print(f"Error: {e} — fill in all TODOs")
except Exception as e:
    print(f"Runtime error: {e}")

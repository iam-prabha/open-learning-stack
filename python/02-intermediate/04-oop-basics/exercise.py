# exercise.py - Practice OOP basics

# TODO 1: Create a class 'Rectangle' with attributes 'width' and 'height'.
# class Rectangle:
#     def __init__(self, width, height):
#         ...

# TODO 2: Add a method 'area()' and a method 'perimeter()' to Rectangle.

# TODO 3: Add a __str__ method that returns "Rectangle(width x height)".

# TODO 4: Create a class 'BankAccount' with attributes 'owner' and 'balance'.
# Balance should default to 0.
# class BankAccount:
#     ...

# TODO 5: Add methods 'deposit(amount)' and 'withdraw(amount)' to BankAccount.
# withdraw should raise ValueError if funds are insufficient.

# TODO 6: Add a @property 'is_empty' that returns True if balance == 0.

# CHALLENGE: Add a class method 'from_string' to BankAccount
# that parses "Alice:500" into BankAccount("Alice", 500).
# @classmethod
# def from_string(cls, data):
#     ...

# --- Verification ---
print("--- Results ---")
try:
    r = Rectangle(4, 6)
    print(f"Area: {r.area()}, Perimeter: {r.perimeter()}, Str: {r}")
    acc = BankAccount("Alice")
    acc.deposit(200)
    acc.withdraw(50)
    print(f"Balance: {acc.balance}, Empty: {acc.is_empty}")
    acc2 = BankAccount.from_string("Bob:300")
    print(f"Parsed: {acc2.owner} | {acc2.balance}")
except NameError as e:
    print(f"Error: {e} — fill in all TODOs")

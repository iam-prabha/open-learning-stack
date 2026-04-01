# solution.py - OOP basics answers

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"Insufficient funds: have {self.balance}, need {amount}")
        self.balance -= amount

    @property
    def is_empty(self):
        return self.balance == 0

    @classmethod
    def from_string(cls, data):
        # "Alice:500" -> BankAccount("Alice", 500)
        owner, amount = data.split(":")
        return cls(owner, int(amount))

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"


# --- Verification ---
r = Rectangle(4, 6)
print(f"Area: {r.area()}, Perimeter: {r.perimeter()}, Str: {r}")

acc = BankAccount("Alice")
acc.deposit(200)
acc.withdraw(50)
print(f"Balance: {acc.balance}, Empty: {acc.is_empty}")

acc2 = BankAccount.from_string("Bob:300")
print(f"Parsed: {acc2.owner} | {acc2.balance}")

print("\n--- Why it works ---")
print("1. __init__ initializes per-instance state via 'self'.")
print("2. @property makes 'is_empty' look like an attribute but computed dynamically.")
print("3. @classmethod receives 'cls' (the class itself) not 'self' — useful for factory methods.")
print("4. Default args (balance=0) allow flexible construction.")

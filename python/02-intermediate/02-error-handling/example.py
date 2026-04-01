# example.py - Error handling with try/except/else/finally

# 1. Basic try/except
print("--- Basic try/except ---")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught: division by zero!")

# 2. Multiple exception types
print("\n--- Multiple exceptions ---")
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid integer")
        return None
    except TypeError:
        print(f"Type {type(value)} cannot be converted")
        return None

safe_convert("abc")
safe_convert(None)
safe_convert("42")

# 3. else and finally
print("\n--- else / finally ---")
try:
    number = int("100")
except ValueError:
    print("Bad input")
else:
    print(f"Conversion succeeded: {number}")   # runs only if no exception
finally:
    print("This always runs (cleanup goes here)")

# 4. Raising exceptions
print("\n--- Raising exceptions ---")
def validate_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"Invalid age: {age}")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Caught: {e}")

# 5. Custom exception class
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        super().__init__(f"Cannot withdraw {amount}; balance is {balance}")
        self.amount = amount
        self.balance = balance

try:
    raise InsufficientFundsError(500, 100)
except InsufficientFundsError as e:
    print(f"\nCustom exception caught: {e}")

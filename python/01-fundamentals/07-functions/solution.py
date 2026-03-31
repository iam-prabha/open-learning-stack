# solution.py - Answers and explanations for function exercises

# TODO 1: square function
def square(n):
    return n * n

# TODO 2: is_even function
def is_even(n):
    return n % 2 == 0

# TODO 3: get_full_name function
def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

# TODO 4: calculate_tax with default parameter
def calculate_tax(price, tax_rate=0.05):
    return price * tax_rate

# TODO 5: repeat_word function
def repeat_word(word, count):
    words = [word] * count
    return " ".join(words)

# CHALLENGE: apply_operation (higher-order function)
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def apply_operation(func, a, b):
    return func(a, b)

# --- Verification ---
print("--- Verification ---")
print(f"Square of 5: {square(5)}")
print(f"Is 4 even? {is_even(4)}")
print(f"Full name: {get_full_name('Alice', 'Smith')}")
print(f"Tax for 100 (5%): {calculate_tax(100)}")
print(f"Tax for 100 (10%): {calculate_tax(100, 0.1)}")
print(f"Repeat: {repeat_word('Python', 3)}")
print(f"Apply Add (5, 10): {apply_operation(add, 5, 10)}")
print(f"Apply Multiply (5, 10): {apply_operation(multiply, 5, 10)}")

print("\n--- Why it works ---")
print("1. 'return' sends a value back to where the function was called.")
print("2. 'n % 2 == 0' is already a boolean expression, so you can return it directly.")
print("3. Default arguments (tax_rate=0.05) make the parameter optional.")
print("4. Functions in Python can be passed as arguments just like any other variable!")

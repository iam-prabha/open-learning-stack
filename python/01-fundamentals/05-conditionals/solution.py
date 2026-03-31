# solution.py - Answers and explanations for conditional exercises

# TODO 1: Positive, Negative, or Zero
number = 10
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# TODO 2: Temperature Categories
temperature = 25
if temperature >= 30:
    print("Hot")
elif temperature >= 20:   # Already checked >= 30, so this range is 20-29
    print("Warm")
else:
    print("Cold")

# TODO 3: Weekend or Holiday
is_weekend, is_holiday = True, False
if is_weekend or is_holiday:
    print("Time to relax!")

# TODO 4: Pass, Fail, or Perfect
score = 85
if score == 100:
    print("Perfect")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

# TODO 5: Ternary parity
n = 7
parity = "Even" if n % 2 == 0 else "Odd"
print(f"Number {n} is {parity}")

# CHALLENGE: Nested conditional
num = 14
if num > 0:
    if num % 2 == 0:
        print(f"{num} is positive and even")
    else:
        print(f"{num} is positive and odd")
else:
    print("Not positive")

# --- Why it works ---
print("\n--- Why it works ---")
print("1. elif is short for 'else if' - it only runs if the previous conditions were False.")
print("2. 'and' and 'or' are logical connectors that join multiple boolean expressions.")
print("3. Indentation is crucial in Python to define the code block belonging to the conditional.")
print("4. The order of conditions matters (put more specific ones like 'score == 100' first).")

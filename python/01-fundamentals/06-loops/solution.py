# solution.py - Answers and explanations for loops exercises

# TODO 1: for loop from 1 to 5
print("--- Numbers 1-5 ---")
for i in range(1, 6):
    print(i)

# TODO 2: list of colors in uppercase
print("\n--- Upper colors ---")
colors = ["red", "green", "blue"]
for color in colors:
    print(color.upper())

# TODO 3: while loop countdown
print("\n--- while countdown ---")
counter = 5
while counter >= 0:
    print(counter)
    counter -= 1

# TODO 4: Even/Odd from 1-10
print("\n--- Even/Odd ---")
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num}: Even")
    else:
        print(f"{num}: Odd")

# TODO 5: break when letter is "H"
print("\n--- break at 'H' ---")
for letter in "PYTHON":
    if letter == "H":
        break
    print(letter)

# TODO 6: Sum 1 to 100
total_sum = 0
for n in range(1, 101):
    total_sum += n
print(f"\nSum of 1-100: {total_sum}")

# CHALLENGE: 3x3 square of stars
print("\n--- 3x3 Square ---")
for i in range(3):
    for j in range(3):
        print("*", end="")
    print()  # Newline after each row

# --- Why it works ---
print("\n--- Why it works ---")
print("1. range(start, stop) goes up to but not including stop.")
print("2. end='' in print() prevents a newline.")
print("3. for loops are cleaner for known sequences; while loops are better for conditions.")
print("4. enumerate() is the Pythonic way to get both index and value (if needed).")

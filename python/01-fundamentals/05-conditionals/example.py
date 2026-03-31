# example.py - Demonstration of if, elif, and else

# 1. Basic if-else
age = 18

print("--- Basic Condition ---")
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 2. multiple branches with elif
score = 85

print("\n--- Multiple Branches ---")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 3. Nested Conditionals
is_logged_in = True
has_premium = False

print("\n--- Nested Conditions ---")
if is_logged_in:
    if has_premium:
        print("Welcome, Premium User!")
    else:
        print("Welcome, Guest User! (Upgrade for more features)")
else:
    print("Please log in to continue.")

# 4. Logical Operators in Conditionals
is_raining = True
has_umbrella = False

print("\n--- Logical AND/OR ---")
if is_raining and not has_umbrella:
    print("You should stay inside!")
elif is_raining and has_umbrella:
    print("You can go out with your umbrella.")
else:
    print("It's a beautiful day!")

# 5. Short-hand (Ternary) operator
status = "Allow" if age >= 18 else "Deny"
print(f"\nAccess: {status}")

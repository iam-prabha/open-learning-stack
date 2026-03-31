# exercise.py - Practice with lists and tuples

# TODO 1: Create a list named 'fruits' with three different fruit names.
# fruits = ...

# TODO 2: Add a new fruit to the end of the 'fruits' list using .append().
# ...

# TODO 3: Change the 2nd fruit in the list to "Mango".
# ...

# TODO 4: Create a tuple named 'dimensions' with three numbers: 1920, 1080, 60.
# dimensions = ...

# TODO 5: Use indexing to print the first fruit in your list and the last number in your tuple.
# print(f"First fruit: {fruits[...]}")
# print(f"Last dim: {dimensions[...]}")

# TODO 6: Slice the 'fruits' list to get the first TWO fruits.
# first_two = ...

# CHALLENGE: 
# Given a list of numbers: nums = [5, 10, 15, 20, 25]
# Use slicing to get the numbers in reverse order: [25, 20, 15, 10, 5]
# reversed_nums = ...

# --- Verification ---
print("--- Results ---")
# Use try-except to avoid stopping on incomplete TODOs
try:
    # Run tests here
    pass
except NameError as e:
    print(f"Error: {e} - Make sure you filled in all TODOs!")
except TypeError as e:
    print(f"Error: {e} - Remember that tuples are immutable!")

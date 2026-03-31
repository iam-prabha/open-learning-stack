# solution.py - Answers and explanations for list/tuple exercises

# TODO 1: Create a list of fruits
fruits = ["Apple", "Banana", "Cherry"]

# TODO 2: Add a fruit
fruits.append("Orange")

# TODO 3: Change the 2nd fruit (index 1)
fruits[1] = "Mango"

# TODO 4: Create a tuple
dimensions = (1920, 1080, 60)

# TODO 5: Indexing
print(f"First fruit: {fruits[0]}")
print(f"Last dimension: {dimensions[-1]}")

# TODO 6: Slicing
first_two = fruits[0:2]

# CHALLENGE: Reverse slicing
nums = [5, 10, 15, 20, 25]
reversed_nums = nums[::-1]

# --- Verification ---
print("--- Verification ---")
print(f"Fruits: {fruits}")
print(f"Dimensions: {dimensions}")
print(f"First two: {first_two}")
print(f"Numbers reversed: {reversed_nums}")

print("\n--- Why it works ---")
print("1. lists use [...] and can be modified; tuples use (...) and cannot.")
print("2. index starts at 0; -1 is an easy way to get the last item.")
print("3. slice stop index (2) is NOT included, so fruits[0:2] gets index 0 and 1.")
print("4. [::-1] works for both lists and tuples to reverse the entire sequence.")

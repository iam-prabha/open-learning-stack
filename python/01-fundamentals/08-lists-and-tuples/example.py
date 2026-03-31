# example.py - Demonstration of list and tuple operations

# 1. List Basics: Creation and Mutability
shopping_list = ["milk", "eggs", "bread"]
print("--- List Operations ---")
print(f"Original: {shopping_list}")

# Adding to a list
shopping_list.append("cheese")
print(f"Added: {shopping_list}")

# Changing an element
shopping_list[0] = "almond milk"
print(f"Changed: {shopping_list}")

# Removing from a list
removed_item = shopping_list.pop(1)  # removes index 1
print(f"Removed item: {removed_item}")
print(f"Current: {shopping_list}")

# 2. Tuple Basics: Creation and Immutability
coordinates = (10.5, 20.3)
print("\n--- Tuple Operations ---")
print(f"Current: {coordinates}")
print(f"X coordinate: {coordinates[0]}")

# Trying to change (this would fail): 
# coordinates[0] = 5.5  # raises TypeError

# 3. List and Tuple Membership
print("\n--- Membership ---")
print(f"Is 'bread' in list? {'bread' in shopping_list}")
print(f"Is 10.5 in tuple? {10.5 in coordinates}")

# 4. Concatenation and length
combined = [1, 2] + [3, 4]
print("\n--- Concatenation ---")
print(f"Combined List: {combined}")
print(f"Length: {len(combined)}")

# 5. Slicing works the same way!
numbers = [0, 1, 2, 3, 4, 5]
sub_list = numbers[1:4]  # index 1, 2, 3
print("\n--- Slicing ---")
print(f"Original: {numbers}")
print(f"Slice [1:4]: {sub_list}")

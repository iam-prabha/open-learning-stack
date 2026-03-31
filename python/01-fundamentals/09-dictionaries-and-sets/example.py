# example.py - Demonstration of dictionary and set operations

# 1. Dictionary Basics: Creation and Access
user = {
    "name": "Alice",
    "age": 30,
    "is_pro": True
}
print("--- Dictionary Operations ---")
print(f"Name: {user['name']}")
print(f"Score: {user.get('score', 0)}")  # Returns 0 if 'score' is missing

# Adding / Updating
user["age"] = 31
user["location"] = "Paris"
print(f"Updated user: {user}")

# Iterating over dictionary
print("\nIterating over keys and values:")
for key, value in user.items():
    print(f"  {key}: {value}")

# 2. Set Basics: Uniqueness
numbers = {1, 2, 2, 3, 4, 4, 5}
print("\n--- Set Operations ---")
print(f"Set (automatically deduplicated): {numbers}")

# Adding to a set
numbers.add(6)
numbers.add(1)  # Already exists, ignored
print(f"After adding 6 and 1: {numbers}")

# 3. Set Mathematics
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("\n--- Set Math ---")
print(f"Union (all unique items): {s1 | s2}")
print(f"Intersection (common items): {s1 & s2}")
print(f"Difference (in s1 but not s2): {s1 - s2}")

# 4. Converting list to set (for deduplication)
my_list = ["apple", "banana", "apple", "cherry"]
unique_list = list(set(my_list))
print("\n--- Deduplication ---")
print(f"Original list: {my_list}")
print(f"Unique list: {unique_list}")

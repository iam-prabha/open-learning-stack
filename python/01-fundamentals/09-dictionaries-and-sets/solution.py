# solution.py - Answers and explanations for dictionary/set exercises

# TODO 1: Create a dictionary
student = {
    "name": "Prabha",
    "age": 25,
    "courses": ["Math", "Python"]
}

# TODO 2: Update dictionary
student["age"] = 26
student["graduated"] = False

# TODO 3: Retrieve list of courses
course_list = student["courses"]

# TODO 4: Create sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# TODO 5: Set intersection
common_items = set_a & set_b  # {4, 5}

# TODO 6: Deduplicate list
scores = [80, 90, 80, 70, 90, 100]
unique_scores = set(scores)

# CHALLENGE: List of dictionaries (nested data)
books = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

print("\n--- Book List ---")
for book in books:
    print(f"{book['title']} by {book['author']}")

# --- Verification ---
print("\n--- Verification ---")
print(f"Student: {student}")
print(f"Intersection: {common_items}")
print(f"Unique Scores: {unique_scores}")

print("\n--- Why it works ---")
print("1. Dictionaries are key-value pairs; use student['key'] or student.get('key').")
print("2. Sets automatically remove duplicates from any input.")
print("3. Nested data structures (like a list of dictionaries) are common in real-world APIs and JSON.")
print("4. Set operators like & (intersection) and | (union) are more readable and faster than custom loops.")

# exercise.py - Practice with dictionaries and sets

# TODO 1: Create a dictionary named 'student' with:
# name: Your name
# age: Your age
# courses: ["Math", "Python"]
# student = ...

# TODO 2: Update the 'age' of your student and add a new key 'graduated' (False).
# ...

# TODO 3: Retrieve the list of 'courses' from the student dictionary.
# course_list = ...

# TODO 4: Create a set named 'set_a' with numbers {1, 2, 3, 4, 5}.
# Create a set named 'set_b' with numbers {4, 5, 6, 7, 8}.
# ...

# TODO 5: Calculate the intersection of 'set_a' and 'set_b'.
# common_items = ...

# TODO 6: Given a list with duplicates: scores = [80, 90, 80, 70, 90, 100]
# Create a set from this list to remove the duplicates.
# unique_scores = ...

# CHALLENGE: 
# Create a list of dictionaries, where each dictionary represents a book 
# with 'title' and 'author'. Loop through the list and print "TITLE by AUTHOR".
# books = [{"title": "1984", "author": "George Orwell"}, ...]
# ...

# --- Verification ---
print("--- Results ---")
# Use try-except to avoid stopping on incomplete TODOs
try:
    # Run tests here
    pass
except NameError as e:
    print(f"Error: {e} - Make sure you filled in all TODOs!")
except KeyError as e:
    print(f"Error: {e} - Make sure you are using the correct keys!")

# exercise.py - Practice with file reading and writing

# TODO 1: Create a variable 'filename' and assign it "my_notes.txt".
# filename = ...

# TODO 2: Use the 'with' statement to open the file in 'w' (write) mode.
# Write three lines:
# 1. "My favorite language is Python."
# 2. "I am learning File IO today."
# 3. "The date is 2026-03-31."
# with open(...) as f:
#     ...

# TODO 3: Open the SAME file in 'a' (append) mode.
# Add the line: "This line was appended!"
# ...

# TODO 4: Open the file in 'r' (read) mode and print the entire contents.
# ...

# TODO 5: Open the file in 'r' mode again and use a for loop to print 
# only the first 2 lines.
# (Hint: use a counter and the 'break' statement)
# ...

# TODO 6: Count the total number of words in the file.
# (Hint: Read the file, use .split() on the content, and len())
# word_count = ...

# CHALLENGE: 
# Copy the contents of "my_notes.txt" to a new file "my_notes_copy.txt".
# Ensure both files are closed properly.
# ...

# --- Verification ---
print("--- Results ---")
# Use try-except to avoid stopping on incomplete TODOs
try:
    # Run tests here
    pass
except Exception as e:
    print(f"Error: {e} - Make sure you filled in all TODOs!")

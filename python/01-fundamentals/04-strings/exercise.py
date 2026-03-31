# exercise.py - Practice with strings

# TODO 1: Create a variable 'greeting' and assign it "Hello, Python!"
# greeting = ...

# TODO 2: Calculate the length of 'greeting' using the len() function.
# length = ...

# TODO 3: Extract the word "Python" from the 'greeting' string using slicing.
# python_word = ...

# TODO 4: Create a new string 'shout' that is the uppercase version of 'greeting'.
# shout = ...

# TODO 5: Replace "Hello" with "Welcome" in the 'greeting' string.
# (Note: Strings are immutable, so you must create a new variable).
# welcome = ...

# TODO 6: Use an f-string to create a message: "The length of '{greeting}' is {length}."
# message = ...

# CHALLENGE: 
# Reverse the 'greeting' string using slicing (the [::-1] trick).
# reversed_greeting = ...

# --- Verification ---
print("--- Results ---")
try:
    print(f"Greeting: {greeting}")
    print(f"Length: {length}")
    print(f"Python word: {python_word}")
    print(f"Shout: {shout}")
    print(f"Welcome: {welcome}")
    print(f"Message: {message}")
    print(f"Reversed: {reversed_greeting}")
except NameError as e:
    print(f"Error: {e} - Make sure you filled in all TODOs!")

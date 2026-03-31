# solution.py - Answers and explanations for string exercises

# TODO 1: Create a variable 'greeting' and assign it "Hello, Python!"
greeting = "Hello, Python!"

# TODO 2: Calculate the length of 'greeting' using the len() function.
length = len(greeting)

# TODO 3: Extract the word "Python" from the 'greeting' string using slicing.
# "Hello, " is 7 chars (0-6). "Python" starts at index 7 and ends at 12.
# So slice is [7:13] (stop index 13 is not included).
python_word = greeting[7:13]

# TODO 4: Create a new string 'shout' that is the uppercase version of 'greeting'.
shout = greeting.upper()

# TODO 5: Replace "Hello" with "Welcome" in the 'greeting' string.
welcome = greeting.replace("Hello", "Welcome")

# TODO 6: Use an f-string to create a message: "The length of '{greeting}' is {length}."
message = f"The length of '{greeting}' is {length}."

# CHALLENGE: Reverse the 'greeting' string using slicing.
reversed_greeting = greeting[::-1]

# --- Verification ---
print("--- Verification ---")
print(f"Greeting: {greeting}")
print(f"Length: {length}")
print(f"Python word: {python_word}")
print(f"Shout: {shout}")
print(f"Welcome: {welcome}")
print(f"Message: {message}")
print(f"Reversed: {reversed_greeting}")

print("\n--- Why it works ---")
print("1. slicing format is [start:stop:step].")
print("2. string methods (upper, replace) return a NEW string, they don't change the original.")
print("3. negative index starts from the end (-1 is the last char).")
print("4. [::-1] reversed the string because we step backward through the entire sequence.")

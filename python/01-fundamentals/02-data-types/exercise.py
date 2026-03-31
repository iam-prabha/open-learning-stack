"""
Data Types — Exercises
======================
Run: python exercise.py (after filling in the TODOs)

6 exercises + 1 challenge. Each has assert statements
that verify your answer. Fill in every TODO, then run
the file — you should see "All exercises passed! 🎉"
"""


# ── Exercise 1: Type identification ─────────────────────────────────
# TODO: For each value below, assign the correct type NAME as a string.
# Example: type_of_42 = "int"
# Hint: use type() in a REPL if unsure.

type_of_42 = ...          # What type is 42?
type_of_3_14 = ...        # What type is 3.14?
type_of_hello = ...       # What type is "hello"?
type_of_true = ...        # What type is True?
type_of_none = ...        # What type is None?

assert type_of_42 == "int", f"Expected 'int', got '{type_of_42}'"
assert type_of_3_14 == "float", f"Expected 'float', got '{type_of_3_14}'"
assert type_of_hello == "str", f"Expected 'str', got '{type_of_hello}'"
assert type_of_true == "bool", f"Expected 'bool', got '{type_of_true}'"
assert type_of_none == "NoneType", f"Expected 'NoneType', got '{type_of_none}'"
print("✓ Exercise 1 passed")


# ── Exercise 2: Type conversion ─────────────────────────────────────
# TODO: Convert the given values to the target types.
# Hint: int(), float(), str(), bool() are your conversion functions.

string_number = "256"
converted_int = ...           # Convert string_number to int

float_number = 9.99
converted_str = ...           # Convert float_number to str

int_number = 0
converted_bool = ...          # Convert int_number to bool

assert converted_int == 256, f"Expected 256, got {converted_int}"
assert isinstance(converted_int, int), "Should be int type"
assert converted_str == "9.99", f"Expected '9.99', got '{converted_str}'"
assert isinstance(converted_str, str), "Should be str type"
assert converted_bool is False, f"Expected False, got {converted_bool}"
assert isinstance(converted_bool, bool), "Should be bool type"
print("✓ Exercise 2 passed")


# ── Exercise 3: List operations ──────────────────────────────────────
# TODO: Perform the following operations on the list.
# Hint: look up append(), remove(), and list slicing.

colors = ["red", "green", "blue"]

# 3a: Add "yellow" to the end of the list
...

# 3b: Remove "green" from the list
...

# 3c: Create a new variable `first_two` containing only the first 2 items
first_two = ...

assert colors == ["red", "blue", "yellow"], f"Expected ['red', 'blue', 'yellow'], got {colors}"
assert first_two == ["red", "blue"], f"Expected ['red', 'blue'], got {first_two}"
print("✓ Exercise 3 passed")


# ── Exercise 4: Dictionary building ─────────────────────────────────
# TODO: Build a dictionary called `student` with the given keys and values.
# Then retrieve a value using .get() with a default.
# Hint: {"key": value, ...} and dict.get(key, default)

# 4a: Create a dict with keys "name" (str), "age" (int), "grades" (list)
student = ...  # name="Alice", age=20, grades=[85, 92, 78]

# 4b: Use .get() to retrieve "email" with default "N/A"
email = ...

assert student["name"] == "Alice", f"Expected 'Alice', got {student['name']}"
assert student["age"] == 20, f"Expected 20, got {student['age']}"
assert student["grades"] == [85, 92, 78], f"Grades don't match"
assert isinstance(student, dict), "student should be a dict"
assert email == "N/A", f"Expected 'N/A', got '{email}'"
print("✓ Exercise 4 passed")


# ── Exercise 5: Set operations ───────────────────────────────────────
# TODO: Use set operations to solve these.
# Hint: use | for union, & for intersection, - for difference.

frontend = {"html", "css", "javascript", "react"}
backend = {"python", "javascript", "sql", "docker"}

# 5a: Find skills that appear in BOTH sets
common_skills = ...

# 5b: Find ALL unique skills across both sets
all_skills = ...

# 5c: Find skills ONLY in frontend (not in backend)
frontend_only = ...

assert common_skills == {"javascript"}, f"Expected {{'javascript'}}, got {common_skills}"
assert all_skills == {"html", "css", "javascript", "react", "python", "sql", "docker"}, f"all_skills mismatch"
assert frontend_only == {"html", "css", "react"}, f"Expected {{'html', 'css', 'react'}}, got {frontend_only}"
print("✓ Exercise 5 passed")


# ── Exercise 6: Tuple unpacking ──────────────────────────────────────
# TODO: Unpack the tuple and create a formatted string.
# Hint: a, b, c = some_tuple and f-strings.

user_record = ("Prabha", 25, "prabha@example.com")

# 6a: Unpack into three variables: name, age, email
...  # Replace with unpacking

# 6b: Create a formatted string: "Prabha (25) — prabha@example.com"
formatted = ...

assert name == "Prabha", f"Expected 'Prabha', got '{name}'"
assert age == 25, f"Expected 25, got {age}"
assert email == "prabha@example.com", f"Expected 'prabha@example.com', got '{email}'"
assert formatted == "Prabha (25) — prabha@example.com", f"Formatted string doesn't match"
print("✓ Exercise 6 passed")


# ── Challenge: Type-safe config parser ───────────────────────────────
# TODO: Build a function that converts a flat "config" dictionary
# with string values into properly typed values.
#
# Rules:
#   - "true"/"false" (case-insensitive) → bool
#   - Strings that look like integers (e.g. "42") → int
#   - Strings that look like floats (e.g. "3.14") → float
#   - Everything else stays as str
#   - Return a NEW dictionary (don't mutate the input)
#
# Hint: str.lower(), str.isdigit(), try/except float()

def parse_config(raw_config):
    """Convert string values to their proper Python types."""
    ...  # Your implementation here


raw = {
    "debug": "True",
    "max_retries": "5",
    "timeout": "30.5",
    "app_name": "my-app",
    "verbose": "false",
}

parsed = parse_config(raw)

assert parsed["debug"] is True, f"Expected True, got {parsed['debug']}"
assert parsed["max_retries"] == 5, f"Expected 5, got {parsed['max_retries']}"
assert isinstance(parsed["max_retries"], int), "max_retries should be int"
assert parsed["timeout"] == 30.5, f"Expected 30.5, got {parsed['timeout']}"
assert isinstance(parsed["timeout"], float), "timeout should be float"
assert parsed["app_name"] == "my-app", f"Expected 'my-app', got {parsed['app_name']}"
assert parsed["verbose"] is False, f"Expected False, got {parsed['verbose']}"

# Verify original dict was NOT mutated
assert raw["debug"] == "True", "Original dict should not be mutated"
print("✓ Challenge passed")


print("\n🎉 All exercises passed!")

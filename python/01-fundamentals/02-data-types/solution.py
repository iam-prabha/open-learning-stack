"""
Data Types — Solutions
======================
Run: python solution.py

Complete answers for all 6 exercises + 1 challenge.
Each answer includes a WHY comment and alternatives.
"""


# ── Solution 1: Type identification ──────────────────────────────────
# WHY: Python's type names match their constructor functions — knowing
# the exact name helps when reading error messages and documentation.

type_of_42 = "int"
type_of_3_14 = "float"
type_of_hello = "str"
type_of_true = "bool"
type_of_none = "NoneType"

# ALTERNATIVE: You could discover these programmatically:
# type_of_42 = type(42).__name__  # Returns "int"

assert type_of_42 == "int"
assert type_of_3_14 == "float"
assert type_of_hello == "str"
assert type_of_true == "bool"
assert type_of_none == "NoneType"
print("✓ Exercise 1 passed")


# ── Solution 2: Type conversion ──────────────────────────────────────
# WHY: Explicit conversion prevents subtle bugs — Python never
# implicitly converts between str and numeric types.

string_number = "256"
converted_int = int(string_number)

float_number = 9.99
converted_str = str(float_number)

int_number = 0
converted_bool = bool(int_number)
# WHY bool(0) is False: zero is "falsy" in Python — any zero-like value
# (0, 0.0, "", [], None) converts to False.

# ALTERNATIVE: For int→bool, you can also use `not not int_number`,
# but bool() is far more readable.

assert converted_int == 256
assert isinstance(converted_int, int)
assert converted_str == "9.99"
assert isinstance(converted_str, str)
assert converted_bool is False
assert isinstance(converted_bool, bool)
print("✓ Exercise 2 passed")


# ── Solution 3: List operations ──────────────────────────────────────
# WHY: Lists are Python's workhorse collection — learning append,
# remove, and slicing covers 80% of daily list work.

colors = ["red", "green", "blue"]

# 3a: append() adds to the end in O(1) amortized time
colors.append("yellow")

# 3b: remove() finds and removes the first occurrence
colors.remove("green")

# 3c: Slicing creates a NEW list — original is untouched
first_two = colors[:2]

# ALTERNATIVE for 3b: You could also use `del colors[1]` to remove by
# index, or `colors.pop(1)` to remove by index AND get the value back.

assert colors == ["red", "blue", "yellow"]
assert first_two == ["red", "blue"]
print("✓ Exercise 3 passed")


# ── Solution 4: Dictionary building ─────────────────────────────────
# WHY: Dicts are Python's most-used data structure for structured data.
# .get() with a default is safer than bracket access for optional keys.

student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 92, 78],
}

email = student.get("email", "N/A")
# WHY .get(): bracket access raises KeyError if key is missing,
# but .get() returns the default value — no crash, no try/except.

# ALTERNATIVE: You could use `student.setdefault("email", "N/A")`,
# which also INSERTS the default into the dict if missing.

assert student["name"] == "Alice"
assert student["age"] == 20
assert student["grades"] == [85, 92, 78]
assert isinstance(student, dict)
assert email == "N/A"
print("✓ Exercise 4 passed")


# ── Solution 5: Set operations ───────────────────────────────────────
# WHY: Set operations (union, intersection, difference) are O(min(n,m))
# and far cleaner than manual loops with if-checks.

frontend = {"html", "css", "javascript", "react"}
backend = {"python", "javascript", "sql", "docker"}

common_skills = frontend & backend
all_skills = frontend | backend
frontend_only = frontend - backend

# ALTERNATIVE: You can use method syntax instead of operators:
# common_skills = frontend.intersection(backend)
# all_skills = frontend.union(backend)
# frontend_only = frontend.difference(backend)
# Method syntax is more readable when chaining multiple operations.

assert common_skills == {"javascript"}
assert all_skills == {"html", "css", "javascript", "react", "python", "sql", "docker"}
assert frontend_only == {"html", "css", "react"}
print("✓ Exercise 5 passed")


# ── Solution 6: Tuple unpacking ──────────────────────────────────────
# WHY: Tuple unpacking gives meaningful names to positional data,
# making code self-documenting instead of using record[0], record[1].

user_record = ("Prabha", 25, "prabha@example.com")

name, age, email = user_record

formatted = f"{name} ({age}) — {email}"

# ALTERNATIVE: For more complex records, consider using
# collections.namedtuple or dataclasses instead of plain tuples:
# from collections import namedtuple
# User = namedtuple("User", ["name", "age", "email"])
# user = User(*user_record)
# formatted = f"{user.name} ({user.age}) — {user.email}"

assert name == "Prabha"
assert age == 25
assert email == "prabha@example.com"
assert formatted == "Prabha (25) — prabha@example.com"
print("✓ Exercise 6 passed")


# ── Challenge Solution: Type-safe config parser ──────────────────────
# WHY: Real-world configs (env vars, .ini files, CLI args) are always
# strings. A parser like this avoids scattered int()/bool() calls.

def parse_config(raw_config):
    """Convert string values to their proper Python types."""
    result = {}
    for key, value in raw_config.items():
        # WHY check bool first: "true".isdigit() is False, but we want
        # to catch it before the int/float checks for clarity.
        if value.lower() in ("true", "false"):
            result[key] = value.lower() == "true"
        else:
            # WHY try int before float: every int is a valid float,
            # so we try the more specific type first.
            try:
                result[key] = int(value)
            except ValueError:
                try:
                    result[key] = float(value)
                except ValueError:
                    result[key] = value
    return result


# ALTERNATIVE approach using a dispatch pattern:
# def parse_value(value):
#     if value.lower() in ("true", "false"):
#         return value.lower() == "true"
#     for converter in (int, float):
#         try:
#             return converter(value)
#         except ValueError:
#             continue
#     return value
#
# def parse_config_alt(raw_config):
#     return {k: parse_value(v) for k, v in raw_config.items()}

raw = {
    "debug": "True",
    "max_retries": "5",
    "timeout": "30.5",
    "app_name": "my-app",
    "verbose": "false",
}

parsed = parse_config(raw)

assert parsed["debug"] is True
assert parsed["max_retries"] == 5
assert isinstance(parsed["max_retries"], int)
assert parsed["timeout"] == 30.5
assert isinstance(parsed["timeout"], float)
assert parsed["app_name"] == "my-app"
assert parsed["verbose"] is False
assert raw["debug"] == "True"
print("✓ Challenge passed")


# ─── KEY TAKEAWAYS ───────────────────────────────────────────────────
#
# 1. Python has 9 core built-in types: int, float, str, bool,
#    list, tuple, dict, set, NoneType — master these first.
#
# 2. Use explicit conversion (int(), str(), float(), bool()) —
#    Python does NOT auto-convert between strings and numbers.
#
# 3. Use `is` for None/True/False comparisons, `==` for values.
#
# 4. Choose the right container: list (ordered, mutable),
#    tuple (ordered, immutable), dict (key-value), set (unique).
#
# 5. Floats are NOT exact (IEEE 754) — use math.isclose() or
#    decimal.Decimal when precision matters.
#
# Next topic: 03-operators
# ─────────────────────────────────────────────────────────────────────

print("\n🎉 All exercises passed!")

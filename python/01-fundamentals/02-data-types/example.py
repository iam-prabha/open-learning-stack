"""
Data Types in Python — Complete Working Demo
=============================================
Run: python example.py

Covers: int, float, str, bool, list, tuple, dict, set, NoneType
"""


# ─── SECTION: Integers (int) ────────────────────────────────────────

# WHY int: Use for counting, indexing, and any value without decimals.
age = 25
negative_count = -3
hex_value = 0xFF        # WHY hex: useful for colors, memory addresses
binary_value = 0b1010   # WHY binary: useful for bitwise flags

# WHY type(): confirms the runtime type — Python is dynamically typed
print(f"age = {age}, type = {type(age)}")
print(f"hex 0xFF = {hex_value}, binary 0b1010 = {binary_value}")

# WHY: Python ints have unlimited precision — no overflow unlike C/Java
big_number = 10 ** 100
print(f"10^100 has {len(str(big_number))} digits — no overflow!")


# ─── SECTION: Floats (float) ────────────────────────────────────────

# WHY float: Use for measurements, percentages, and scientific values.
temperature = 36.6
pi = 3.14159
scientific = 2.5e-3    # WHY: scientific notation for very small/large values

print(f"\ntemperature = {temperature}, pi = {pi}")
print(f"2.5e-3 = {scientific}")

# WHY this warning: floats use IEEE 754 — they are NOT exact
print(f"0.1 + 0.2 = {0.1 + 0.2}  (not exactly 0.3!)")


# ─── SECTION: Strings (str) ─────────────────────────────────────────

# WHY str: Python's text type — immutable sequence of Unicode characters.
name = "Prabha"
greeting = f"Hello, {name}!"     # WHY f-string: cleanest way to embed values
multiline = """Line one
Line two"""

print(f"\n{greeting}")
print(f"Name length: {len(name)}")
print(f"Uppercase: {name.upper()}")
print(f"Starts with 'P': {name.startswith('P')}")

# WHY slicing: strings are sequences — you can extract parts by index
print(f"First 3 chars: {name[:3]}")


# ─── SECTION: Booleans (bool) ────────────────────────────────────────

# WHY bool: Two-value type for conditions and flags.
is_active = True
is_admin = False

# WHY: bool is a subclass of int → True==1, False==0
print(f"\nTrue + True = {True + True}")
print(f"is_active and is_admin = {is_active and is_admin}")

# WHY: these are all "falsy" — they evaluate to False in conditions
falsy_values = [0, 0.0, "", [], {}, set(), None, False]
print(f"All falsy: {all(not v for v in falsy_values)}")


# ─── SECTION: Lists (list) ───────────────────────────────────────────

# WHY list: ordered, mutable collection — your go-to general container.
fruits = ["apple", "banana", "cherry"]
fruits.append("date")         # WHY append: adds to end in O(1)
fruits[1] = "blueberry"       # WHY: lists are mutable — direct index assignment

print(f"\nfruits = {fruits}")
print(f"Length: {len(fruits)}, First: {fruits[0]}, Last: {fruits[-1]}")

# WHY list comprehension: concise way to transform/filter lists
squares = [x ** 2 for x in range(5)]
print(f"Squares: {squares}")


# ─── SECTION: Tuples (tuple) ─────────────────────────────────────────

# WHY tuple: immutable ordered sequence — use for fixed records.
coordinates = (10.0, 20.0)
rgb_red = (255, 0, 0)

# WHY unpacking: extract tuple values into named variables for clarity
x, y = coordinates
print(f"\nCoordinates: x={x}, y={y}")

# WHY tuples as dict keys: they're hashable (lists are NOT)
locations = {(0, 0): "origin", (1, 1): "diagonal"}
print(f"Location at (0,0): {locations[(0, 0)]}")


# ─── SECTION: Dictionaries (dict) ────────────────────────────────────

# WHY dict: key-value mapping — O(1) lookups by key.
person = {
    "name": "Prabha",
    "age": 25,
    "skills": ["Python", "ML"],
}

print(f"\nPerson: {person}")
print(f"Name: {person['name']}")

# WHY .get(): returns None instead of raising KeyError for missing keys
print(f"Email: {person.get('email', 'not set')}")

# WHY: iterate keys, values, or both
for key, value in person.items():
    print(f"  {key}: {value}")


# ─── SECTION: Sets (set) ─────────────────────────────────────────────

# WHY set: unordered collection of unique items — fast membership checks.
unique_numbers = {1, 2, 3, 2, 1}  # WHY: duplicates auto-removed
print(f"\nSet from {{1,2,3,2,1}}: {unique_numbers}")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference: {a - b}")

# WHY: set for deduplication is idiomatic Python
names = ["alice", "bob", "alice", "charlie", "bob"]
unique_names = list(set(names))
print(f"Unique names: {unique_names}")


# ─── SECTION: NoneType ───────────────────────────────────────────────

# WHY None: represents "no value" — use for optional returns and defaults.
result = None
print(f"\nresult is None: {result is None}")

# WHY `is None` not `== None`: identity check is safer and faster
def find_user(user_id):
    """Returns None when user not found — caller must check."""
    users = {1: "Prabha", 2: "Alice"}
    return users.get(user_id)

user = find_user(99)
if user is None:
    print("User not found — None returned")


# ─── SECTION: Type Checking & Conversion ─────────────────────────────

# WHY isinstance(): preferred over type() == because it handles inheritance
print(f"\nisinstance(42, int): {isinstance(42, int)}")
print(f"isinstance(True, int): {isinstance(True, int)}")  # bool IS int

# WHY conversion: user input is always str — you must convert explicitly
age_str = "30"
age_int = int(age_str)
price_str = "19.99"
price_float = float(price_str)
print(f"Converted: '{age_str}' → {age_int}, '{price_str}' → {price_float}")

print("\n✅ All examples ran successfully!")

# Data Types

## What is it?

Every value in Python has a **type** that determines what operations you can perform on it. Python is dynamically typed — you don't declare types, but every value *is* a specific type at runtime. The built-in types (`int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`, `NoneType`) cover the vast majority of everyday programming.

## Real-world analogy

Think of data types like different kinds of containers in a kitchen. A measuring cup (float) holds liquids with precision. A counting jar (int) holds whole marbles. A label maker (str) produces text. A light switch (bool) is either on or off. A shopping bag (list) holds items in order and you can swap things in and out. A sealed envelope (tuple) holds items you shouldn't change. A filing cabinet (dict) lets you look things up by label. A marble bag (set) holds unique marbles with no duplicates.

## When to use it

| Use when... | Avoid when... |
|---|---|
| `int` — counting, indexing, IDs | You need decimal precision (use `float` or `Decimal`) |
| `float` — measurements, percentages, scientific values | You need exact currency math (use `decimal.Decimal`) |
| `str` — text, labels, user input, file paths | You need a single character type (Python has no `char`) |
| `bool` — flags, conditions, toggles | You need tri-state logic (use an enum instead) |
| `list` — ordered, mutable collections | You need immutability (use `tuple`) |
| `tuple` — fixed records, dictionary keys, function returns | You need to add/remove items (use `list`) |
| `dict` — key-value lookups, JSON-like data, config | You need ordered insertion *and* don't use Python 3.7+ |
| `set` — unique items, membership checks, deduplication | You need to preserve insertion order (use `dict.fromkeys`) |
| `None` — representing "no value", optional returns | You need a falsy placeholder with meaning (use `0` or `""`) |

## Common mistakes

1. **Confusing `==` with `is`** — `==` checks value equality; `is` checks identity (same object in memory). Use `is` only for `None`, `True`, `False`.
2. **Mutating a default list argument** — `def f(items=[])` shares one list across all calls. Use `def f(items=None)` and create inside.
3. **Assuming `float` is exact** — `0.1 + 0.2 != 0.3` due to IEEE 754. Use `math.isclose()` for comparisons.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of all 9 built-in types — read and run |
| `exercise.py` | 6 TODOs + 1 challenge — test your understanding |
| `solution.py` | Complete answers with WHY comments |

## Go deeper

- [Python Built-in Types — Official Docs](https://docs.python.org/3/library/stdtypes.html)
- [Python Data Model — Official Docs](https://docs.python.org/3/reference/datamodel.html)

# Dictionaries and Sets

## What is it?

Dictionaries and sets are unordered collections in Python that use curly braces `{...}`. A **dictionary** stores data as key-value pairs (`key: value`), while a **set** stores only unique values.

## Real-world analogy

Think of a **dictionary** like a real **language dictionary**: You look up a "word" (key) to find its "definition" (value). Every word in the dictionary is unique, but several words might have the same definition.

Think of a **set** like a **bag of unique marbles**. If you try to put a second "blue marble" in the bag, it won't work—the bag only cares about which *kinds* of marbles are inside, not how many of each you have.

## When to use it

| Feature | Dictionary (`{k: v}`) | Set (`{v}`) |
|---|---|---|
| **Structure** | Key-Value pairs | Only values (unique) |
| **Lookup Speed** | Extremely fast (O(1)) | Extremely fast (O(1)) |
| **Common Use** | Mapping data (e.g., user profiles, word counts) | Deduplicating lists, membership testing, math operations (union/intersection) |
| **Methods** | `get()`, `keys()`, `values()`, `items()` | `add()`, `remove()`, `union()`, `intersection()` |

## Common mistakes

1. **Accessing a non-existent key** — `my_dict["missing"]` will raise a `KeyError`. Use `my_dict.get("missing")` which returns `None` instead.
2. **Tuples vs. Dictionaries** — Both can use curly braces (sets too!). Remember: `{}` is an empty *dictionary*. Use `set()` for an empty set.
3. **Mutable keys** — You cannot use a list as a dictionary key or in a set because keys must be "hashable" (immutable).
4. **Duplicate set items** — Python won't throw an error if you add a duplicate to a set; it will just ignore it.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of dictionary lookups and set operations |
| `exercise.py` | 6 TODOs + 1 challenge on mapping and unique items |
| `solution.py` | Answers with explanations for nested dictionaries and set math |

## Go deeper

- [Dictionaries — Official Docs](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Sets — Official Docs](https://docs.python.org/3/tutorial/datastructures.html#sets)

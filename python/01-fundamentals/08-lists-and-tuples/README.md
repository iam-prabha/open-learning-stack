# Lists and Tuples

## What is it?

Lists and tuples are sequences used to store collections of data in a single variable. A **list** is mutable (it can be changed after creation) and defined using square brackets `[...]`. A **tuple** is immutable (it cannot be changed) and defined using parentheses `(...)`.

## Real-world analogy

Think of a **list** like a **shopping list** written on a notepad: "Buy milk, eggs, bread." If you realize you have enough bread, you can cross it off and add "Buy cheese" instead. It’s flexible.

Think of a **tuple** like a **sealed document**: "Date of birth, Place of birth, Name." Once written and sealed, you cannot change the information without making a completely new document. It’s permanent and secure.

## When to use it

| Feature | Lists (`[]`) | Tuples (`()`) |
|---|---|---|
| **Mutability** | Mutable (can change) | Immutable (cannot change) |
| **Performance** | Slightly slower for large data | Slightly faster (uses less memory) |
| **Common Use** | Ordered, changeable items (players, items in a cart) | Fixed records (coordinates, database results, constant data) |
| **Methods** | Many (append, remove, pop, sort) | Few (count, index) |

## Common mistakes

1. **Confusing list and tuple syntax** — Use `[]` for lists and `()` for tuples.
2. **Trying to change a tuple** — `my_tuple[0] = 5` will raise a `TypeError`.
3. **Omitting the comma for a single-item tuple** — `(5)` is an integer; `(5,)` is a tuple of length 1.
4. **Lists as dictionary keys** — You cannot use a list as a dictionary key because it’s mutable. Use a tuple instead!

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of list manipulation and tuple basics |
| `exercise.py` | 6 TODOs + 1 challenge on collection operations |
| `solution.py` | Answers with explanations for list methods and slicing |

## Go deeper

- [Python Data Structures (Lists) — Official Docs](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Tuples and Sequences — Official Docs](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

# Strings

## What is it?

Strings are sequences of characters used to represent text in Python. You can create a string by enclosing characters in single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` or `"""..."""`) for multi-line text.

## Real-world analogy

Think of a string as a **beaded necklace**. Each bead is a character (a letter, number, space, or symbol), and they are strung together in a specific order. You can ask for the 3rd bead, you can cut the necklace (slicing), or you can join two necklaces together (concatenation).

## When to use it

| Use when... | Avoid when... |
|---|---|
| You need to display text to the user | You should be using a numeric type for calculations |
| You are reading from or writing to a text file | You are dealing with binary data (use `bytes`) |
| You need to represent identifiers, labels, or names | You need a single character (Python has no separate `char` type; it's just a string of length 1) |

## Common mistakes

1. **Forgetting quotes** — `name = Alice` will fail because Python looks for a variable named `Alice`. Use `name = "Alice"`.
2. **Off-by-one errors** — String indexing starts at `0`. The 1st character is `s[0]`, not `s[1]`.
3. **Strings are immutable** — You cannot change a character in a string directly (e.g., `s[0] = 'H'` fails). You must create a new string.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of concatenation, slicing, and string methods |
| `exercise.py` | 6 TODOs + 1 challenge on text manipulation |
| `solution.py` | Answers with explanations for f-strings and slicing |

## Go deeper

- [Python String Methods — Official Docs](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Common String Operations — Official Docs](https://docs.python.org/3/library/string.html)

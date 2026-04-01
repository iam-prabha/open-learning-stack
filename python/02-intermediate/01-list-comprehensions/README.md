# List Comprehensions

## What is it?

A list comprehension is a concise, Pythonic way to create a new list by applying an expression to each item in an existing iterable, optionally filtering items with a condition. It replaces multi-line `for` loops with a single line of expressive code.

## Real-world analogy

Think of a list comprehension like a **filter coffee machine**. You pour in raw ingredients (the source iterable), the filter applies a rule (the condition), and out comes a clean, transformed result (the new list) — all in one step. A classic `for` loop is like manually doing each step one at a time.

## When to use it

| Use when... | Avoid when... |
|---|---|
| You are building a new list from another sequence | The logic is complex enough to require multiple statements |
| The transformation is simple (one expression) | You need side effects only (no returned list) — use a plain `for` loop |
| Readability stays high (fits in one line) | Nesting more than 2 levels deep — it becomes unreadable |

## Common mistakes

1. **Forgetting the brackets** — `x*2 for x in nums` is a generator expression. You need `[x*2 for x in nums]` for a list.
2. **Over-nesting** — Deeply nested list comprehensions are hard to read. Break them into separate steps.
3. **Using them for side effects** — `[print(x) for x in items]` works but is poor style. Use a `for` loop instead.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of filtering, transforming, and nesting |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with explanations |

## Go deeper

- [List Comprehensions — Official Docs](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [PEP 202 — List Comprehensions](https://peps.python.org/pep-0202/)

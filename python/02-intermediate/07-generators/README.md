# Generators

## What is it?

A generator is a special type of function that **yields** values one at a time instead of returning them all at once. When you call a generator function, it returns a **generator object** that you can iterate over. Each call to `next()` resumes the function until the next `yield` statement. Generators are **lazy** — they compute values only when needed, making them memory-efficient for large or infinite sequences.

## Real-world analogy

Think of a generator like a **vending machine**. You don't get all the snacks at once. You insert a coin, get one snack (`yield`), then the machine waits. Next coin → next snack. The machine only produces when asked. Compare this to a list which is like a tray — all snacks prepared upfront.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Working with large or infinite sequences (file lines, sensor data) | You need random access to elements by index |
| You want to build data pipelines (chain generators together) | The sequence is small and fits comfortably in memory |
| Memory is constrained and compute-as-you-go is viable | You need to iterate multiple times over the same data |

## Common mistakes

1. **Generators are consumed once** — After iterating, the generator is exhausted. You must re-create it.
2. **Confusing `yield` with `return`** — `return` in a generator raises `StopIteration`; `yield` pauses and sends a value.
3. **Forgetting `()` for generator expressions** — `(x*2 for x in nums)` is a generator; `[x*2 for x in nums]` is a list.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | `yield`, generator expressions, chaining generators |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Generators — Official Docs](https://docs.python.org/3/tutorial/classes.html#generators)
- [PEP 255 — Simple Generators](https://peps.python.org/pep-0255/)

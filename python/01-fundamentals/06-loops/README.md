# Loops

## What is it?

Loops allow you to execute a block of code multiple times. Python provides two main types of loops: `for` loops (used for iterating over a sequence like a list or range) and `while` loops (used to repeat code as long as a condition is true).

## Real-world analogy

Think of a loop as a **repetitive task**. A `for` loop is like reading a book: "For every page in the book, read the page." You know exactly when you'll finish. A `while` loop is like waiting for a bus: "While the bus has not arrived, stay at the bus stop and watch the road." You don't know how many times you'll look until the bus appears!

## When to use it

| Type | Use when... | Example |
|---|---|---|
| **for** | You have a sequence or a fixed number of items to iterate over | `for student in class_list:` |
| **while** | You don't know how many times to repeat, but you have a condition | `while user_input != "quit":` |
| **range()** | You need to loop a specific number of times | `for i in range(5):` |

## Common mistakes

1. **Infinite loops** — A `while` loop whose condition never becomes `False` (e.g., `while True:` without a `break`).
2. **Off-by-one errors with range()** — `range(5)` gives you 0, 1, 2, 3, 4 (it starts at 0 and stops *before* 5).
3. **Modifying a list while looping over it** — This can cause unexpected behavior. Always iterate over a copy of the list if you need to mutate it.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of for loops, while loops, and range() |
| `exercise.py` | 6 TODOs + 1 challenge on iteration and breaking loops |
| `solution.py` | Answers with explanations for nested loops and loop control |

## Go deeper

- [Python Control Flow (Loops) — Official Docs](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [The range() Function — Official Docs](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

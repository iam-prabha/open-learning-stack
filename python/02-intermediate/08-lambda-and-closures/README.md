# Lambda and Closures

## What is it?

**Lambda functions** are small, anonymous one-line functions defined without a name using the `lambda` keyword. They are restricted to a single expression.

**Closures** are function objects that remember values in enclosing scopes even if they are no longer in memory. A closure "closes over" the local variables of an outer function.

## Real-world analogy

Think of a **lambda** like a **post-it note** with a single instruction (e.g., "Add 5"). You use it once for a specific task and throw it away. A named function is like a **user manual** stored on a shelf.

Think of a **closure** like a **personal assistant** who remembers your specific preferences (like how you take your coffee) even after the initial meeting is over. The assistant "captures" those details for later use.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Lambda** | Passing simple logic to `sort()`, `filter()`, or `map()` | The logic is more than one expression or spans multiple lines |
| **Closure** | You need to "factory-produce" functions with preset data | A simple class with `__call__` would be more readable |

## Common mistakes

1. **Overusing lambdas** — If a lambda is hard to read, give it a name with `def`.
2. **Late binding in closures** — Python closures bind variables, not values. Be careful when creating closures in loops (use default arguments to snap the current value).
3. **Trying to write multiple statements in lambda** — Lambdas can only contain a single expression.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Basic lambda usage, sorting, simple closures, nonlocal keyword |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Lambda Expressions — Official Docs](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Closures in Python — Real Python](https://realpython.com/python-closure/)

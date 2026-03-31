# Functions

## What is it?

Functions are reusable blocks of code that perform a specific task. They allow you to write logic once and call it multiple times, which makes your code cleaner, more modular, and easier to debug. In Python, you define a function using the `def` keyword.

## Real-world analogy

Think of a function as a **recipe**. The name of the function is the name of the dish (e.g., `make_cake`). The **parameters** are the ingredients (flour, eggs, sugar). When you call the function, you are "cooking" the recipe with specific values. The **return value** is the final cake that you get at the end. You can reuse the recipe with different ingredients to get different cakes.

## When to use it

| Use when... | Avoid when... |
|---|---|
| You find yourself writing the same code more than twice | The code is only one line and used once (don't over-engineer) |
| You want to break a complex problem into smaller, manageable parts | The function name doesn't clearly describe what it does |
| You need to perform a calculation or action that returns a result | You are just grouping unrelated code together (use modules instead) |

## Common mistakes

1. **Forgetting to return** — A function without a `return` statement will return `None` by default.
2. **Confusing parameters and arguments** — Parameters are the variables in the function definition; arguments are the values you pass when calling it.
3. **Not defining before calling** — Python reads code from top to bottom, so you must define a function before you can use it.
4. **Modifying global variables inside a function** — This is generally bad practice. Pass values as arguments and return the result instead.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of function definition, parameters, and return values |
| `exercise.py` | 6 TODOs + 1 challenge on writing custom functions |
| `solution.py` | Answers with explanations for scope and default arguments |

## Go deeper

- [Defining Functions — Official Docs](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Function Arguments — Official Docs](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)

# Variables

## What is it?

Variables are named storage locations in your computer's memory that hold data. In Python, you create a variable by assigning a value to a name using the `=` operator. Python is dynamically typed, meaning you don't need to declare the type of a variable when you create it; the type is determined by the value it holds.

## Real-world analogy

Think of a variable as a **labeled box**. The name of the variable is the label on the outside of the box, and the value is the item you put inside. If you have a box labeled `score` and you put the number `10` inside, you can later ask "what's in the score box?" and get `10`. You can also take out the `10` and put in a `20` — the label stays the same, but the content changes.

## When to use it

| Use when... | Avoid when... |
|---|---|
| You need to store a piece of data to use later | You can use the value directly and it's clear (e.g., small constants) |
| You want to give a descriptive name to a value for readability | You are using a value so temporarily it doesn't need a name |
| The value might change during the program's execution | You are define a constant that should never change (use UPPER_CASE) |

## Common mistakes

1. **Naming conflicts** — using Python keywords like `print`, `list`, or `if` as variable names.
2. **Accessing before assignment** — trying to use a variable name that hasn't been given a value yet.
3. **Inconsistent naming** — mixing `camelCase`, `snake_case`, and `PascalCase` in the same project. (Follow PEP 8: use `snake_case`).

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of variable assignment and re-assignment |
| `exercise.py` | 6 TODOs + 1 challenge on variable basics |
| `solution.py` | Answers with explained naming conventions |

## Go deeper

- [Python Variables — W3Schools](https://www.w3schools.com/python/python_variables.asp)
- [PEP 8 Variable Naming — Official Style Guide](https://peps.python.org/pep-0008/#naming-conventions)

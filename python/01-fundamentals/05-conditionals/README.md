# Conditionals

## What is it?

Conditionals allow your program to make decisions and execute different blocks of code based on whether a condition is `True` or `False`. In Python, we use the `if`, `elif` (else if), and `else` keywords to create decision-making logic.

## Real-world analogy

Think of a conditional as a **fork in the road**. You reach a signpost: "IF it is raining, take the path to the left. ELSE, take the path to the right." You can only take one path based on the current weather condition. If there's an `elif`, it's like having a third option: "IF it's raining, take the left path. ELIF it's snowing, stop and wait. ELSE, take the right path."

## When to use it

| Use when... | Avoid when... |
|---|---|
| You need to run code only if a specific rule is met | The code should always run regardless of the state |
| You have multiple mutually exclusive options | You are checking for the same condition multiple times (refactor your logic) |
| You need to handle error cases or edge cases | You can use a dictionary lookup or polymorphism for more complex branching |

## Common mistakes

1. **Forgetting the colon** — `if x > 5` will fail. It must be `if x > 5:`.
2. **Incorrect indentation** — All code inside the `if` block must be indented consistently (usually 4 spaces).
3. **Using `=` instead of `==`** — `if x = 5:` is an error because it's trying to assign a value, not compare it.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of if/elif/else and nested conditionals |
| `exercise.py` | 6 TODOs + 1 challenge on decision-making logic |
| `solution.py` | Answers with explanations for boolean logic in conditionals |

## Go deeper

- [Python Conditionals — Official Docs](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Boolean Operations — Official Docs](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

# Error Handling

## What is it?

Error handling allows your program to **detect, manage, and recover** from errors at runtime without crashing. Python uses `try`, `except`, `else`, and `finally` blocks. Errors are represented as **exceptions** — objects of classes like `ValueError`, `TypeError`, `FileNotFoundError`, etc.

## Real-world analogy

Think of error handling like a **safety net under a tightrope walker**. The tightrope is the normal code path. If the walker slips (an exception is raised), the net (`except`) catches them. The `else` block is the crowd cheering only if everything went fine. The `finally` block is the stage crew cleaning up props regardless of what happened.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Code might fail for reasons outside your control (file missing, bad user input, network down) | You already know the preconditions can be checked with `if` |
| You want to handle specific error types differently | You catch all exceptions blindly with a bare `except:` |
| You need cleanup that must run (close files, release connections) | The error means truly broken state — let it propagate |

## Common mistakes

1. **Bare `except:`** — catches `KeyboardInterrupt`, `SystemExit` — always specify the exception type.
2. **Silently swallowing errors** — `except Exception: pass` hides bugs permanently.
3. **Catching too broad a type** — catching `Exception` when you only expect `ValueError` masks unexpected errors.
4. **Forgetting `finally`** — resources (files, DB connections) must be closed even when exceptions occur.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | try/except/else/finally, raising custom exceptions |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Errors and Exceptions — Official Docs](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions — Official Docs](https://docs.python.org/3/library/exceptions.html)

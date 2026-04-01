# Modules and Packages

## What is it?

A **module** is any Python file (`.py`) that contains reusable code — functions, classes, or variables. A **package** is a directory of modules with an `__init__.py` file. The `import` statement lets you bring code from one module into another, enabling you to organize large programs into smaller, maintainable pieces.

## Real-world analogy

Think of modules like **books in a library**. Each book covers a specific topic (math, strings, files). A package is a **shelf** that groups related books together. The `import` statement is like checking a book out of the library and bringing it to your desk to use.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Code exceeds a comfortable file size (~300+ lines) | Everything fits in one short script |
| Multiple scripts share the same helper functions | You are just running a one-off analysis |
| You want to distribute reusable code | The abstraction adds complexity without benefit |

## Common mistakes

1. **Circular imports** — Module A imports B, and B imports A. Restructure or use late imports.
2. **Shadowing standard library names** — Naming your file `random.py` or `os.py` breaks imports.
3. **Star imports (`from x import *`)** — Pollutes your namespace unpredictably; always use explicit imports.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Importing from stdlib, aliasing, `__name__ == "__main__"` |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Modules — Official Docs](https://docs.python.org/3/tutorial/modules.html)
- [The Import System — Official Docs](https://docs.python.org/3/reference/import.html)

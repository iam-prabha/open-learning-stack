# Type Hints

## What is it?

**Type hints** (statically defined types) are optional annotations in Python that specify what type of data a variable, function parameter, or return value should have. While Python remains a dynamic language at runtime, type hints allow external tools like `mypy`, `pyright`, or your IDE to catch "type errors" before you even run the code.

## Real-world analogy

Think of type hints like **labels on luggage**:
- **Dynamic Typing (No Hints)**: Every bag looks the same. You only know what's inside (socks vs. breakable vase) when you open it. If you accidentally throw a "socks" treatment at a "vase" bag, it breaks at that moment.
- **Static Type Hints**: Every bag has a label ("Fragile", "Clothing"). You (the developer) and the airport staff (Mypy) can see which bag is which from the outside. If you try to put a vase in a "socks only" bin, the staff stops you before the plane even takes off.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Building large codebases with many contributors | Writing small, quick scripts or prototypes |
| You want better IDE autocompletion and "Jump to Definition" | The overhead of defining complex types slows down exploratory work |
| Catching bugs early before they happen at runtime | Using libraries that are heavily dynamic and don't support typing well |

## Common mistakes

1. **Thinking hints are enforced at runtime** — Python *ignores* hints when running. `def add(a: int, b: int)` will still happily take strings unless you use a tool like `mypy`.
2. **Overusing `Any`** — `Any` tells the type checker to "give up". If you use `Any` everywhere, you lose the benefits of typing.
3. **Circular imports for types** — Use `from __future__ import annotations` or string literal types (`'MyClass'`) to avoid import errors when two files need each other's types.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Basic types, List/Dict, Optional, Union, Callable, and Protocol (Structural Typing) |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Type Hinting — Real Python](https://realpython.com/python-type-checking/)
- [typing module — Official Docs](https://docs.python.org/3/library/typing.html)
- [Mypy Documentation](https://mypy.readthedocs.io/)

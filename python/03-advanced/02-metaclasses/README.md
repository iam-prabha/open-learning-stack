# Metaclasses

## What is it?

In Python, everything is an object, including classes themselves. A **metaclass** is the "class of a class". Just as a class defines how an instance behaves, a metaclass defines how a **class** behaves. By default, Python uses `type` as the metaclass for all classes.

## Real-world analogy

Think of a **metaclass** as a **factory for factories**:
- **Object**: A product (like a specific car).
- **Class**: The factory that builds the car.
- **Metaclass**: The blueprints and rules for building the **factory itself**. It ensures every factory has a loading dock, safety signs, and follows specific regulations before it can even start building cars.

## When to use it

| Use when... | Avoid when... |
|---|---|
| You need to automatically modify classes at creation time (e.g., adding methods, validation) | You can achieve the same result with class decorators or simple inheritance |
| You are building deep framework/library internal logic (like an ORM) | The logic is simple and applies to only a few classes |
| You want to enforce strict interface compliance across many classes | A simple base class or Abstract Base Class (ABC) is sufficient |

## Common mistakes

1. **Overcomplicating the design** — Most problems don't need metaclasses. As Tim Peters said: "Metaclasses are deeper magic than 99% of users should ever worry about."
2. **Ignoring Class Decorators** — Class decorators are often simpler and more readable than metaclasses for basic class modification.
3. **Mismatched Metaclasses** — Inheriting from two classes with different metaclasses can cause errors that are hard to debug.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Basic metaclass definition, `__new__` vs `__init__`, and practical uses |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Metaclasses in Python — Real Python](https://realpython.com/python-metaclasses/)
- [The `type` Class — Official Docs](https://docs.python.org/3/library/functions.html#type)

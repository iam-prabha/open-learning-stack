# OOP Inheritance

## What is it?

Inheritance lets one class (**child/subclass**) automatically receive all the attributes and methods of another class (**parent/superclass**). You then add or override behaviour in the child class. This enables **code reuse** and models "is-a" relationships (a `Dog` *is-a* `Animal`).

## Real-world analogy

Think of inheritance like a **family trait**. Every person in a family inherits certain traits from their parents (eye colour, height tendencies). But each person also develops their own unique personality. The parent class is the ancestor with shared traits; each subclass is a family member who also adds their own.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Two classes truly share an "is-a" relationship | The relationship is actually "has-a" (use composition instead) |
| You want to reuse and extend existing behaviour | You are inheriting just to get some helper methods (prefer mixins or composition) |
| You need polymorphism — treat subclasses uniformly via a base class interface | Deep inheritance chains (>2-3 levels) increase complexity fast |

## Common mistakes

1. **Not calling `super().__init__()`** — The parent's `__init__` doesn't run automatically; always call it.
2. **Deep inheritance chains** — Prefer flat hierarchies and composition over multi-level inheritance.
3. **Overriding without calling super** — For methods like `__str__`, always call `super()` if you still want the parent behaviour.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Single inheritance, method override, `super()`, polymorphism |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Inheritance — Official Docs](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [super() explained — Official Docs](https://docs.python.org/3/library/functions.html#super)

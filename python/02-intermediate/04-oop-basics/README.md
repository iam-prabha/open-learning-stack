# OOP Basics

## What is it?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around **objects** — bundles of **data (attributes)** and **behaviour (methods)**. A **class** is the blueprint; an **object** (or instance) is a concrete thing built from that blueprint.

## Real-world analogy

Think of a class like a **blueprint for a car**. The blueprint describes that every car has `color`, `model`, and `speed`. When you build an actual car from the blueprint, that car is an **object (instance)**. Two car objects can have different colours but both know how to `accelerate()` because they share the same blueprint.

## When to use it

| Use when... | Avoid when... |
|---|---|
| You have data and behaviour that naturally belong together | Simple scripts with no repeated structures |
| You want to create many similar things (users, products, orders) | Functional or procedural style fits better |
| You need to model real-world entities with state | OOP adds boilerplate without benefit |

## Common mistakes

1. **Missing `self`** — Every method must take `self` as the first argument: `def greet(self):`.
2. **Confusing class and instance attributes** — Class attributes are shared; instance attributes are per-object. Set instance attributes inside `__init__`.
3. **Forgetting to call `super().__init__()`** — Always call it in subclasses to properly initialize the parent class.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Defining classes, creating instances, calling methods |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Classes — Official Docs](https://docs.python.org/3/tutorial/classes.html)
- [Data Model — Official Docs](https://docs.python.org/3/reference/datamodel.html)

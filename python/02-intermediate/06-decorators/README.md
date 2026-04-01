# Decorators

## What is it?

A decorator is a function that **wraps another function** to extend or modify its behaviour without changing its source code. The `@decorator` syntax is syntactic sugar for `func = decorator(func)`. Decorators are a core Python pattern used in frameworks like Flask, Django, and FastAPI.

## Real-world analogy

Think of a decorator like a **phone case**. The phone (original function) still works the same. The case (decorator) adds protection and a new look without modifying the phone itself. You can swap cases (decorators) freely. Putting on the case is `@case` — you just place it on top.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Adding cross-cutting concerns (logging, timing, auth checks) | The wrapper logic is complex and obscures intent |
| You want to modify many functions uniformly without touch each one | A simple helper function call would be clearer |
| Building reusable function wrappers | You only need to modify one specific function |

## Common mistakes

1. **Forgetting `functools.wraps`** — Without it, the wrapped function loses its `__name__`, `__doc__`, etc.
2. **Calling instead of passing** — `@my_decorator()` vs `@my_decorator` — be careful; decorators with arguments need an extra layer.
3. **Order matters with stacked decorators** — `@a` on top of `@b` applies `a(b(func))`.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Simple decorator, decorator with arguments, stacking |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Decorators — Real Python](https://realpython.com/primer-on-python-decorators/)
- [functools.wraps — Official Docs](https://docs.python.org/3/library/functools.html#functools.wraps)

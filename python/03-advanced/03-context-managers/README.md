# Context Managers

## What is it?

A **context manager** is an object that defines the runtime context to be established when executing a `with` statement. It ensures that resources are properly acquired and, most importantly, **automatically released**, even if an error occurs. The most common example is `with open('file.txt') as f:`.

## Real-world analogy

Think of a context manager like **renting a bowling lane**:
1. **Setup (`__enter__`)**: You pay the fee, get your shoes, and the lane is turned on for you.
2. **Work (Body of `with`)**: You bowl your games.
3. **Teardown (`__exit__`)**: Regardless of whether you bowled a strike or fell down, the lane is turned off and you return the shoes when your time is up. The system "cleans up" after you automatically.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Managing resources like files, network sockets, or database connections | The lifetime of the resource is complex and spans many unrelated functions |
| You need to guarantee "cleanup" code runs (e.g., releasing a lock) | You are just grouping code for visual clarity (use a function instead) |
| Temporarily changing global state (e.g., precision in decimal math) | The setup/teardown logic is trivial and repeated only once |

## Common mistakes

1. **Forgetting to return `True` in `__exit__`** — If you want to "swallow" an exception, you must return `True`. Otherwise, the exception propagates.
2. **Opening resources in `__enter__` without a plan to close them in `__exit__`** — The whole point is the guarantee of closure.
3. **Overusing `@contextmanager` for complex logic** — For complex state, a class-based context manager is often more readable than a generator-based one.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Class-based and function-based (`@contextlib.contextmanager`) demos |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [The `with` statement — Official Docs](https://docs.python.org/3/reference/compound_stmts.html#with)
- [contextlib module — Official Docs](https://docs.python.org/3/library/contextlib.html)

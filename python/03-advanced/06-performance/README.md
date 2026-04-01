# Performance

## What is it?

Performance in Python involves **measuring** (profiling) and **improving** (optimizing) the execution speed and memory usage of your code. Python is a high-level interpreted language, so while it is slower than C or Rust, there are many ways to make it run significantly faster by using the right data structures, algorithms, and libraries.

## Real-world analogy

Think of performance like **packing a shipping container**:
- **Inefficient Code**: Throwing items in randomly. You run out of space quickly and it takes ages to sort through.
- **Profiling**: Opening the container to see exactly which items are taking up the most space.
- **Optimization**: Organizing items into boxes, using the available volume perfectly, and maybe replacing a heavy wooden crate with a lighter plastic one. It's the same cargo, but now it's faster to move and easier to manage.

## When to use it

| Use when... | Avoid when... |
|---|---|
| A function is a bottleneck and slows down the user experience | The code is already "fast enough" (Premature optimization is the root of all evil) |
| Running heavy data processing or scientific simulations | Improving the code makes it unreadable and harder to maintain |
| You want to reduce cloud computing costs for high-scale apps | The bottleneck is actually the Network or Database (not Python) |

## Common mistakes

1. **Premature Optimization** — Optimizing code before you even know if it's slow. Always profile first!
2. **Ignoring the Standard Library** — Built-in functions like `sum()`, `min()`, `max()` are written in C and are much faster than writing your own loops.
3. **Using the wrong data structure** — For example, searching in a `list` ($O(n)$) when you could use a `set` ($O(1)$).
4. **Reinventing the wheel** — Trying to write your own math logic instead of using `numpy`.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | basic profiling with `timeit` and `cProfile` |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Python Speed — Official Docs](https://docs.python.org/3/library/stdtypes.html#types-speed)
- [timeit module — Official Docs](https://docs.python.org/3/library/timeit.html)
- [cProfile — Official Docs](https://docs.python.org/3/library/profile.html)

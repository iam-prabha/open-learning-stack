# Concurrency

## What is it?

Concurrency in Python refers to running multiple tasks in overlapping periods of time. It is achieved through three main approaches:

1. **Threading**: Good for I/O-bound tasks (waiting for network/disk). Multiple threads share the same memory space but are limited by the Global Interpreter Lock (GIL).
2. **Multiprocessing**: Good for CPU-bound tasks (heavy calculations). It spawns separate Python processes, each with its own GIL and memory space.
3. **Asyncio**: Cooperative multitasking for high-concurrency I/O. Uses a single thread and an event loop with `async`/`await`.

## Real-world analogy

Think of a **restaurant**:
- **Threading**: One waiter handling multiple tables. While one table is reading the menu, the waiter checks on another. (Waiters share the same kitchen space).
- **Multiprocessing**: Multiple separate restaurants. Each has its own kitchen and staff. One restaurant being busy doesn't slow down the other.
- **Asyncio**: A very fast waiter who only moves when a customer is ready. They don't mindlessly wait at a table; they use an event system to respond instantly to needs.

## When to use it

| Approach | Use when... | Avoid when... |
|---|---|---|
| **Threading** | Frequent waiting (HTTP requests, database queries) | Heavy mathematical computations (GIL will slow it down) |
| **Multiprocessing** | CPU-intensive work (image processing, data crunching) | Frequent communication between tasks is needed (overhead is high) |
| **Asyncio** | Thousands of concurrent network connections | You have blocking I/O librairies that don't support `await` |

## Common mistakes

1. **GIL Misunderstanding** — Thinking threads will speed up math. In Python, only one thread executes bytecode at a time.
2. **Race Conditions** — Multiple threads modifying the same variable at once. Always use `Lock` or `Queue`.
3. **Blocking the Event Loop** — Putting a `time.sleep()` inside an `async` function. Use `await asyncio.sleep()`.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | basic threading, multiprocessing, and asyncio demos |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Concurrency in Python — Real Python](https://realpython.com/python-concurrency/)
- [threading — Official Docs](https://docs.python.org/3/library/threading.html)
- [multiprocessing — Official Docs](https://docs.python.org/3/library/multiprocessing.html)
- [asyncio — Official Docs](https://docs.python.org/3/library/asyncio.html)

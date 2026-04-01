# Closures

## What is it?

A **closure** is the combination of a function bundled together (enclosed) with references to its surrounding state (the **lexical environment**). In simpler terms, a closure gives an inner function access to the outer function's scope, even after the outer function has finished executing.

## Real-world analogy

Think of a closure like a **backpack** that a function carries around:
- When a function is "born" (defined), it looks around and packs everything it sees in its current environment into its backpack.
- Even if that function travels to a completely different part of the code (different scope), it still has its backpack with all the original variables it needs.
- No one else can look inside that specific backpack — it's private to that function.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Creating **private variables** (data encapsulation) | You only need a simple, self-contained calculation |
| **Function factories**: Creating functions with pre-filled data | It makes tracing the source of a variable too confusing |
| Maintaining state in asynchronous callbacks | You are creating thousands of closures unnecessary (memory overhead) |

## Common mistakes

1. **Memory leaks** — Because closures keep variables alive, holding onto a closure for too long can prevent garbage collection of large data structures.
2. **Loop closure trap** — Using `var` in a loop with closures often leads to all functions sharing the *last* value of the loop. Always use `let`.
3. **Overusing for simple state** — Sometimes a simple class or object property is clearer than a complex closure.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | basic closures, private state, and function factories |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Closures — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [Understanding Closures — JavaScript.info](https://javascript.info/closure)

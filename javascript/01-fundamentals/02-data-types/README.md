# Data Types

## What is it?

JavaScript is a dynamically typed language, meaning variables don't have types — **values** do. JavaScript has 8 built-in types, divided into two categories:

1. **Primitives**: Simple, immutable values stored directly (String, Number, Boolean, Null, Undefined, Symbol, BigInt).
2. **Objects**: Complex, mutable data structures stored by reference (Object, Array, Function).

## Real-world analogy

Think of data types like **shipping items**:
- **Primitives**: Small, individual items like a **coin** or a **key**. They are what they are. If you want a different coin, you swap it for another one.
- **Objects**: A **locker** or a **bag**. You can put many things inside it, take them out, or change them. You give someone the **key** (reference) to the locker rather than the locker itself.

## When to use it

| Type | Use when... | Avoid when... |
|---|---|---|
| **Number** | Any mathematical value (no separate float/int) | Extremely large integers (use `BigInt`) |
| **String** | Text data | Storing structured objects as strings (use `Object`) |
| **Boolean** | True/False logic and flags | Confusing numbers (0/1) for true/false |
| **Null/Undefined** | Intentional absence of value (`null`) vs. uninitialized (`undefined`) | Checking for existence without knowing the difference |

## Common mistakes

1. **`typeof null` returns `"object"`** — This is a well-known legacy bug in JavaScript.
2. **Numbers are always 64-bit floats** — `0.1 + 0.2` does not exactly equal `0.3` due to floating-point precision.
3. **Comparing objects by value** — `{} === {}` is `false`. Objects are compared by reference, not by their content.
4. **NaN is a number** — `typeof NaN` returns `"number"`, even though it stands for "Not a Number".

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of all 8 types and the `typeof` operator |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Data types — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [The 'typeof' operator — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)

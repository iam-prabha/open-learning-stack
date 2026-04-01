# Promises

## What is it?

A **Promise** is an object representing the eventual completion (or failure) of an asynchronous operation and its resulting value. It allows you to write asynchronous code that looks and behaves more like synchronous code, avoiding the dreaded "Callback Hell."

## Real-world analogy

Think of a Promise like **ordering a pizza**:
1. **Pending**: You place the order. The pizza shop gives you a receipt (the Promise). You don't have the pizza yet, but you have a "promise" that it will arrive.
2. **Success (Fulfilled)**: The delivery driver arrives with your pizza. You then take an action (eat the pizza). This is handled by `.then()`.
3. **Failure (Rejected)**: The shop calls and says they ran out of dough. You then take a backup action (order something else). This is handled by `.catch()`.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Making network requests (e.g., `fetch`) | The operation is already synchronous and fast |
| Reading large files from storage | You have a simple calculation that results immediately |
| You want to chain multiple async steps in order | You only have one single async task (callbacks are fine but Promises are cleaner) |

## Common mistakes

1. **The "Shadow" Promise** — Forgetting to `return` a promise inside a `.then()` block, causing the chain to break.
2. **Nesting instead of Chaining** — Putting a `.then()` inside another `.then()` instead of returning the promise to the outer level.
3. **Ignoring `.catch()`** — Unhandled promise rejections can crash your application or make debugging impossible.
4. **Expecting immediate results** — Trying to use the value of a promise before it has resolved.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | basic promise creation, `.then()`, `.catch()`, and `.finally()` |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Promises — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [Using Promises — MDN Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)

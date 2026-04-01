# Async / Await

## What is it?

`async` and `await` are special keywords that allow you to write asynchronous code that looks and behaves like synchronous code. Built on top of Promises, they provide a cleaner, more readable way to handle async logic without excessive `.then()` chaining.

- **`async`**: Used before a function declaration. It ensures the function *always* returns a Promise.
- **`await`**: Used inside an `async` function. It pauses the function execution until the Promise resolves, then returns the result.

## Real-world analogy

Think of `async/await` like **a personal assistant**:
- **Promises (`.then`)**: You tell your assistant, "Go buy coffee. When you're done, call me. When you've called me, I'll write this email." You have to plan the whole chain of events upfront.
- **`async/await`**: You tell your assistant, "**Wait** here while I tell you to buy coffee. **Wait** until you're back. Okay, now I will write the email." You write the instructions in order, and the program "pauses" just like a human would, making it much easier to read and maintain.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Handing sequential async operations (First do A, then do B) | Doing multiple independent tasks that can run at the same time (use `Promise.all` instead) |
| You want to use standard `try/catch` for async error handling | The logic is trivial and a short `.then()` is more concise |
| Cleaning up deeply nested promise chains | You are not inside an `async` function (you cannot use `await` at the top level in all environments) |

## Common mistakes

1. **Forgetting `await`** — If you call an async function without `await`, you just get the Promise object, not the result.
2. **Serializing instead of Paralleling** — `await task1(); await task2();` runs them one after the other. If they don't depend on each other, use `await Promise.all([task1(), task2()])`.
3. **Forgetting `try/catch`** — Since `await` doesn't have a `.catch()` attached by default, an error will crash the function unless wrapped in a `try/catch` block.
4. **Using `await` in a `.forEach()` loop** — `.forEach` doesn't "wait" for the callback. Use a standard `for...of` loop instead.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | basic async/await syntax, try/catch, and Promise.all integration |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [async function — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [await operator — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)

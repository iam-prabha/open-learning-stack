# Error Handling

## What is it?

Error handling is the process of anticipating, detecting, and resolving errors in your application. In JavaScript, we use the `try...catch...finally` block along with the `throw` keyword to manage execution flow when something unexpected happens. Proper error handling prevents your application from crashing and provides helpful feedback to both developers and users.

## Real-world analogy

Think of error handling like **a safety net for a circus performer**:
- **Execution (`try`)**: The performer attempting a difficult stunt.
- **The Stunt Fails (`throw`)**: Something goes wrong mid-air.
- **The Safety Net (`catch`)**: Catches the performer so they don't hit the ground (prevents the app from crashing). The net might also sound an alarm (log an error) or direct the performer to a backup routine.
- **Cleanup (`finally`)**: The performer takes a bow or checks their equipment before leaving the stage, regardless of whether the stunt succeeded or the net was used.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **`try...catch`** | Processing unreliable inputs (like JSON parsing or network requests) | Doing simple, reliable math (e.g., `1 + 1`) |
| **`throw`** | You discover an invalid state early in a function (e.g., a negative age) | You can easily handle the case with a simple `if/else` |
| **`finally`** | You need to close a file or stop a loading spinner no matter what happens | You have no cleanup logic to perform |
| **Custom Errors** | Creating specialized error types for your library (e.g., `ValidationError`) | A simple string message is enough for a small app |

## Common mistakes

1. **Swallowing errors** — `catch(err) { }` (doing nothing in the catch block) is dangerous as it hides bugs. Always at least log the error.
2. **Forgetting `.catch()` on async functions** — Errors in async functions won't be caught by a regular `try/catch` unless you use `await` inside the try block.
3. **Implicitly returning `undefined`** — If a function fails and catches an error, ensure it returns something sensible (like `null`) or re-throws the error if it can't handle it.
4. **Throwing non-Error objects** — You can `throw "Oops"`, but it's better to `throw new Error("Oops")` as it includes a **stack trace**.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | basic try/catch, throw, finally, and custom error classes |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Error handling, "try...catch" — JavaScript.info](https://javascript.info/try-catch)
- [The Error object — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)

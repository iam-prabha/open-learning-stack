# The Event Loop

## What is it?

JavaScript is a **single-threaded** language, meaning it can only do one thing at a time. However, it can handle asynchronous operations (like network requests or timers) without blocking the main thread. This is made possible by the **Event Loop**, which coordinates the interaction between the **Call Stack**, **Web APIs** (or C++ APIs in Node), the **Task Queue** (Macrotasks), and the **Microtask Queue**.

## Real-world analogy

Think of the Event Loop like **a restaurant kitchen**:
- **The Chef (Call Stack)**: The single person cooking. They can only handle one order at a time.
- **The Oven (Web APIs)**: When a pizza needs 10 minutes to bake, the Chef doesn't just stand there staring at the oven. They put it in and move to the next order.
- **The Bell (Task Queue)**: When the oven dings, a notice is placed on a board.
- **The Manager (Microtask Queue)**: High-priority tasks (like "Clean up a spilled drink") that the Chef MUST do before taking the next order from the Bell board.
- **The Manager's Rule (Event Loop)**: The Chef only looks at the board when their hands are empty (Stack is clear). They always check the spills (Microtasks) before the Pizza dings (Macrotasks).

## When to use it

| Feature | Use when... | Priority |
|---|---|---|
| **Synchronous Code** | Standard calculations and logic | **Immediate** (Highest) |
| **Microtasks (`Promise.then`)** | High-priority async tasks that should run as soon as current code finished | **Medium** (Before Macrotasks) |
| **Macrotasks (`setTimeout`)** | Lower-priority tasks or tasks that need to wait a specific time | **Low** (Wait for next loop) |
| **`process.nextTick` (Node only)** | Tasks that must run in the exact same phase of the loop | **Critical** (Even before Promises) |

## Common mistakes

1. **Blocking the Event Loop** — Running a massive `for` loop (like 10 billion iterations) blocks the chef from ever looking at the oven or the bell. The UI "freezes."
2. **Expecting `setTimeout(..., 0)` to be immediate** — It only places the task at the back of the queue. It will still wait for every synchronous line and every microtask to finish first.
3. **Infinite Microtask Loops** — If a promise `.then()` creates another promise `.then()`, the Chef will handle them forever and never reach the Macrotask queue.
4. **Confusing execution order** — Thinking `setTimeout` will run before a resolved `Promise.then` just because it was written above it.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of execution order (Stack vs Micro vs Macro) |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [The Event Loop — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop)
- [Visual Guide to the Event Loop — Lydia Hallie](https://dev.to/lydiahallie/javascript-visualized-event-loop-33ee)

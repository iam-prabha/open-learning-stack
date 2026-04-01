# Variables (let, const, var)

## What is it?

In JavaScript, there are three ways to declare variables: `let`, `const`, and `var`. They differ in terms of **scope** (where they are accessible) and **re-assignability** (whether you can change their value).

- **`const`**: For values that should never change. Block-scoped.
- **`let`**: For values that can change. Block-scoped.
- **`var`**: The old way. Avoid in modern JS. Function-scoped and subject to "hoisting".

## Real-world analogy

Think of variables like **labeled containers**:
- **`const`**: A **sealed box**. You can see what's inside, but you can't open it to swap the item. You'd have to destroy the box (delete the variable) to change it.
- **`let`**: A **re-sealable container** (like Tupperware). You can take the lid off, swap the item, and put the lid back on.
- **`var`**: A **cardboard box in a shared basement**. It's messy, easily confused with other boxes, and sometimes appears before you even put it there (hoisting).

## When to use it

| Keyword | Use when... | Avoid when... |
|---|---|---|
| `const` | By default, for almost everything | You know you need to change the value later |
| `let` | You are writing a loop or a counter | Global state or values that shouldn't change |
| `var` | Never | In modern JavaScript development |

## Common mistakes

1. **Trying to re-assign a `const`** — `const x = 1; x = 2;` throws a `TypeError`.
2. **Accessing `let`/`const` before declaration** — Unlike `var`, they are in a "Temporal Dead Zone" (TDZ) and will throw a `ReferenceError`.
3. **Using `var` in loops** — `var` doesn't create a new scope for each loop iteration, which often leads to unexpected bugs in async code.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of scope, re-assignment, and the TDZ |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Variables — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [ES6 let and const — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)

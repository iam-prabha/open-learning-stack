# Functions

## What is it?

Functions are blocks of reusable code designed to perform a particular task. In JavaScript, functions are "first-class citizens," meaning they can be stored in variables, passed as arguments, and returned from other functions. There are three main ways to define them: **Declarations**, **Expressions**, and **Arrow Functions**.

## Real-world analogy

Think of a function like a **vending machine**:
- **Inputs (Parameters)**: The money and the button you press (e.g., "B4").
- **Processing (Body)**: The machine checks if the money is enough and moves the mechanical arm to pick the item.
- **Output (Return)**: The snack drops into the tray. If the machine just makes a sound but no snack drops, it's like a function that returns `undefined`.

## When to use it

| Type | Use when... | Avoid when... |
|---|---|---|
| **Declaration** | Standard, standalone functions. They are **hoisted** (can be called before they are defined). | You want to limit the function's scope tightly. |
| **Expression** | You want to store a function in a variable or object property. | You need to call the function before its definition. |
| **Arrow (`=>`)** | Short, "anonymous" functions (like callbacks). They have a modern, concise syntax and **lexical `this`**. | Complex logic or when you explicitly need a separate `this` context. |

## Common mistakes

1. **Forgetting to `return`** — If you don't use the `return` keyword, the function returns `undefined` by default.
2. **Confusing Parameters vs Arguments** — Parameters are the variables in the function definition; Arguments are the actual values you pass when calling it.
3. **Implicit Return in Arrow Functions** — `(a, b) => a + b` returns the result automatically. `(a, b) => { a + b }` returns `undefined` because of the curly braces.
4. **Hoisting behavior** — Function declarations are hoisted, but function expressions (stored in `const`/`let`) are not!

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of declarations, expressions, arrow functions, and default parameters |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Functions — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [Arrow functions — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

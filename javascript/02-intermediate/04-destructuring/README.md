# Destructuring

## What is it?

Destructuring assignment is a special syntax that allows you to "unpack" values from arrays, or properties from objects, into distinct variables. It makes your code cleaner, more readable, and reduces the need for repetitive boilerplate code.

## Real-world analogy

Think of destructuring like **unpacking a shipping crate**:
- **Standard Assignment**: You open the crate, reach in, grab one item, and put it on a shelf. Then you reach in again for the next item.
- **Destructuring**: You have a specialized machine that opens the crate and instantly places the **hammer**, the **wrench**, and the **screwdriver** into their exact spots on your workbench in one motion.

## When to use it

| Use when... | Avoid when... |
|---|---|
| Extracting multiple properties from an object (e.g., function parameters) | You only need one single property from a very deeply nested object |
| Swapping variables quickly: `[a, b] = [b, a]` | The structure you're unpacking is unpredictable or changes constantly |
| Handling function return values (especially arrays from Hooks or APIs) | It makes the variable names less clear than the original object property |

## Common mistakes

1. **Undefined properties** — If the property doesn't exist, the variable becomes `undefined`. Use **default values** to prevent this: `const { name = "Guest" } = user`.
2. **Aliasing confusion** — `const { name: userName } = user` creates a variable `userName`, NOT `name`.
3. **Nested complexity** — Deeply nesting destructuring: `const { a: { b: { c } } } = obj` can be very hard to read.
4. **Incorrect syntax for Arrays vs Objects** — Using `{ }` for arrays or `[ ]` for objects will cause an error or unexpected behavior.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | basic and advanced destructuring, aliasing, and defaults |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Destructuring assignment — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
- [ES6 Destructuring — JavaScript.info](https://javascript.info/destructuring-assignment)

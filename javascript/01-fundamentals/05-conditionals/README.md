# Conditionals

## What is it?

Conditionals allow your code to make decisions based on certain conditions. In JavaScript, we primarily use `if/else`, the **Ternary Operator** (shorthand for simple if/else), and the `switch` statement for multiple fixed choices.

## Real-world analogy

Think of conditionals like **an automated toll booth**:
- **`if/else`**: A simple gate. "IF you have a pass, open the gate. ELSE, keep it closed and ask for payment."
- **Ternary (`? :`)**: A **one-line sign**. "Pass? $0 : $5". It's a quick decision that returns a single result (the price).
- **`switch`**: A **multi-lane divider**. "Lane 1 for Trucks, Lane 2 for Cars, Lane 3 for Motorcycles." You jump straight to the lane that matches your vehicle type.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **`if/else`** | Standard logic, ranges (e.g. `age > 18`), or complex comparisons | You have a long list of exact string/number matches (use `switch`) |
| **Ternary (`? :`)** | Assigning a variable based on a simple condition | Nesting ternaries within ternaries (very hard to read!) |
| **`switch`** | One variable has many discrete, exact values | You need to check for ranges or use different variables in each branch |
| **Early Return** | Handling errors or base cases at the top of a function | Having a giant `else` block that wraps the rest of the function |

## Common mistakes

1. **Forgetting `break` in a `switch`** — Without `break`, the code will "fall through" and execute all subsequent cases.
2. **Confusing `=` with `===`** — `if (x = 5)` assigns 5 to x and is always truthy. Always use `if (x === 5)`.
3. **Overusing the Ternary** — If your ternary is longer than one line, it belongs in an `if/else` for readability.
4. **Truthy/Falsy traps** — `if (0)` is falsy. `if ("false")` is truthy (because it's a non-empty string).

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of if/else, switch/case, and ternary logic |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Conditionals — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals)
- [Switch statement — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)

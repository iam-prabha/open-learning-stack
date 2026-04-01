# Functions

## What is it?

In TypeScript, functions are a core way of defining logic, and you can add type annotations to both the **parameters** (the inputs) and the **return type** (the output). This ensures that you call the function with the right data and that the function returns exactly what you expect.

## Real-world analogy

Think of a typed function like **a vending machine**:
- **Parameters (Input)**: The machine only accepts specific items (like "US Quarters" or "1 Dollar Bills"). If you try to put in a "Laundry Token," it rejects it.
- **Return Type (Output)**: You know exactly what you'll get back (a "Can of Soda" or "Change"). You won't accidentally get an "Anchor."
- **Logic**: The internal mechanism of the machine that converts your dollar into a drink.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Parameter Types** | Every time you define a function | Never! Always type your inputs |
| **Return Type** | Whenever the return value is complex or you want to enforce a specific shape | Simple functions where TS can easily infer the return type (optional but recommended) |
| **Optional Params** | Parameters that aren't always needed (e.g., `(msg: string, user?: string)`) | The parameter is strictly required for the function to work |
| **Void** | Functions that don't return any value (just perform an action) | You forgot to write a return statement (use it intentionally) |

## Common mistakes

1. **Forgetting the return type** — While TS can often infer it, explicitly defining it acts as a safeguard. If you change your logic later, TS will tell you if the return value no longer matches your original intent.
2. **Infinite arguments** — Not using **Rest Parameters** (`...args: number[]`) when you need to handle multiple inputs.
3. **Implicit 'any'** — Leaving parameters untyped defaults them to `any` (if strict mode is off), which is unsafe.
4. **Incorrect Optional placement** — Optional parameters MUST come after all required parameters in the function definition.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Typed parameters, return types, optional/default params, and Rest parameters |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [More on Functions — TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/2/functions.html)
- [Function Type Expressions](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-type-expressions)

# Type Guards and Narrowing

## What is it?

**Type Narrowing** is the process where TypeScript uses your code's logic to refine a broad type (like a Union) into a more specific one. **Type Guards** are the actual checks you write (like `typeof` or `instanceof`) that trigger this narrowing. This allows you to safely access properties that might only exist on one branch of a union.

## Real-world analogy

Think of type guards like **a security checkpoint at a festival**:
- **Broad Type (Ticket Holder)**: Everyone at the gate has a "Ticket."
- **Check (`typeof`)**: The guard checks if the ticket is "VIP" or "General Admission."
- **Narrowing**: Once you are confirmed as "VIP," you are "narrowed" into that group. You can now access the "VIP Lounge" (a property), which the "General Admission" group cannot.
- **Predicates**: A specialized guard who knows exactly how to identify a "Performer" even if they don't have a standard ticket.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **`typeof`** | Checking for primitives (string, number, boolean) | Checking for custom classes or complex objects |
| **`instanceof`**| Checking if an object was created with a specific `class` | Checking for interfaces (interfaces don't exist at runtime) |
| **`in` operator** | Checking if a property exists on an object | You have many objects with similar property names |
| **Type Predicates**| Creating a reusable function to identify a specific type (returns `arg is T`) | Simple checks that can be done inline |

## Common mistakes

1. **Checking Interfaces with `instanceof`** — Interfaces are "erased" during compilation, so `instanceof MyInterface` will always fail. Use the `in` operator or a type predicate instead.
2. **Forgetting "Truthiness"** — Narrowing a variable to `string` doesn't mean it's not an empty string `""`.
3. **Incomplete narrowing** — Handling two cases of a three-part union and forgetting the last one.
4. **Incorrect Predicate Return** — Returning `boolean` instead of `arg is T` for a custom type guard. Without the `is` keyword, TypeScript won't narrow the type in the calling function.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Built-in guards and user-defined predicates |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Narrowing — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/narrowing.html)
- [Discriminated Unions — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions)

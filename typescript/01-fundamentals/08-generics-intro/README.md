# Generics (Intro)

## What is it?

**Generics** allow you to create reusable components that work with a variety of types rather than a single one. This allows users to consume these components and use their own types. Generics are like "variables for types." They provide a way to tell TypeScript: "This function/class will work with *some* type, and I'll tell you which one when I use it."

## Real-world analogy

Think of a Generic like **a shipping container**:
- **The Container (Generic)**: It's a standard box designed to hold *something*. It doesn't care if it's "Cars," "Apples," or "Computers."
- **The Label (`<T>`)**: When you load the container, you put a label on it: `Container<Cars>`. Now everyone knows exactly what's inside.
- **Type Safety**: Because of the label, the crane (compiler) won't try to unload the cars and put them in a fruit basket. It knows they are cars and handles them correctly.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Generics (`<T>`)** | Building utility functions (like `identity`, `first`, or `wrapper`) | You already know the exact type you need |
| **Generic Classes** | Creating collection-like structures (like a `DataStore` or `Queue`) | The class only ever deals with one specific type of data |
| **Generic Interfaces**| Describing a response shape from an API (e.g., `ApiResponse<T>`) | The response always has the same fixed structure |

## Common mistakes

1. **Over-genericizing** — Making every function generic even when it's not needed. This makes the code much harder to read.
2. **Confusing Generics with `any`** — `any` says "I don't care what the type is, and I won't check it." Generics say "I don't know the type yet, but once I do, I will enforce it strictly."
3. **Using vague names** — While `T`, `U`, and `V` are standard, sometimes using more descriptive names like `TData` or `TUser` can be clearer in complex logic.
4. **Incorrect Constraints** — Forgettting that you can restrict what types a generic can be (e.g., `<T extends string>`).

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Basic generic functions, interfaces, and classes |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Generics — TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/2/generics.html)
- [Generics Explained — Visual Guide](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-types)

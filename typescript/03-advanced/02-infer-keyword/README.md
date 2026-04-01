# The 'infer' Keyword

## What is it?

The **`infer`** keyword is a powerful feature of [Conditional Types](02-intermediate/07-conditional-types/) that allows you to "pattern match" and "pluck" a type out of another complex type. It tells TypeScript: "If the input matches this specific shape, **infer** (guess) what this internal type is and give it a name so I can use it later."

## Real-world analogy

Think of the `infer` keyword like **a set of X-ray goggles used by a warehouse worker**:
- **The Box (Target Type)**: A sealed box containing something (`Array<string>`, `Promise<User>`).
- **The Goggles (infer)**: You look at the box. You don't know what's inside yet, but you know *where* it is inside the box.
- **The Capture**: You say, "Whatever is in that specific spot, label it as `T_CONTENT`."
- **The Result**: Now you can use `T_CONTENT` to print a new label or decide where the box goes. You've "inferred" the inner content from the outer package.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **`infer`** | Extracting the return type of a function | You can directly access the type (e.g., via a simple interface) |
| **`infer`** | Unwrapping a `Promise<T>` to get the `T` | You already have the `T` type defined separately |
| **`infer`** | Getting the element type of an array (`T[]`) | The array type is simple and already known |

## Common mistakes

1. **Incorrect Context** — `infer` can ONLY be used inside the `extends` clause of a conditional type.
2. **Ambiguous Matches** — Trying to `infer` from a type that doesn't follow a clear pattern.
3. **Overusing Generics** — Sometimes you can get the same result by using a generic parameter directly in a function instead of a complex conditional type with `infer`.
4. **Naming Conflicts** — Using common names like `T` inside multiple `infer` statements in the same complex type can be confusing.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Unwrapping Promises, function returns, and array elements |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Inference within Conditional Types — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#inferring-within-conditional-types)
- [How 'infer' works — Visual Guide](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#inferring-within-conditional-types)

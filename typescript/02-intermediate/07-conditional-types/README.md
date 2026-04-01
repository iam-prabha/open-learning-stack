# Conditional Types

## What is it?

**Conditional Types** allow you to write logic at the type level. Using the syntax `SomeType extends OtherType ? TrueType : FalseType`, you can tell TypeScript to choose a type based on a condition. This is essentially an **if-else statement for types**.

## Real-world analogy

Think of a conditional type like **an automatic sorting machine in a recycling center**:
- **The Input (`T`)**: A mix of items (Paper, Plastic, Glass).
- **The Condition (`extends`)**: The machine checks: "IS this item made of Paper?"
- **The Result (`? True : False`)**: 
    - If **YES**, it goes into the "Paper Bin" (Type X).
    - If **NO**, it goes into the "Other Bin" (Type Y).
- **The `infer` keyword**: Like a camera that can look inside a box and "guess" what's inside based on its shape, then use that guess for the next step.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Conditional Type**| Your component's return type depends on its input type (e.g., passing a string returns a string, but passing a number returns a number) | You can achieve the same result with simple function overloading |
| **`infer`** | You need to "pluck" a type out of another complex type (like getting the type of elements inside an array) | You already have direct access to the type |
| **Excluding Types** | Creating a type that removes certain members from a union (e.g., `Exclude<string | number, string>`) | You only have 2-3 members (just write them out) |

## Common mistakes

1. **Over-nesting** — `A extends B ? (C extends D ? E : F) : G`. This becomes "unreadable soup" very quickly. Try to break complex logic into multiple named types.
2. **Distribution surprises** — When you pass a Union to a conditional type, it "distributes" (runs the check for each member). This is usually what you want, but it can be surprising if you're not expecting it.
3. **Using `any` as a condition** — This will usually result in a union of both the True and False branches, which is rarely useful.
4. **Incorrect `infer` placement** — The `infer` keyword can only be used in the `extends` clause of a conditional type.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Basic conditionals, distribution, and `infer` |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Conditional Types — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html)
- [Inferring with Conditional Types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#inferring-within-conditional-types)

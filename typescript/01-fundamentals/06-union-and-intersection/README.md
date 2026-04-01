# Union and Intersection Types

## What is it?

TypeScript provides powerful ways to combine existing types:
- **Union Types (`|`)**: Allows a value to be one of several types. Think of it as **OR**.
- **Intersection Types (`&`)**: Combines multiple types into one. Think of it as **AND**. This new type will have all the properties of all the combined types.

## Real-world analogy

Think of types like **qualifications or job roles**:
- **Union (`OR`)**: A job posting says, "We need a **Developer** OR a **Designer**." You only need one of those skill sets to apply.
- **Intersection (`AND`)**: A job posting says, "We need a **Full-stack Developer** (Front-end AND Back-end)." You must possess both sets of skills to fulfill the role.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Union (`|`)** | Variables that can hold different types (e.g., `string | number`) | You can group the types into a single object or interface |
| **Intersection (`&`)** | Merging existing interfaces to create a more specific one | The combined types have conflicting properties (e.g., `string & number` is impossible, results in `never`) |
| **Literal Union** | Creating a fixed set of string choices (e.g., `"Red" | "Green" | "Blue"`) | You have a massive list of options (use an `Enum`) |

## Common mistakes

1. **Accessing common properties** — In a Union (`A | B`), you can only access properties that exist in BOTH A and B unless you narrow the type first.
2. **Conflicting Intersections** — Trying to intersect two primitives like `string & number`. This results in the `never` type because a value can't be both at once.
3. **Overcomplicating Unions** — If you have 10+ unions, it might be a sign that you need a better data structure or a base interface.
4. **Forgetting Type Guards** — When using a union, you almost always need to check which type you have before using it (e.g., using `typeof` or `instanceof`).

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Basic unions, intersections, and literal types |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Unions and Intersection Types — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types)
- [Combining Types — TypeScript Deep Dive](https://basarat.gitbook.io/typescript/type-system/union-types)

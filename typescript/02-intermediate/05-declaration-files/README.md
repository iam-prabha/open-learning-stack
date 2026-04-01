# Declaration Files (.d.ts)

## What is it?

**Declaration Files** (`.d.ts`) are the "Bridge" between the world of untyped JavaScript and the world of TypeScript. They allow you to describe the shape of an existing JavaScript library so that TypeScript can understand it, provide autocomplete, and check for errors, all without actually changing the original JavaScript code.

## Real-world analogy

Think of a declaration file like **a blueprint for a building that's already built**:
- **The Building (JavaScript)**: The actual structure. You can walk inside, but you don't have a map.
- **The Blueprint (.d.ts)**: A separate document that shows exactly where the rooms are, what the dimensions are, and what each room is for.
- **The Map (IDE)**: The blueprint allows you to navigate the building without getting lost (no `undefined` errors).
- **DefinitelyTyped**: A massive library of blueprints for almost every famous building in the world (`@types/node`, `@types/react`).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **`.d.ts`** | You are using a legacy JS library that doesn't have types | You are writing a new library in TypeScript (TS generates these for you automatically) |
| **`declare module`**| You need to define types for a third-party package | You are defining types for your own internal project files (use standard `.ts` files) |
| **`declare global`**| You are adding a new method to a built-in object like `Window` or `String` | You can achieve the same goal with a standard class or utility function |

## Common mistakes

1. **Forgetting `export`** — Declaration files are usually treated as "Ambient" (global) unless they contain an `export` or `import` statement.
2. **Duplicating implementation** — Putting actual logic (like `function add(a, b) { return a + b }`) inside a `.d.ts` file. These files should ONLY contain type definitions.
3. **Incorrect file naming** — Not ending the file with `.d.ts`.
4. **Namespace confusion** — Using `declare namespace` when a simple `declare module` would work better for modern ESM projects.

## Files in this folder

| File | Purpose |
|---|---|
| `my-lib.js` | A simulated untyped JS library |
| `my-lib.d.ts` | The declaration file for the library |
| `example.ts` | Using the JS library with full type-safety |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Declaration Files Guide — TS Handbook](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)
- [How to create your own .d.ts](https://www.typescriptlang.org/docs/handbook/declaration-files/templates.html)

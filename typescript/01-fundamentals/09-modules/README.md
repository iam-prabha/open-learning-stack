# Modules in TypeScript

## What is it?

TypeScript modules follow the standard ES Modules (ESM) syntax (`import` and `export`), but with one superpower: you can also **import and export Types and Interfaces**. This allows you to share data structures across your entire project without adding any extra weight to the compiled JavaScript, as type imports are removed during the build process.

## Real-world analogy

Think of TypeScript modules like **a modular shelving system**:
- **The Box (Module)**: Each shelf is its own self-contained unit.
- **The Items (Exports)**: You can put "Books" (functions/values) on the shelf and label them so others can use them.
- **The Instruction Manual (Types)**: You can also export the "Instructions" (Types/Interfaces) for how to build or use the box.
- **Custom Shipping**: When you ship the shelving unit to a customer (compile to JS), you keep the Books but throw away the Instruction Manual to save on weight (Type Erasure).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **`export`** | You want to make a function, class, or type available in other files | The item is a private helper used only within one file |
| **`import type`** | You are ONLY importing a type or interface | You also need to use a real class or function from that same file (use standard `import`) |
| **`export default`**| The file has one primary purpose (like a single large component) | You have a "library" file with many small utility functions (use named exports) |

## Common mistakes

1. **Forgetting `.ts` extensions** — Just like in JS, modern environments often require explicit extensions. In TS, you usually write `import { x } from "./file"`, and the compiler figures out the extension.
2. **Standard vs Type imports** — Using `import { User } from "./types"` when `User` is an interface. While this works, using `import type { User }` is clearer and can help with certain compiler optimizations.
3. **Circular Dependencies** — File A imports B, and B imports A. This can cause runtime errors where values are `undefined` or classes are not yet initialized.
4. **Namespace Overuse** — Using `import * as Utils` everywhere can make it harder for bundle-analyzers to "tree-shake" (remove) the functions you aren't actually using.

## Files in this folder

| File | Purpose |
|---|---|
| `types.ts` | Shared interfaces |
| `utils.ts` | Named and default exports |
| `example.ts` | Standard and Type-only imports |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Modules — TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/2/modules.html)
- [Working with Type Imports](https://www.typescriptlang.org/docs/handbook/2/modules.html#type-only-imports-and-exports)

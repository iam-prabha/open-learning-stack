# Types and Annotations

## What is it?

Type annotations are the most basic and fundamental feature of TypeScript. They allow you to explicitly specify what type of data a variable, function parameter, or return value should hold. This enables the TypeScript compiler to catch errors *before* you even run your code.

## Real-world analogy

Think of type annotations like **labels on storage bins**:
- **JavaScript**: A pile of unlabeled boxes. You don't know if a box contains "Shoes" (strings), "Tools" (objects), or "Batteries" (numbers) until you open it and try to use it. If you try to wear a battery as a shoe, you have a problem.
- **TypeScript**: Every box has a clear label from the factory. If you try to put a shoe into a box labeled "Batteries," the factory manager (the compiler) stops you immediately and says, "That doesn't go there!"

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Explicit Type** | Declaring variables that aren't immediately initialized | Simple assignments where TS can perfectly "infer" the type |
| **`any`** | **Almost never.** Only for migration from JS or extremely complex dynamic data | You are lazy or unsure of the type (try `unknown` instead) |
| **`primitive`** | Basic data like `string`, `number`, `boolean` | You are describing complex objects (use `interface` or `type`) |

## Common mistakes

1. **Over-annotating** — You don't need to write `const x: number = 5;`. TypeScript already knows `5` is a number (Type Inference).
2. **Using the 'any' escape hatch** — Using `any` turns off TypeScript's safety features for that variable. It defeats the purpose of using TS.
3. **Confusing 'string' (type) vs 'String' (wrapper)** — Always use the lowercase versions (`string`, `number`, `boolean`) as these are the actual primitives.
4. **Ignoring Compiler Errors** — TypeScript errors are hints to fix bugs. Using `// @ts-ignore` should be a last resort.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Basic primitives, arrays, and inference examples |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Basics — TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
- [The Basics — TS Tutorial](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html)

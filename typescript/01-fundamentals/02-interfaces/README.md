# Interfaces

## What is it?

An **Interface** in TypeScript is a powerful way to define the shape (structure) of an object. It acts as a contract that any object must follow. Unlike classes, interfaces don't exist at runtime (they are "erased" during compilation); they are purely for the compiler to check your data structures while you're coding.

## Real-world analogy

Think of an interface like **a Driver's License or a Passport**:
- **The Interface (Passport)**: It defines that "a person must have a photo, a name, and a date of birth."
- **The Object (You)**: You are a real person who provides that information. You don't "become" a passport; you merely "conform" to its requirements to travel.
- **Optional Property (`?`)**: A passport might have a "Middle Name" field that you can leave blank. It's still a valid passport.
- **Read-only (`readonly`)**: You cannot change your "Date of Birth" once the passport is issued.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Interface** | Describing the shape of objects, API responses, or function configs | Describing single values, unions, or primitives (use `type`) |
| **`readonly`** | Prohibiting properties from being changed after they are created | You expect the data to change over time (like a "Score" or "Counter") |
| **Index Signatures** | You don't know the exact names of all properties (e.g., `[key: string]: number`) | You have a fixed, known set of properties |

## Common mistakes

1. **Forgetting `readonly`** — Not using `readonly` for things that *shouldn't* change (like IDs) can lead to accidental mutations.
2. **interfaces vs Classes** — An interface defines *what* something looks like; a class defines *how* it behaves (methods and logic). Don't use a class if you just need to describe a data object.
3. **Overusing Index Signatures** — `{ [key: string]: any }` makes your code as unsafe as standard JavaScript. Be as specific as possible.
4. **Duplicate definitions** — Redefining the same interface instead of using **Extends** to add onto an existing one.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Basic interfaces, optional properties, and `readonly` |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Object Types — TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#interfaces)
- [Interface vs Types — The nuance](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)

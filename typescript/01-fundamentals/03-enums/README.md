# Enums

## What is it?

**Enums** (short for Enumerations) allow us to define a set of named constants. Using enums can make it easier to document intent or create a set of distinct cases. TypeScript provides both numeric and string-based enums. Unlike interfaces, enums *do* exist at runtime as real objects in your compiled JavaScript.

## Real-world analogy

Think of an enum like **a set of options on a remote control**:
- **The Enum (Remote)**: It has a fixed set of buttons: `POWER`, `VOLUME_UP`, `VOLUME_DOWN`, `MUTE`.
- **The Value**: You can't press a "Banana" button because it's not on the remote. You can only choose from the predefined set.
- **Label vs Value**: The button says `VOLUME_UP` (the Label), but inside the remote, it sends a specific signal like `2` (the Value).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Numeric Enum** | You need to map friendly names to internal status codes (0, 1, 2) | The numeric values might change or be confusing to debug |
| **String Enum** | Use when readability is key and you want the value to be clear in logs | You have a massive set of constants (might slightly increase bundle size) |
| **`const enum`** | You want the performance of an enum but don't need the object at runtime | You need to iterate over the enum values or look them up dynamically |

## Common mistakes

1. **Numeric auto-incrementing** — If you don't assign a value to a numeric enum, it starts at 0. Adding a new item at the beginning of the list will shift all subsequent values, which can break database records or API integrations.
2. **Reverse mappings** — Numeric enums allow you to look up the name from the value (`Status[0]`), but string enums do NOT.
3. **Using enums for everything** — Sometimes a simple **Union Type** (`type Direction = "Up" | "Down"`) is simpler and more performant than an enum.
4. **Confusing Enum vs Object** — Enums are types AND values. Objects are only values unless you use `typeof`.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Numeric vs String enums and their usage |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Enums — TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/enums.html)
- [Const Enums — Why they matter](https://www.typescriptlang.org/docs/handbook/enums.html#const-enums)

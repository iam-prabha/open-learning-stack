# Mapped Types

## What is it?

**Mapped Types** allow you to create new types based on an existing type by "looping" through every property and transforming it. They are essentially **for-each loops for types**. If you've ever used `Array.map()` in JavaScript, mapped types are the TypeScript equivalent for object structures.

## Real-world analogy

Think of a mapped type like **a factory line with specialized machines**:
- **The Box (Existing Type)**: A standard part with many components.
- **The Machine (Mapping Rule)**: You put the box through a "Paint Machine." It doesn't change the shape of the parts, but it changes their "Color" (Property Type).
- **Modifier (`-?`, `readonly`)**: You put the box through a "Standardization Machine" that removes all the "Optional" tags from the parts, making them all mandatory.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Mapped Type** | You need a variation of an existing type where every property changes in the same way (e.g., all fields become `boolean`) | You only need to create a simple, static type |
| **Modifier (`?`, `+`, `-`)**| Toggle optionality or read-only status for an entire type | You only need to change one or two properties |
| **Key Remapping (`as`)**| Renaming keys based on a pattern (e.g., prefixing with "get") | The key changes are completely random and don't follow a pattern |

## Common mistakes

1. **Mapping over unions** — Mapped types don't automatically "distribute" over unions in the way you might expect.
2. **Infinite loops** — Creating a mapped type that references itself in a way the compiler can't resolve.
3. **Overcomplicating Logic** — Trying to do too much in a single mapping. Sometimes using two utility types or a helper interface is clearer.
4. **Incorrect `keyof` usage** — Trying to map over something that isn't a valid set of keys.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Basic mapping, modifiers, and key remapping |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Mapped Types — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html)
- [Key Remapping in Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html#key-remapping-via-as)

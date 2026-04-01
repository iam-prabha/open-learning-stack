# Classes in TypeScript

## What is it?

TypeScript adds powerful features to the standard ES6 Classes. Specifically, it allows you to **type instance properties**, use **visibility modifiers** (like `private` and `protected`), and use a unique shorthand called **Parameter Properties** to significantly reduce boilerplate code.

## Real-world analogy

Think of a TypeScript class like **a building with security levels**:
- **Public (`public`)**: The lobby. Anyone can enter and walk around.
- **Private (`private`)**: The vault. Only people inside the building (the class itself) can access it.
- **Protected (`protected`)**: The employee lounge. Only people in this building OR in a subsidiary building (sub-classes) can enter.
- **Readonly (`readonly`)**: A plaque on the wall. You can see it, but you can't change what it says after it's installed.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Property Typing** | Every time you have data belonging to an instance | Leaving them implicitly typed as `any` |
| **`private`** | Hiding implementation details or sensitive data (like a password) | You need the property to be accessible to other classes |
| **`protected`** | Data that should be shared with children (sub-classes) but not the public | You don't plan on using inheritance |
| **Parameter Props** | Instantly declaring and initializing a property in the constructor | You have complex logic to perform before saving the data |

## Common mistakes

1. **Duplicate declaration** — Declaring `public name: string` at the top AND then again in the constructor `constructor(name: string) { this.name = name }`. Use the **Parameter Property** shorthand instead.
2. **Ignoring Visibility** — Leaving everything as the default (`public`). This makes your class harder to maintain because any other piece of code can change your internal state.
3. **Confusing `#private` vs `private`** — `#private` is a JavaScript feature that works at runtime. `private` is a TypeScript feature that only works during compilation. Usually, `private` is enough for most apps.
4. **Incorrect `super()` order** — Just like in JS, you must call `super()` before accessing `this`.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Classes, modifiers, parameter properties, and inheritance |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Classes — TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/2/classes.html)
- [Parameter Properties](https://www.typescriptlang.org/docs/handbook/2/classes.html#parameter-properties)

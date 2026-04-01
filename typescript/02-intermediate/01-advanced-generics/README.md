# Advanced Generics

## What is it?

In the Fundamentals track, we saw how Generics allow us to create flexible components. **Advanced Generics** take this further by allowing us to **constrain** what those types can be and provide **default** types if none are specified. This ensures that while our code is flexible, it still follows specific rules (like "This generic must have a `.length` property").

## Real-world analogy

Think of advanced generics like **a specialized charging station**:
- **Generics (Any Charger)**: A station that fits "any device." This is risky because you might try to charge a toaster with a phone charger.
- **Constraints (`extends`)**: A station that says, "I only fit devices that **extend** (follow the shape of) a USB-C input." Now you can't plug in the wrong thing, but you can still charge *any* USB-C phone, tablet, or laptop.
- **Defaults (=)**: If you don't say which cable you want, the station **defaults** to providing a standard 5V USB-C cable.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Constraints (`extends`)** | You need to access a specific property on a generic (like `arg.length` or `arg.id`) | You truly don't care about the object's properties |
| **Defaults (`= T`)** | You have a preferred "fallback" type for a generic class or function | Every user of the component should explicitly define their own type |
| **`keyof`** | Restricting a generic to be a valid key of an object | You are using hard-coded strings that might drift from the object's keys |

## Common mistakes

1. **Too many constraints** — Adding so many requirements that the generic is no longer flexible at all. At that point, just use a standard interface.
2. **Confusing Inference with Defaults** — Thinking the default type will be used even when TypeScript can clearly figure out a better type from the arguments. Defaults only kick in when inference fails or is not applicable.
3. **Circular Constraints** — Letting type T extend U, while U extends T.
4. **Incorrect `keyof` usage** — Trying to use `keyof` on a value instead of a Type.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Constraints, `keyof`, and default generic types |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Generic Constraints — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-constraints)
- [Default Types in Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-parameter-defaults)

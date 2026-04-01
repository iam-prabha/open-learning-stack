# Tuples and Arrays

## What is it?

In TypeScript, arrays and tuples allow you to manage collections of data with high precision:
- **Arrays**: Collections of the same type (like a list of numbers). They can have any length.
- **Tuples**: Special arrays with a **fixed number of elements**, where each element has a **specific type** corresponding to its position. Think of a tuple as a "typed record" inside an array.

## Real-world analogy

Think of the difference between **a Bag of Candy and a Bento Box**:
- **Array (Bag of Candy)**: A bag that contains many items, but they are all "Candy." You can add as many pieces as you want, but you expect every piece to follow the same basic rule (don't put a rock in the candy bag).
- **Tuple (Bento Box)**: A container with specifically sized compartments. The first compartment MUST hold "Rice," the second MUST hold "Fish," and the third MUST hold "Ginger." You can't put fish in the rice spot, and you can't add a 4th compartment without a new box.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Array (`T[]`)** | Standard lists of data (Users, Prices, Coordinates) | The position of elements in the list is critical to their meaning |
| **Tuple (`[T, U]`)** | Representing a strict pair of values (like `[Latitude, Longitude]` or `[Response, Error]`) | You have more than 3-4 elements (use an `Interface` or `Object` instead for clarity) |
| **`readonly`** | You want to prevent any modifications (push/pop/index change) to the list | You need to update the list over time |

## Common mistakes

1. **Tuples and `.push()`** — Warning! TypeScript will let you `.push()` to a tuple at runtime, but it won't let you access those extra elements via indexing (`tuple[3]`). Be careful not to treat a tuple as a growable list.
2. **Confusing names** — A tuple like `[number, string]` doesn't tell you what the number or string *is*. For larger sets of data, an object `{ id: 1, name: "Alice" }` is always better than a tuple `[1, "Alice"]`.
3. **Array Inference** — Forgetting that `const x = [1, 2]` is inferred as `number[]`, while `const x: [number, number] = [1, 2]` is a strict tuple.
4. **Infinite depth** — Nesting arrays inside tuples inside arrays. If it's more than 2 levels deep, consider creating an interface to simplify the structure.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Array basics, Multi-dimensional arrays, and Tuples |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Tuple Types — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types)
- [Array Types — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#arrays)

# Type-Level Programming

## What is it?

**Type-Level Programming** is the art of using TypeScript's type system to perform complex computations that usually happen at runtime. In TypeScript, the type system is **Turing Complete**, meaning you can write "programs" that run entirely within the compiler to transform, filter, and validate data structures with extreme precision.

## Real-world analogy

Think of type-level programming like **a programmable logic controller (PLC) in a factory**:
- **Standard Types**: Simple switches ("Is it on or off?").
- **Type-Level Programs**: A complex sequence of logic ("If the sensor detects a blue box AND it's taller than 10cm, then route it to the North wing, OTHERWISE strip its labels and send it to recycling").
- **Execution**: This logic doesn't run while the factory is shipping (Runtime); it's programmed into the machines before the first box ever arrives (Compile-time).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Recursive Types** | Handling deeply nested structures (e.g., `DeepPartial<User>`) | The nesting depth is shallow and predictable |
| **Tuple Manipulation**| Building safe APIs for things like `printf` or Route parameters | You can just use a simple Array or Object |
| **Type Arithmetic** | Enforcing strict relationships between multiple inputs | The logic is better handled by a standard runtime check |

## Common mistakes

1. **Recursion Limit** — TypeScript has a limit on how deep types can recurse (usually around 50-100 levels). If your types are too complex, you'll see a "Type instantiation is excessively deep" error.
2. **Readability Death** — Creating types so complex that no other developer (including your future self) can understand them. **Always add comments describing the logic.**
3. **Performance Hit** — Each complex type-level program adds work for the TypeScript compiler. Too many of these can make your IDE feel laggy.
4. **Trying to do too much** — Sometimes a `console.log` and a runtime test are better than a 50-line type-level validation.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | DeepPartial, Tuple manipulation, and string splitting |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Recursive Conditional Types — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#recursive-conditional-types)
- [Type-level programming in TypeScript](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html)

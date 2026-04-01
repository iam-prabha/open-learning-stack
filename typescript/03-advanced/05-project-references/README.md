# Project References

## What is it?

**Project References** allow you to structure your TypeScript programs into smaller, independent pieces. Instead of one massive `tsconfig.json` for your entire codebase, you can have multiple smaller ones that "reference" each other. This significantly improves build times and forces you to maintain a cleaner, more modular architecture.

## Real-world analogy

Think of project references like **building a modular space station**:
- **Common Logic (Core)**: The oxygen and power module. Every other module NEEDS it to function.
- **Project Reference**: The docking port that connects the Core to the Living Quarters.
- **Build System (`tsc --build`)**: The computer that knows: "If I change the solar panels on the Power module, I ONLY need to re-check the Living Quarters, not the entire station."
- **Performance**: You don't have to rebuild the whole station every time you change a lightbulb in one room.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Project Ref** | Building a Monorepo with shared logic between Backend and Frontend | You have a small, single-folder project |
| **`composite`** | Marking a sub-project as a dependency that others can import from | You are at the "Leaf" of your project (nothing imports you) |
| **`--build`** | Compiling multiple interconnected projects in the correct order | You only have one project (standard `tsc` is fine) |

## Common mistakes

1. **Forgetting `"composite": true`** — A project cannot be referenced by another unless it has this flag enabled in its `tsconfig.json`.
2. **Circular References** — Project A references B, and B references A. This is NOT allowed and will cause a build error.
3. **Incorrect Paths** — Using the wrong relative path in the `"references"` array.
4. **Out-of-sync builds** — Running `tsc` on a single sub-project and forgetting that its dependencies have changed (Always use `tsc --build` or `tsc -b`).

## Files in this folder

| File | Purpose |
|---|---|
| `core/tsconfig.json` | Simulated shared core project |
| `app/tsconfig.json` | Simulated application that references core |
| `example.ts` | Conceptual overview of the file structure |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Project References — TS Handbook](https://www.typescriptlang.org/docs/handbook/project-references.html)
- [tsc --build (Incremental Builds)](https://www.typescriptlang.org/docs/handbook/project-references.html#build-mode-for-typescript)

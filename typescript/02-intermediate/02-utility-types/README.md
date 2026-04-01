# Utility Types

## What is it?

TypeScript provides several **built-in utility types** to facilitate common type transformations. These utilities are available globally and allow you to take an existing type and "tweak" it (e.g., make all properties optional, or pick only a few specific fields) without having to manually redefine the whole structure.

## Real-world analogy

Think of Utility Types like **Photoshop Filters for your data**:
- **Original Image (Type)**: A high-resolution photo with many details (User with `id`, `name`, `email`, `password`).
- **Partial Filter (`Partial`)**: A "sketch" version. You can see the outlines, but many details might be missing (Updating a profile where you only change the `email`).
- **Crop Tool (`Pick/Omit`)**: Cutting out only the face of the person in the photo (`Pick<User, 'name'>`).
- **Grayscale Filter (`Readonly`)**: You can see the photo, but you can't add any new colors to it (The data can't be changed).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **`Partial<T>`** | Creating "Update" functions where only some fields are sent to the server | You need to ensure a specific property ALWAYS exists |
| **`Pick<T, K>`** | Extracting a subset of properties for a specific UI component | You end up picking 90% of the properties (just use the original type) |
| **`Omit<T, K>`** | Removing sensitive fields (like `password`) before sending data to the client | You only have 1-2 properties to keep (use `Pick` instead) |
| **`Record<K, T>`**| Mapping keys to a specific value type (e.g., a dictionary of status codes) | The keys are completely dynamic and unknown (use index signature) |

## Common mistakes

1. **Nesting Utilities** — `Partial<Pick<User, 'name'>>`. While valid, this can become hard to read. Sometimes creating a new named type is cleaner.
2. **Confusing `Pick` and `Omit`** — Using `Omit` to remove 10 fields when you only wanted to keep 2. Use `Pick` for "keep these" and `Omit` for "remove these."
3. **ReturnType on values** — Forgetting that `ReturnType` only works on *Types* of functions, not the function values themselves (`ReturnType<typeof myFunc>`).
4. **Over-using `Partial`** — Making every object partial "just in case." This loses the safety of knowing required fields like `id` exist.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Partial, Required, Pick, Omit, and Record |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Utility Types — TS Handbook](https://www.typescriptlang.org/docs/handbook/utility-types.html)
- [TypeScript Utility Types Guide](https://www.typescriptlang.org/docs/handbook/utility-types.html)

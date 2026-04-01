# Type Aliases

## What is it?

A **Type Alias** in TypeScript allows you to create a new name for an existing type. It doesn't create a "new" type; it merely points to the shape you've defined. Type aliases are incredibly versatile because they can describe primitives, unions, intersections, and object shapes — basically anything you can define in TypeScript.

## Real-world analogy

Think of a Type Alias like **a nickname for a complex recipe**:
- **The Long Type**: "Mix 2 eggs, 1 cup of flour, 1 cup of milk, and a pinch of salt." (Very wordy to repeat every time).
- **The Alias (Pancakes)**: You give this specific combination a name: `type Pancakes`. Now, whenever you want to eat, you just say "Give me some Pancakes."
- **Reusability**: If you decide to add sugar to the recipe, you only change the `type Pancakes` definition in one place, and every chef (function) using it is updated.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Type Alias** | Defining complex **Unions** or **Intersections** | Defining a simple object shape that might need to be extended (use `interface`) |
| **`type`** | Creating a name for a primitive (e.g., `type ID = string`) | You want the convenience of **Declaration Merging** (interfaces can have the same name multiple times; types cannot) |
| **`type`** | Describing the return type of a complex function | The type is very simple and used only once |

## Common mistakes

1. **Confusion with Interface** — While `type` and `interface` are similar, an interface is strictly for objects/functions and can be extended with `extends`. A type alias is more flexible but cannot be "merged" (you can't have two `type X` declarations in the same file).
2. **Circular references** — Trying to use a type inside itself without using an interface or a specific pattern.
3. **Overusing Primtive Aliases** — Creating a type `type MyString = string` for every variable can make the code harder to read rather than easier.
4. **Incorrect naming** — Using names that are too vague (like `Data` or `Object`).

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Basic type aliases, unions, and function types |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Type Aliases — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases)
- [Types vs Interfaces](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)

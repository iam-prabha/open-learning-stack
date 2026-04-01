# Decorators

> [!IMPORTANT]
> To use decorators in your project, you must enable `experimentalDecorators: true` in your `tsconfig.json` file.

## What is it?

**Decorators** provide a way to add both annotations and a meta-programming syntax for class declarations and members. They are functions that are called with information about the class or method they are "decorating," allowing you to modify their behavior or add metadata.

## Real-world analogy

Think of a decorator like **a post-it note or a sticker on a box**:
- **The Box (Class/Method)**: The actual logic.
- **The Sticker (Decorator)**: You put a "FRAGILE" sticker on the box. The sticker doesn't change what's *inside* the box, but it changes how the "Courier" (the runtime) handles the box.
- **Decorator Factory**: A machine that prints custom stickers (e.g., a sticker that says "Handle with care because it contains [Item Name]").

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Class Decorator** | You want to observe, modify, or replace a class definition entirely (e.g., adding a `createdAt` timestamp to every instance) | You can just use inheritance or a simple wrapper function |
| **Method Decorator** | Logging, timing, or access control (e.g., `@Log`, `@Authorize`) | The logic only needs to run once during class definition |
| **Property Decorator** | Injecting values or validating data (e.g., `@Required`) | You can handle the validation in the constructor |
| **Decorator Factory**| Passing arguments to your decorator (e.g., `@Role('admin')`) | Your decorator logic is static and doesn't need data from the outside |

## Common mistakes

1. **Forgetting `tsconfig`** — Not enabling `experimentalDecorators`.
2. **Incorrect Signature** — Each type of decorator (Class, Method, etc.) has a different set of arguments. Using the wrong one will result in a compile error.
3. **Overusing Decorators** — Turning your code into "Decorator Soup" where it's hard to follow the actual execution flow.
4. **Confusing with ES Decorators** — TypeScript's current decorators are "Experimental." There is a standard JavaScript decorator proposal that is slightly different.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Class, Method, and Property decorators |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Decorators — TS Handbook](https://www.typescriptlang.org/docs/handbook/decorators.html)
- [How Decorators Work — Visual Guide](https://www.typescriptlang.org/docs/handbook/decorators.html#class-decorators)

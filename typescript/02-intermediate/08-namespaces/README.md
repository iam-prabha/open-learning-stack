# Namespaces

> [!NOTE]
> Namespaces are a legacy feature. In modern TypeScript development, **ES Modules** (`import`/`export`) are much more common and officially recommended for almost all projects.

## What is it?

**Namespaces** (formerly called "Internal Modules") provide a way to logically group related code under a single global name. They help prevent name collisions in the global scope by wrapping your variables, functions, and classes in a named object container.

## Real-world analogy

Think of a namespace like **a labeled drawer in a workshop**:
- **The Workshop (Global Scope)**: A messy table where everything (tools, screws, glue) is thrown together.
- **The Drawer (Namespace)**: You add a drawer labeled "Plumbing" and put only those tools inside.
- **The Access**: To get a tool, you first go to the "Plumbing" drawer and then look for the "Wrench." 
- **Collision Prevention**: Now you can have another "Wrench" in the "Carpentry" drawer without getting them mixed up.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Namespace** | Maintaining legacy codebases that don't use modern module loaders | Building a new web or Node.js application (use ESM) |
| **Namespace** | Generating a single bundle for a simple browser script without a build tool like Webpack | Your project uses a bundler or a modern environment |
| **Nested Namespace**| Organizing extremely large, complex internal structures | A simple folder structure would be clearer |

## Common mistakes

1. **Confusing with Modules** — Thinking that namespaces and ES modules are the same. Namespaces are a TS-specific global object; ESM is a JavaScript standard with many files.
2. **Forgetting `export`** — Even inside a namespace, if you don't prefix a function with `export`, it remains private to that namespace and can't be used externally.
3. **Over-using Global Scope** — Since namespaces often attach to the `window` or `global` object, they can still lead to "Global Scope Pollution" if you're not careful.
4. **Incorrect Reference Paths** — Forgetting to use `/// <reference path="..." />` when splitting a namespace across multiple files.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Single and nested namespaces |
| `multi-file/` | Demonstration of namespaces across files |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Namespaces — TS Handbook](https://www.typescriptlang.org/docs/handbook/namespaces.html)
- [Namespaces vs Modules](https://www.typescriptlang.org/docs/handbook/namespaces-and-modules.html)

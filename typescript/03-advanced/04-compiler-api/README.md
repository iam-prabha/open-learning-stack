# TypeScript Compiler API

## What is it?

The **TypeScript Compiler API** allows you to use the TypeScript engine as a tool within your own JavaScript or TypeScript programs. Instead of just running `tsc` in the terminal, you can programmatically read, transform, and generate TypeScript code. You can build your own linters, automatic refactoring tools, or even generate documentation directly from your source code.

## Real-world analogy

Think of the Compiler API like **taking apart a car engine and using the parts to build a different machine**:
- **`tsc` (The Command)**: Like driving the car. You turn the key, and it goes (converts TS to JS).
- **Compiler API**: Like being a mechanic with a set of wrenches. You can open the hood, take out the "piston" (a function definition), measure its "bore" (the return type), and decide to replace it with a more "efficient" part (refactoring).
- **Abstract Syntax Tree (AST)**: The blueprint of the car engine that shows every bolt and wire.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **AST Transformation** | Automatically adding `try/catch` blocks to every function in a large codebase | You only need to change 2 or 3 files (do it manually) |
| **Type Checking** | Building a custom CI tool that checks for specific architectural rules | Standard ESLint or `tsc` handles the check |
| **Code Generation** | Generating API clients from a GraphQL or Swagger schema | You can just write a simple template string or use a mature tool |

## Common mistakes

1. **Learning Curve** — The API is massive and can be very intimidating. Start with small transformations before trying to build a full compiler plugin.
2. **Performance** — Programmatic compilation is "Expensive." If you run it on every file change in a large project, it will be slow.
3. **AST Complexity** — Forgetting that a "simple" line of code like `const x = 5` actually consists of dozens of AST nodes (VariableDeclaration, Identifier, NumericLiteral, etc.).
4. **Breaking Versioning** — The internal Compiler API can sometimes change between TypeScript versions. Always pin your `typescript` dependency.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Traversing the AST and finding function names |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Compiler API Documentation — TS Wiki](https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API)
- [AST Explorer](https://astexplorer.net/) (Crucial tool for visualizing code as a tree)

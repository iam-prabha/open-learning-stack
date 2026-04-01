# Modules (ESM)

## What is it?

Modules are a way to split your code into separate, smaller files. This helps with organization, reusability, and keeping your global scope clean. In modern JavaScript, we use **ES Modules (ESM)** with the `import` and `export` keywords.

## Real-world analogy

Think of modules like **Lego bricks**:
- Each brick (module) is self-contained. It has its own shape and color (internal logic).
- Some bricks have "studs" (exported functions/variables) that allow them to connect to other bricks.
- You can build a massive spaceship (application) by importing only the specific bricks you need for each part.
- If you lose one brick, you just replace that one; you don't have to throw away the whole ship.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Named Export** | Exporting multiple utility functions or constants from one file | You only have one primary thing to export (use `default`) |
| **Default Export** | Exporting exactly one thing (like a main class or a single component) | You want to force the importer to use original variable names |
| **`import * as Aliased`** | Importing everything from a large utility library | You only need one or two specific functions (destructure them instead) |

## Common mistakes

1. **Missing file extensions** — In vanilla JS modules, you MUST include the `.js` or `.mjs` extension in the import path: `import { x } from "./tools.js"`.
2. **Naming default exports** — You can name a default export whatever you want during import, but this can lead to confusion if different files use different names for the same thing.
3. **Circular Dependencies** — Module A imports B, and B imports A. This can cause strange `undefined` bugs or infinite loops.
4. **Incorrect type in HTML** — Forgetting `<script type="module">` when using imports in the browser.

## Files in this folder

| File | Purpose |
|---|---|
| `utils.mjs` | The module that exports functions |
| `example.mjs` | The main file that imports and uses those functions |
| `exercise.js` | Conceptual and code TODOs (Instructions on how to split code) |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [JavaScript modules — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
- [ES Modules — Node.js Docs](https://nodejs.org/api/esm.html)

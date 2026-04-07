# AGENTS.md — Open Learning Stack

## Repo Overview

A structured learning repository covering **Python, JavaScript, TypeScript, Go, and Rust** + **AI/ML** (math → ML → DL → LLMs → MLOps). Every topic folder contains exactly 4 files following a strict pattern.

## Commands

### Running files (no build step — just run)

| Language | Run example/exercise/solution |
|---|---|
| Python | `python example.py` |
| JavaScript | `node example.js` |
| TypeScript | `npx tsx example.ts` (no tsconfig — files are self-contained) |
| Go | `go run example.go` (no go.mod — files are self-contained) |
| Rust | `rustc example.rs && ./example` (no Cargo.toml — single-file programs) |

### Running a single exercise
```bash
cd python/02-intermediate/06-decorators/
python exercise.py   # fails until TODOs are filled in
python solution.py   # shows correct answers
```

### Running a single topic end-to-end
```bash
cd typescript/01-fundamentals/05-classes/
npx tsx example.ts    # read the demo
npx tsx exercise.ts   # fill in TODOs, then run
npx tsx solution.ts   # verify answers
```

### Linting / Formatting
**None configured.** This repo has no linters, formatters, typecheckers, or CI. Code quality is enforced by review against the 4-file pattern and style conventions below.

## 4-File Pattern (MANDATORY)

Every topic folder MUST contain exactly these 4 files:

| File | Purpose |
|---|---|
| `README.md` | Concept explanation: what it is, analogy, when to use/avoid, common mistakes, further reading |
| `example.[ext]` | One clean, runnable demo — annotated with WHY comments |
| `exercise.[ext]` | 6 TODOs + 1 challenge — with assert-based or try/except self-checking |
| `solution.[ext]` | Complete answers with WHY comments + alternative approaches + key takeaways |

To add a new topic: copy `_templates/` to the correct path (e.g. `python/01-fundamentals/11-new-topic/`), then fill in all 4 files.

## Code Style

### General (all languages)
- **File header**: `// example.ext - Topic description` (or `# example.py - Topic description`)
- **Section headers**: Numbered, e.g. `# 1. Basic decorator` or `// 1. Creating a Promise`
- **WHY comments**: Explain WHY an approach is used, not WHAT the code does. Use `# WHY: ...` inline or a `"--- Why it works ---"` block at the bottom of solutions.
- **Progressive complexity**: Sections go from basic → practical → advanced within each example file.
- **Self-contained**: No external dependencies. Each topic folder is a complete unit.
- **Completion signal**: Example/solution files end with a success print (e.g. `print("\n✅ All examples ran successfully!")`)

### Python
- **Naming**: `snake_case` for functions, variables, modules. `PascalCase` for classes.
- **Imports**: Standard library first, one per line, alphabetical order. No wildcard imports.
- **Decorators**: Always use `@functools.wraps(func)` to preserve metadata.
- **Private vars**: Leading underscore prefix (`_cache`).
- **Error handling**: `raise ValueError(...)` for validation; `try/except` in exercises for self-checking.
- **Exercise verification**: Use `try/except NameError` to detect unfilled TODOs.

### JavaScript
- **Naming**: `camelCase` for variables, functions, methods. `PascalCase` for classes.
- **Variables**: Prefer `const` over `let`. Never use `var`.
- **Functions**: Arrow functions for callbacks, `function` keyword for named declarations.
- **Error handling**: `.catch()` for promises; `console.error()` for error output.
- **Verification**: `console.log()` for visual verification.

### TypeScript
- **Naming**: `PascalCase` for classes/interfaces/types. `camelCase` for methods/properties/variables.
- **Types**: Explicit type annotations on function parameters and return types. Use `void` for no-return.
- **Visibility**: Use constructor parameter properties (`public name: string`) for brevity.
- **Error handling**: Compile-time errors demonstrated via commented-out code.

### Go (when populated)
- **Naming**: `camelCase` for unexported, `PascalCase` for exported identifiers.
- **Imports**: Grouped stdlib imports in parentheses, sorted alphabetically.
- **Error handling**: Return `error` as last return value; check with `if err != nil`.

### Rust (when populated)
- **Naming**: `snake_case` for functions/variables/modules. `PascalCase` for types/traits/enums.
- **Imports**: `use` statements at top, grouped by crate.
- **Error handling**: `Result<T, E>` with `?` operator; `panic!` only for unrecoverable errors.

## README.md Template Structure

```markdown
# [Topic Name]

## What is it?          ← 2-3 plain English sentences
## Real-world analogy   ← Relatable metaphor
## When to use it       ← Table: use when / avoid when
## Common mistakes      ← Numbered list with one-sentence explanations
## Files in this folder ← Table mapping files to purposes
## Go deeper            ← Links to official docs
```

## PR Checklist for New Topics

1. All 4 files present and follow templates exactly
2. `example.[ext]` runs with zero errors
3. `exercise.[ext]` has 6 TODOs + 1 challenge with verification
4. `solution.[ext]` runs with zero errors and includes WHY comments
5. README.md has all sections filled (analogy, use/avoid, mistakes)
6. Correct folder naming: `XX-category/NN-topic-name/` (zero-padded, sequential)

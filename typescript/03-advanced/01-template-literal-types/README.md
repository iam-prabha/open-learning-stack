# Template Literal Types

## What is it?

**Template Literal Types** are built on top of [String Literal Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#literal-types) and have the ability to expand into many strings via unions. They use the same syntax as JavaScript template literals (backticks), but they work at the **Type level**. This allows you to create complex string patterns and ensure that a string follows a very specific format.

## Real-world analogy

Think of a template literal type like **a custom rubber stamp kit**:
- **The Base Stamp**: You have a set of prefixes: `[User, Admin, Guest]`.
- **The Suffixes**: You have a set of actions: `[Logged, Updated, Deleted]`.
- **The Expansion**: When you combine them (`${Prefix}_${Suffix}`), the kit automatically creates every possible combination: `User_Logged`, `Admin_Deleted`, etc.
- **Validation**: If you try to stamp `Guest_Hacked`, the ink won't stick because it's not a pre-manufactured combination in your kit.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Template Type** | Creating specific string patterns like CSS properties (`margin-top`, `padding-left`) | The string can be literally anything |
| **Union Expansion**| Generating combinations of events or keys (e.g., `onKeyUp`, `onKeyDown`) | You only have 2 or 3 static strings |
| **Mapping keys** | Combined with Mapped Types to rename properties (e.g., `get${Name}`) | You don't need the string to be predictable |

## Common mistakes

1. **Massive Unions** — If you combine two unions of 100 items each, you get 10,000 types. This can crash the TypeScript compiler or make your IDE extremely slow.
2. **Infinite Recursion** — Trying to create an infinitely long string pattern.
3. **Complexity overload** — Using template types for things that should just be simple variables or enums.
4. **Incorrect delimiters** — Using the wrong characters (like regular quotes) instead of backticks.

## Files in this folder

| File | Purpose |
|---|---|
| `example.ts` | Basic patterns, union expansion, and casing helpers |
| `exercise.ts` | 6 TODOs + 1 challenge |
| `solution.ts` | Answers with WHY comments |

## Go deeper

- [Template Literal Types — TS Handbook](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html)
- [String Manipulation Utilities](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html#uppercase-lowercase-capitalize-and-uncapitalize)

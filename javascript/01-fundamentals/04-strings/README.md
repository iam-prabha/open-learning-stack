# Strings and Template Literals

## What is it?

In JavaScript, strings are used to represent text. Modern JavaScript provides **Template Literals** (using backticks `` ` ``) which are much more powerful than standard single (`'`) or double (`"`) quotes. They allow for easy variable injection and multi-line strings.

## Real-world analogy

Think of strings like **labels on a filing system**:
- **Standard Quotes (' ')**: A **handwritten label**. If you want to add a date, you have to cut the label, stick a new piece on, and tape it together (`"Date: " + dateVal`).
- **Template Literals (` `)**: A **digital label**. You can design it with placeholders (`${dateVal}`) that automatically fill in the correct information. It's cleaner, faster, and much harder to mess up.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Template Literals** | Almost always. Especially for dynamic text or multi-line strings | Very short, static strings where `' '` is faster to type |
| **`.includes()` / `.startsWith()`** | Checking for substrings (modern, readable) | Using old `.indexOf() !== -1` checks |
| **`.trim()` / `.toLowerCase()`** | Cleaning up user input | You need the original formatting for some reason |
| **`.split()`** | Converting a CSV or space-separated string into an array | You are just iterating over characters (use a `for...of` loop) |

## Common mistakes

1. **Confusing single/double/backtick quotes** — You cannot start with `'` and end with `"`.
2. **Forgetting `.toUpperCase()` returns a NEW string** — Strings in JS are immutable. `s.toUpperCase()` does NOT change `s`.
3. **Escaping hell** — Trying to use `\n` and `\"` in standard strings when backticks would handle it automatically.
4. **Using `.substring()` vs `.slice()`** — They are similar but have different rules for negative numbers. Stick to `.slice()`.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of template literals, multi-line strings, and common methods |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Strings — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
- [Template Literals — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)

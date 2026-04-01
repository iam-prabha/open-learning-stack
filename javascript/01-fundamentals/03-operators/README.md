# Operators

## What is it?

Operators are symbols used to perform operations on values (operands). JavaScript includes standard arithmetic, comparison, and logical operators, as well as some unique ones like the **Strict Equality** operator (`===`) and the **Nullish Coalescing** operator (`??`).

## Real-world analogy

Think of operators like **tools in a workshop**:
- **Arithmetic (+, -, *, /)**: Measuring tapes and saws. They change the physical dimensions of your materials.
- **Comparison (==, ===, <, >)**: Levels and rulers. They tell you if two pieces of wood are the same length or which one is longer.
- **Logical (&&, ||, !)**: Safety switches. "If the guard is down AND the power is on, THEN start the saw."

## When to use it

| Operator | Use when... | Avoid when... |
|---|---|---|
| **`===`** (Strict) | Always, for comparing both value and type | `==` (Loose), which performs unpredictable type coercion |
| **`&&` / `||`** | Complex logical conditions or default values | Over-nesting them (use early returns instead) |
| **`??`** | Providing a default when a value is `null` or `undefined` | Using `||` if `0` or `""` are valid non-null values |
| **`++` / `--`** | Incrementing counters in loops | Using them inside complex expressions (confusing order of ops) |

## Common mistakes

1. **`==` vs `===`** — `0 == ""` is `true`, but `0 === ""` is `false`. Always use `===`.
2. **Modulo vs Remainder** — `%` in JS is the remainder operator. It handles negative numbers differently than Python's modulo.
3. **Operator Precedence** — Forgetting that `*` happens before `+`. Use parentheses `( )` to be explicit.
4. **Truthy/Falsy confusion** — In JS, `0`, `""`, `null`, `undefined`, and `NaN` are all "falsy". Everything else is "truthy".

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of arithmetic, comparison, logic, and nullish coalescing |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Expressions and Operators — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)
- [Operator Precedence Table — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)

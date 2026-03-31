# Operators

## What is it?

Operators are special symbols that carry out arithmetic, logical, and relational computations. In Python, operators act on **operands** (values or variables) to produce a result. They are the "verbs" of your programming language, defining how data interacts.

## Real-world analogy

Think of operators like the **buttons on a calculator**. `+` adds numbers, `-` subtracts them, and `*` multiplies them. Logical operators like `and` or `or` are like the rules in a game: "If you have a key AND you are at the door, you can enter." Comparison operators like `>` are like comparing the height of two people to see who is taller.

## When to use it

| Category | Use when... | Example |
|---|---|---|
| **Arithmetic** | Performing mathematical calculations | `total = price * quantity` |
| **Comparison** | Comparing two values to get a boolean | `is_over_age = age >= 18` |
| **Logical** | Combining boolean values | `is_valid = is_authorized and is_logged_in` |
| **Assignment** | Assigning and updating values in one step | `score += 10` |
| **Membership** | Checking if a value is in a collection | `if "apple" in basket:` |

## Common mistakes

1. **Confusing `=` with `==`** — `=` is for assignment (give a name to a value); `==` is for comparison (check if two values are equal).
2. **Dividing by zero** — `10 / 0` will raise a `ZeroDivisionError`.
3. **Asssuming `/` returns an integer** — In Python 3, `/` always returns a float (e.g., `5 / 2` is `2.5`). Use `//` for integer (floor) division.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of all common Python operators |
| `exercise.py` | 6 TODOs + 1 challenge on arithmetic and logic |
| `solution.py` | Answers with explanations for operator precedence |

## Go deeper

- [Python Operators — Official Docs](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Operator Precedence — Official Docs](https://docs.python.org/3/reference/expressions.html#operator-precedence)

# Loops

## What is it?

Loops are used to repeat a block of code multiple times. JavaScript provides several types of loops, ranging from the classic `for` loop to modern iterators like `for...of` and `for...in`.

## Real-world analogy

Think of loops like **a track athlete running laps**:
- **`for` loop**: A planned workout. "Start at lap 1, run until lap 10, increment by 1 lap each time."
- **`while` loop**: Running until exhausted. "As long as `energy > 0`, keep running." You don't know exactly how many laps it will be.
- **`for...of`**: Handing out water to every runner on the track. "For every `runner` of `track`, give water." You care about the **item** (the runner).
- **`for...in`**: Inspecting the lockers. "For every `locker_number` in `locker_room`, check the contents." You care about the **keys/indices**.

## When to use it

| Loop Type | Use when... | Avoid when... |
|---|---|---|
| **`for`** | You need precise control over the index/counter | Simple iteration over an array (use `for...of`) |
| **`for...of`** | Iterating over values in an Array or String | Objects (use `for...in` or `Object.entries`) |
| **`for...in`** | Iterating over keys of an Object | Arrays (it's slower and can have unexpected order) |
| **`while`** | You don't know the end point in advance | You have a fixed collection (use a `for` variant) |

## Common mistakes

1. **Infinite loops** — Forgetting to increment the counter in a `while` loop: `while (true) { }`.
2. **Infinite `for...in` on arrays** — It iterates over property names (strings), not indices (numbers), which can break math logic.
3. **Off-by-one errors** — Using `i <= arr.length` instead of `i < arr.length`.
4. **Modifying the collection while looping** — Deleting items from an array while iterating over it can skip elements.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of for, while, for...of, and for...in |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Loops and iteration — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration)
- [for...of — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
- [for...in — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)

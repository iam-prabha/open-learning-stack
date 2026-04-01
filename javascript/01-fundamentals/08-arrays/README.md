# Arrays

## What is it?

Arrays in JavaScript are ordered lists of values. Unlike some languages, JS arrays can hold a mix of different data types and can grow or shrink in size automatically. Modern JavaScript provides powerful methods and syntax (like **spread** and **destructuring**) for working with arrays efficiently.

## Real-world analogy

Think of an array like **a train with many cars**:
- **Index**: Each car is numbered starting from 0.
- **Value**: The cargo inside each car. One car could have coal (a string), another could have gold (a number), and another could have passengers (an object).
- **Methods**: Tools to modify the train. You can add a car to the back (`push`), remove it from the front (`shift`), or split the train into two pieces (`slice`).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Array** | Storing an ordered list of similar items | You need to store unique values with no duplicates (use `Set`) |
| **`.map()` / `.filter()`** | Transforming or filtering list data without changing the original array | You just need a simple loop (use `for...of`) |
| **Spread (`...`)** | Creating copies or merging multiple arrays | You are working with extremely large arrays (it can be memory-intensive) |
| **Destructuring** | Quickly extracting values into variables: `[a, b] = arr` | You only need one value from a very long array |

## Common mistakes

1. **Incorrect indices** — Array indices start at 0. The last item is at `arr.length - 1`.
2. **Confusing `.slice()` vs `.splice()`** — `.slice()` returns a COPY; `.splice()` mutates the ORIGINAL array.
3. **Using `push()` when you want a new array** — `push()` changes the original array. If you want a new one, use `[...old, new]`.
4. **`typeof []` is `"object"`** — As seen in the data types topic, always use `Array.isArray(arr)` to check.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of push/pop/shift/unshift, slice/splice, map/filter, and destructuring |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Arrays — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Array Methods Reference — W3Schools](https://www.w3schools.com/jsref/jsref_obj_array.asp)

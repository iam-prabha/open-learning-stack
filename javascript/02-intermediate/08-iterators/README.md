# Iterators

## What is it?

Iterators are objects that define a sequence and potentially a return value upon its completion. Specifically, an iterator is any object which implements the **Iterator protocol** by having a `next()` method that returns an object with two properties: `value` and `done`. The **Iterable protocol** allows JavaScript objects to define or customize their iteration behavior, such as what values are looped over in a `for...of` construct.

## Real-world analogy

Think of an iterator like **a deck of cards**:
- **The Deck (Iterable)**: The collection of cards that you can go through one by one.
- **The Dealer (Iterator)**: The process of dealing the cards. The dealer has a standard way to give you the `next()` card.
- **`next()`**: You ask the dealer for a card. They give you a card (`value: "Ace of Spades"`) and tell you if there are more left (`done: false`).
- **End of Deck**: Eventually, the dealer says "No more cards" (`value: undefined`, `done: true`).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **`for...of`** | You want to loop over values of an array, string, or any custom iterable | Looping over plain object keys (use `for...in` or `Object.entries`) |
| **`Symbol.iterator`** | You want to make your own custom class/object loopable | A simple array property on your object is easier to iterate over |
| **Generators** | You need to produce a sequence of values lazily or manage complex state | A simple array can store all the values you need upfront |

## Common mistakes

1. **Forgetting `.next()` structure** — An iterator must return an object with BOTH `value` and `done`. If one is missing, `for...of` will fail or produce an infinite loop.
2. **Confusing Iterators vs Iterables** — An **Iterable** is the object (like an Array); an **Iterator** is the temporary "pointer" used during the loop.
3. **Modifying data during iteration** — Adding or removing items from the collection while iterating can cause index shifts and skip elements.
4. **Iterating over plain objects** — Plain objects (`{ }`) are NOT iterable by default in JS. You must either use `Object.keys()` or implement `Symbol.iterator` yourself.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | basic use of for...of, manual iteration, and custom iterators |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Iterators and generators — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_generators)
- [Iterables — JavaScript.info](https://javascript.info/iterable)

# Prototypes

## What is it?

In JavaScript, objects have a special hidden property called `[[Prototype]]` (accessible via `__proto__` or `Object.getPrototypeOf`). This property points to another object, creating what we call the **Prototype Chain**. When you try to access a property or method on an object, JS first looks at the object itself. If it doesn't find it there, it follows the chain up to the prototype, and then the prototype's prototype, until it either finds the property or reaches `null`.

## Real-world analogy

Think of prototypes like **biological DNA**:
- **You (The Object)**: You have your own unique traits (properties like height or eye color).
- **Your Parents (The Prototype)**: If someone asks about your "Last Name," you "inherit" it from your parents. You don't have a unique last name stored just on you; you look up the family tree.
- **Ancestors (The Chain)**: Your parents inherited traits from their parents. The "JSON" of humanity goes back to a common ancestor (like `Object.prototype`).
- **Override**: You can choose to change your last name. Now, when people ask for your last name, they find it directly on "You" and stop looking up the chain.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Prototypes** | You want to share methods across thousands of instances to save memory | You are using modern ES6 Classes (which handle prototypes for you automatically) |
| **`Object.create()`** | You need to create an object with a specific prototype without using a constructor | You just need a simple data container (use `{}`) |
| **Polyfills** | You are adding a missing method to a global prototype (like `Array.prototype.myNewSum`) | In production code of large teams (modifying globals is generally considered a "bad practice") |

## Common mistakes

1. **Polluting Global Prototypes** — Adding methods to `Object.prototype` affects EVERY object in your application, which can cause breaks in libraries or built-in functions.
2. **Infinite Loops** — Accidentally pointing an object's prototype to itself.
3. **Confusing `prototype` vs `__proto__`** — `Function.prototype` is what the constructor *gives* to new objects; `__proto__` is what the object *has* to look up.
4. **Performance** — Very deep prototype chains can slow down property access because JS has to "climb" many levels.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | basic prototyping, `Object.create`, and the chain in action |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Prototypes — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)
- [Prototypes, __proto__ — JavaScript.info](https://javascript.info/prototypes)

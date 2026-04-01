# Objects

## What is it?

Objects are the heart of JavaScript. They are collections of **key-value pairs**, where keys are strings (or symbols) and values can be anything — including other objects or functions (which we call **methods**). Modern JavaScript provides concise syntax for creating, merging, and extracting data from objects.

## Real-world analogy

Think of an object like **a smartphone**:
- **Properties (Values)**: Its state. `model: "iPhone"`, `battery: 85`, `isLocked: true`.
- **Methods (Functions)**: Its actions. `unlock()`, `takePhoto()`, `sendText()`.
- **Destructuring**: Pulling out just the parts you need. "I just want the **battery** level and the **model** name to show on my smartwatch."

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Object Literal `{}`** | Grouping related data and functions together | Sequential, ordered data (use `Array`) |
| **Bracket Notation `[]`** | Accessing a property using a dynamic variable: `obj[keyVar]` | The property name is fixed and known (use dot notation `.`) |
| **Object Shorthand** | Key and variable have the same name: `{ name }` instead of `{ name: name }` | You want to rename the key |
| **Destructuring** | Extracting multiple values into clean variables | You only need one deep property (use dot notation) |

## Common mistakes

1. **Confusing Objects with JSON** — Objects are a JS data structure; JSON is a string format for data exchange. Objects can contain functions; JSON cannot.
2. **Accessing undefined properties** — If `user.address` is undefined, `user.address.zip` will crash. Use **Optional Chaining** (`?.`).
3. **Reference traps** — `const copy = original` doesn't copy the object; it points both variables to the **same** object in memory.
4. **Forgetting `this` in methods** — To access an object's own properties inside a method, you must typically use `this.prop`.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of creation, methods, shorthand, destructuring, and optional chaining |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Objects — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
- [Working with Objects — MDN Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects)

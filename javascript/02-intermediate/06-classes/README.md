# Classes

## What is it?

Classes in JavaScript are a template for creating objects. Introduced in ES6, they provide a much cleaner and more familiar syntax for OOP (Object-Oriented Programming) compared to the older prototype-based approach. While JS is still prototype-driven under the hood, classes make it easier to define structures, methods, and inheritance.

## Real-world analogy

Think of a class like **a blueprint for a house**:
- **The Blueprint (Class)**: The design. It says "A house has a number of bedrooms, a color, and a door that can be opened." It isn't a physical house yet.
- **The House (Instance)**: When you build the house from the blueprint. You might build a "Blue House with 3 beds" and a "Red House with 2 beds." These are different houses, but they came from the same design.
- **Renovations (Inheritance)**: You take the "House" blueprint and add "Solar Panels" and "A Pool." This is a new "Luxury House" blueprint that inherits all the basic "House" features.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Class** | Creating multiple objects that share the same properties and methods | You only need one single, simple data object (use an object literal `{}`) |
| **`constructor`** | Initializing data for every new instance (like setting a name or ID) | You don't have any unique starting data for the object |
| **`extends`** | Creating a specialized version of a base class (Inheritance) | You are creating deep, complex trees of inheritance (Inheritance can get messy; favor composition) |
| **`static`** | Creating utility functions that belong to the Class, but not specific instances | The function needs to access instance data (like `this.name`) |

## Common mistakes

1. **Forgetting `new`** — You MUST use the `new` keyword to create an instance: `const car = new Car()`.
2. **Missing `super()`** — If you `extend` a class, your constructor MUST call `super()` before using `this`.
3. **Misusing `this`** — In classes, `this` refers to the specific instance being created. Forgetting to bind `this` in callbacks can lead to `undefined` errors.
4. **Over-engineering** — Many things in JS can be solved with simple functions. Only use classes when you genuinely need to manage persistent state across multiple instances.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | basic class syntax, constructors, methods, and inheritance |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Classes — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [Class inheritance — JavaScript.info](https://javascript.info/class-inheritance)

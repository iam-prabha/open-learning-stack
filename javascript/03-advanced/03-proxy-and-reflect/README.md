# Proxy and Reflect

## What is it?

**Proxy** and **Reflect** are powerful meta-programming features introduced in ES6.
- **Proxy**: Allows you to create an object that can intercept and redefine fundamental operations for another object (like property lookup, assignment, enumeration, function invocation, etc.).
- **Reflect**: A built-in object that provides methods for interceptable JavaScript operations. It's essentially the companion to Proxy, making it easy to perform the "default" behavior inside a proxy trap.

## Real-world analogy

Think of a Proxy like **a personal firewall or a middle-man**:
- **The Object**: A secret bank vault.
- **The Proxy**: A security guard standing in front of the vault.
- **Traps (`get`, `set`)**: When you try to put something in (set) or take something out (get), the guard stops you.
- **Interception**: The guard checks your ID (validation), logs the time (logging), or even gives you a fake version of what's inside (mocking) before letting you through.
- **Reflect**: The guard's special key that lets them perform the actual vault operation once they've finished their checks.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Proxy** | Implementing **validation**, logging, profiling, or data binding (like in Vue.js) | You only need simple access to object properties (Proxy has a performance cost) |
| **Reflect** | Writing clean Proxy traps or performing meta-programming operations | Standard object syntax like `obj.prop` is sufficient |
| **Traps** | Intercepting operations that aren't possible with standard getters/setters (like deleting or checking `in`) | You have a small number of known properties to watch |

## Common mistakes

1. **Performance overhead** — Because EVERY access goes through a function call, Proxies are slower than standard objects. Use them sparingly in performance-critical loops.
2. **Infinite loops** — Accessing the proxy object *inside* its own trap without using `Reflect`.
3. **Misusing 'this'** — When an object is wrapped in a Proxy, its internal `this` points to the proxy, which can break some built-in behaviors or private fields.
4. **Incorrect trap signatures** — Forgetting that most traps take `(target, property, receiver)` as arguments.

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of basic traps (get/set), validation, and Reflect usage |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Proxy — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
- [Reflect — MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect)

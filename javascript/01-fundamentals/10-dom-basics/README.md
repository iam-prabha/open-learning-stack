# DOM Basics

## What is it?

The **Document Object Model (DOM)** is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects. That way, programming languages can connect to the page.

## Real-world analogy

Think of the DOM like **a remote control for a TV**:
- **The TV**: The raw HTML/CSS on the screen.
- **The Remote (DOM)**: The bridge that lets you change the channel (content), volume (styles), or turn it off (remove elements) without physically opening the back of the TV.
- **Buttons (Events)**: Clicking a button on the remote triggers a circuit (Event Listener) that performs an action.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **`document.querySelector()`** | Selecting elements using CSS selectors (modern and powerful) | Using old `getElementById` unless performance is absolutely critical |
| **`addEventListener()`** | Responding to user clicks, typing, or scrolling | Using inline `onclick="..."` in HTML (messy and hard to maintain) |
| **`.textContent`** | Changing only the text inside an element (safe) | Using `.innerHTML` for user-provided data (Cross-Site Scripting risk) |
| **`.classList`** | Adding/removing CSS classes to change styles | Changing individual styles like `.style.color = "red"` (keep styles in CSS) |

## Common mistakes

1. **Running script before DOM is ready** — If your `<script>` is in the `<head>`, it might run before the elements exist! Use `defer` or put the script at the bottom of `<body>`.
2. **Infinite event loops** — Accidentally triggering an event inside its own listener.
3. **Memory leaks** — Adding thousands of event listeners to a list instead of using **Event Delegation** on the parent.
4. **Case sensitivity** — `querySelector(".myClass")` works, but `.myclass` won't if the CSS is capitalized.

## Files in this folder

| File | Purpose |
|---|---|
| `index.html` | A simple page to host the DOM exercise |
| `example.js` | Demos of selection, event listening, and class manipulation |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Introduction to the DOM — MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [DOM Manipulation — JavaScript.info](https://javascript.info/dom-nodes)

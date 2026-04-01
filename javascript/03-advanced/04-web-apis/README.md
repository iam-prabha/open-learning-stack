# Web APIs

## What is it?

Web APIs are built-in interfaces provided by the browser (or environment) that allow you to perform complex tasks that aren't part of the core JavaScript language itself. This includes making network requests (**Fetch**), storing data (**LocalStorage**), handling concurrency (**Web Workers**), and interacting with the hardware (Camera, Sensors).

## Real-world analogy

Think of Web APIs like **the tools in a workshop**:
- **JavaScript**: The person working in the shop.
- **The Workshop (Browser)**: Provides specialized machines that the person can't build themselves.
- **Fetch API**: A delivery truck that brings in materials from the outside world.
- **LocalStorage**: A locker where you can put tools away and find them exactly where you left them tomorrow morning.
- **Web Workers**: Hiring an apprentice to do a long, boring task (like sanding wood) in a separate room so you can keep building the main structure without stopping.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Fetch** | Getting data from a server or posting updates | You only need simple, static local data |
| **LocalStorage** | Saving user preferences (Theme, Session tokens, Drafts) | Storing sensitive data like passwords (it's not encrypted!) |
| **Web Workers** | Performing heavy calculations (Big data processing, Image manipulation) | Simple, quick tasks (the overhead of starting a worker might be slower) |
| **IntersectionObserver**| Implementing "infinite scroll" or lazy-loading images | The page is very simple and doesn't scroll much |

## Common mistakes

1. **Blocking the UI with Fetch** — Fetch is async, but processing a massive 20MB JSON response in the main thread will still freeze the UI. Use a worker for the processing.
2. **Exceeding Storage limits** — LocalStorage only has ~5MB of space. If you try to store more, it will throw an error and crash your script.
3. **Fetching without Error handling** — `fetch()` only rejects if there's a network error. An HTTP 404 or 500 is considered a "success" (response.ok = false). You must check `response.ok` manually.
4. **LocalStorage on Server** — LocalStorage is a **Web** API. It doesn't exist in Node.js (unless using a library).

## Files in this folder

| File | Purpose |
|---|---|
| `example.js` | Demos of Fetch, LocalStorage, and a simple Worker check |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Introduction to Web APIs — MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- [Fetch API — MDN](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Web Workers — MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API)

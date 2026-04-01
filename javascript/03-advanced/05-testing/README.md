# Testing

## What is it?

Testing is the process of verifying that your code behaves exactly as expected. In the JavaScript ecosystem, **Jest** is the most popular framework for this. Testing isn't just about finding bugs; it's about **documentation** (showing how code should work) and **confidence** (knowing that a new change didn't break an old feature).

## Real-world analogy

Think of testing like **pre-flight checks on a plane**:
- **Units (`05-testing`)**: Checking the individual bolts, sensors, and fuel gauges. Each part is tested in isolation.
- **Integration**: Checking if the engines, wings, and fuel systems work together correctly.
- **End-to-End (E2E)**: Flying the entire plane on a simulated route to see if it reaches the destination.
- **Manual Testing**: A pilot looking around and saying, "Yep, it looks like a plane."

## When to use it

| Test Type | Use when... | Avoid when... |
|---|---|---|
| **Unit Test** | Verifying a pure function (like `add(a, b)` or `formatDate(d)`) | Testing complex UI interactions (use E2E) |
| **Snapshots** | Ensuring your UI component's HTML structure doesn't change unexpectedly | The output changes frequently by design |
| **Mocks** | Simulating a database or API response so your tests are fast and offline | You need to verify the actual connection to the server |
| **Code Coverage**| Identifying parts of your app that aren't being tested at all | Striving for 100% at the cost of writing bad, useless tests |

## Common mistakes

1. **Testing Implementation instead of Behavior** — If your test breaks just because you renamed a private variable, your test is too coupled to the implementation.
2. **Slow Tests** — Making real network calls or waiting for `setTimeout` to finish. Use **Mocks** and **Jest Timers** to make tests instant.
3. **Logic in Tests** — If your test code is as complex as your source code, you'll need tests for your tests! Keep them simple and flat.
4. **Flaky Tests** — Tests that fail sometimes and pass other times (usually due to random numbers or timing issues).

## Files in this folder

| File | Purpose |
|---|---|
| `math.js` | Simple functions to be tested |
| `math.test.js` | Jest-style test suites (Conceptual syntax) |
| `exercise.js` | 6 TODOs + 1 challenge |
| `solution.js` | Answers with WHY comments |

## Go deeper

- [Jest Documentation](https://jestjs.io/docs/getting-started)
- [JavaScript Testing Best Practices — Goldbergyoni](https://github.com/goldbergyoni/javascript-testing-best-practices)

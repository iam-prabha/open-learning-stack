# Testing

## What is it?

Testing is the practice of writing code to verify that your application code works as expected. In Python, there are two dominant tools:
1. **unittest**: The built-in library (inspired by JUnit). Uses a class-based approach.
2. **pytest**: A powerful, popular third-party framework that uses simple functions and `assert` statements. It is the industry standard for modern Python.

## Real-world analogy

Think of testing like a **car factory quality check**:
- **Unit Testing**: Testing the brakes, the engine timing, and the door locks individually before they are put together.
- **Integration Testing**: Testing how the brakes and the engine work together when the car is moving.
- **Assertion**: The "pass/fail" sensor. If a sensor says "Brake pressure should be 50" and it's 20, the red light flashes (test fails).

## When to use it

| Use when... | Avoid when... |
|---|---|
| You want to ensure refactoring doesn't break existing features | You are writing throwaway code for a one-time script |
| The logic is complex and has many edge cases | The code is purely declarative (e.g., just a list of constants) |
| Building production-grade software | You're in "exploratory" mode, just seeing if an API works |

## Common mistakes

1. **Not testing edge cases** — Only testing "happy paths" like `add(2, 2)` instead of `add(None, 0)` or `add("a", 1)`.
2. **Brittle tests** — Tests that break every time you change a variable name, even if the logic is the same. Test *behaviour*, not implementation.
3. **Hardcoding results** — Forgetting to mock external calls (like databases or APIs), making tests slow and flaky.
4. **Too many assertions in one test** — If one fails, the rest don't run, and you don't know the full state. Keep tests focused.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | basic unittest and pytest syntax, mocking with unittest.mock |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Testing Your Code — Python Guide](https://docs.python-guide.org/writing/tests/)
- [unittest — Official Docs](https://docs.python.org/3/library/unittest.html)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)

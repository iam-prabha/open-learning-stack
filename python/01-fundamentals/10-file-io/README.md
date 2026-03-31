# File IO

## What is it?

File IO (Input/Output) allows your Python program to interact with files on your computer's storage. You can read data from files (Input) and write data to files (Output). In Python, we use the built-in `open()` function and the `with` statement to manage files safely.

## Real-world analogy

Think of File IO like **writing in a notebook**.
- **Opening a file** is like taking your notebook out of your bag.
- **Reading** is like looking at what's already written on the pages.
- **Writing** is like using a pen to put new words on the paper.
- **Closing a file** is like putting your notebook back in your bag. If you forget to close it, the pages might get crumpled or lost!

## When to use it

| Mode | Use when... | Example |
|---|---|---|
| **'r' (Read)** | You want to read an existing file | `open("data.txt", "r")` |
| **'w' (Write)** | You want to create a new file or overwrite an existing one | `open("output.txt", "w")` |
| **'a' (Append)**| You want to add new data to the end of an existing file | `open("log.txt", "a")` |
| **with statement**| You want to ensure the file is closed automatically | `with open(...) as f:` |

## Common mistakes

1. **Forgetting to close a file** — Always use the `with` statement to avoid memory leaks and data corruption.
2. **Overwriting data with 'w'** — Remember that 'w' mode deletes everything in the file before writing. Use 'a' to keep existing data.
3. **Incorrect file paths** — Make sure the file exists and you are providing the correct path (relative or absolute).
4. **Encoding issues** — When working with non-English characters, specify `encoding="utf-8"`.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Working demo of reading, writing, and appending to files |
| `exercise.py` | 6 TODOs + 1 challenge on local file manipulation |
| `solution.py` | Answers with explanations for context managers and line-by-line reading |

## Go deeper

- [Reading and Writing Files — Official Docs](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Context Managers (with statement) — PEP 343](https://peps.python.org/pep-0343/)

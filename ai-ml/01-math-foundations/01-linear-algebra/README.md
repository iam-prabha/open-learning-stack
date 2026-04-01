# Linear Algebra for AI/ML

## What is it?

**Linear Algebra** is the language of modern AI. At its core, it's the study of **Vectors** (lists of numbers) and **Matrices** (grids of numbers). In Machine Learning, every data point (like an image or a piece of text) is turned into a vector, and every operation the computer performs is just a series of matrix multiplications.

## Real-world analogy

Think of Linear Algebra like **the spreadsheet for a digital world**:
- **Vectors**: Like a single row in a spreadsheet. One row might contain `[Age, Height, Weight]`. 
- **Matrices**: Like the entire spreadsheet. Each row is a person, and each column is a feature.
- **Dot Product**: Like calculating a weighted total. If you multiply your `[Items]` vector by a `[Prices]` vector, you get the `Total Bill`.
- **Matrix Multiplication**: Like running that same calculation for every customer in the store at once.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **NumPy Arrays** | Storing and manipulating large datasets efficiently | You only have a few small lists (standard Python lists are fine) |
| **Dot Product** | Calculating similarity between two vectors (e.g., in recommendation systems) | You just need simple addition or subtraction |
| **Matrix Mult** | Running a neural network (every layer is a matrix multiplication) | You are doing simple data entry |

## Common mistakes

1. **Shape Mismatch** — Trying to multiply two matrices where the columns of A don't match the rows of B. This is the most common error in AI engineering.
2. **Confusing Dot vs. Element-wise** — `A * B` in NumPy is element-wise, but `A @ B` or `np.dot(A, B)` is the actual matrix multiplication.
3. **Broadcasting Errors** — PyTorch/NumPy will sometimes try to "stretch" a small vector to match a large matrix. If you don't mean for this to happen, you can get very strange bugs.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Vectors, Matrices, and Dot Products in NumPy |
| `notebook.ipynb` | Visualizing Vector addition and Basis components |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Essence of Linear Algebra — 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [Linear Algebra Review for ML — Stanford CS229](https://see.stanford.edu/materials/aimlcs229/cs229-linalg.pdf)

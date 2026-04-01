# Support Vector Machines (SVM): The Maximum Margin

## What is it?

**Support Vector Machines (SVM)** are powerful models used for both classification and regression. Imagine you have two groups of points (cats and dogs) that you want to separate with a line. While there are many lines you *could* draw, SVM finds the **Optimal Line** — the one that stays as far away from both groups as possible. This extra space is called the **Margin**.

## Real-world analogy

Think of SVM like **building a wide highway between two towns**:
- **Towns**: Your data points (Categories).
- **The Center Line**: Your Decision Boundary.
- **The Shoulders**: The Margins.
- **Support Vectors**: The houses closest to the highway. These are the ONLY points that matter; if you move a house far away from the road, the road stays where it is.
- **The Kernel**: If the towns are mixed together and you can't build a straight road, the Kernel "lifts" the whole landscape into 3D so you can slice between them with a flat plane.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **High-Dim** | You have many features (like gene sequences or pixel data) | You have more data points than features |
| **Separable** | Your data has a clear (even if non-linear) gap | Your data is very "noisy" and overlapping |

## Common mistakes

1. **Ignoring Scaling** — SVM is based on distance. If one feature is measured in thousands and another in decimals, the large feature will dominate the model. **Always scale your data for SVM.**
2. **The Wrong Kernel** — Using a 'Linear' kernel for data that is shaped like a donut.
3. **Over-Regularization (C)** — Setting 'C' too high makes the model try to get EVERY point right, which leads to a very wiggly, overfitted boundary.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Training SVM with Linear and RBF Kernels |
| `notebook.ipynb` | Visualizing Margins and the Kernel Trick |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [SVM — Scikit-Learn Docs](https://scikit-learn.org/stable/modules/svm.html)
- [Support Vector Machines Explained — StatQuest](https://www.youtube.com/watch?v=efR1C6B75QI)

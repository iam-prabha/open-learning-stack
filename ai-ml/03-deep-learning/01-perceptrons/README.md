# Perceptrons & Activation Functions

## What is it?

A **Perceptron** is the simplest form of an artificial neural network — the "atom" of deep learning. It's a mathematical model that takes multiple inputs, multiplies them by weights, adds them together, and passes the result through an **Activation Function** to produce a binary or continuous output.

## Real-world analogy

Think of a perceptron like **a bouncer at a club**:
- **Inputs**: The bouncer checks three things: `Is the person 21+?`, `Are they wearing a tie?`, `Are they a VIP?`.
- **Weights**: The bouncer cares most about `Age` (Weight = 10), moderately about `Tie` (Weight = 2), and a lot about `VIP` (Weight = 8).
- **Sum**: If the total score hits a "Threshold" (Bias), the person gets in.
- **Activation Function**: This is the rule for entry. If Score > Threshold, output is `1` (Allowed); otherwise `0` (Denied).

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Perceptron** | Solving simple binary classification (Yes/No) that is "Linearly Separable" (can be split by a straight line) | Solving complex problems like image recognition or language translation (needs multi-layer networks) |
| **Sigmoid** | Predicting probabilities between 0 and 1 | The math requires "Sparse" activations (ReLU is better) |
| **ReLU** | The "default" choice for hidden layers in modern deep networks | You are dealing with negative numbers that carry important information |

## Common mistakes

1. **Forgetting the Bias** — Without a bias term, a perceptron's decision boundary must always pass through the origin (0,0), which is rarely what you want.
2. **Step Function Gradients** — The original "Heaviside" step function has zero gradient everywhere. This makes it impossible to train using modern optimization. We use Sigmoid/ReLU instead.
3. **Linear Separability** — Trying to solve the "XOR problem" with a single perceptron. It's mathematically impossible; you need at least one hidden layer.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Simple Perceptron using PyTorch |
| `notebook.ipynb` | Visualizing decision boundaries |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [The Perceptron — Wikipedia](https://en.wikipedia.org/wiki/Perceptron)
- [PyTorch Linear Layer Docs](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html)

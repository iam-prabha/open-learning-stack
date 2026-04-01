# Logistic Regression: Binary Classification

## What is it?

Despite its name, **Logistic Regression** is used for **Classification**, not regression. It's the standard tool for predicting a binary outcome (Yes/No, Spam/Ham, Pass/Fail). It works by taking the output of a linear equation and squeezing it through a "Sigmoid" function to turn it into a probability between 0 and 1.

## Real-world analogy

Think of Logistic Regression like **a light switch with a dimmer**:
- **Goal**: You want to know if an email is Spam (1) or Not Spam (0).
- **The Line**: Just like Linear Regression, it calculates a score based on keywords.
- **The Dimmer (Sigmoid)**: If the score is very high, the light is fully ON (1.0 probability). If it's very low, it's fully OFF (0.0). If it's in the middle, the light is partially on (0.5), and we have to make a choice.
- **The Decision**: Usually, if the probability is > 0.5, we say it's Spam.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Binary Class** | Predicting a yes/no outcome (e.g., will a customer churn?) | Predicting a number (e.g., how much will they spend?) |
| **Probability** | You need to know how "confident" the model is | You have more than 2 categories (unless using One-vs-Rest) |

## Common mistakes

1. **Thinking it's for Regression** — Don't use it to predict house prices! It only predicts probabilities for categories.
2. **Imbalanced Data** — If 99% of your emails are Not Spam, the model might just learn to say "Not Spam" every time to get 99% accuracy.
3. **Non-linear Boundaries** — It can only separate data with a straight line. If your data is shaped like a circle, you need a different tool (like SVM with kernels).

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Classification using Scikit-Learn |
| `notebook.ipynb` | Visualizing the Sigmoid curve and Decision Boundary |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Logistic Regression — Scikit-Learn Docs](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
- [The Sigmoid Function — Wikipedia](https://en.wikipedia.org/wiki/Sigmoid_function)

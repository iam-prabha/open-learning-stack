# Decision Trees: Flowchart-based Learning

## What is it?

A **Decision Tree** is one of the most intuitive models in AI. It works like a flowchart: if you ask enough Yes/No questions about a piece of data, you'll eventually arrive at a prediction. Unlike Linear models, Decision Trees can easily capture non-linear patterns (e.g., "If Age > 20 AND Income < 10k...").

## Real-world analogy

Think of a Decision Tree like **a digital game of 20 Questions**:
- **Root Node**: The very first question (e.g., "Is it an animal?").
- **Branches**: The possible answers (Yes/No).
- **Leaf Nodes**: The final prediction (e.g., "It's a Dog!").
- **Gini Impurity**: A math measure of "messiness." If a group is all dogs, Gini=0. If it's half dogs and half cats, Gini=0.5. The tree always asks the question that reduces messiness the most.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Non-linear** | You have complex 'rules' (e.g., medical diagnosis) | You have a simple linear trend |
| **Categorical** | You have data like 'Color' or 'City' | You have very high-dimensional sparse data (text) |
| **Visual** | You need to explain *exactly* how a decision was made to a human | You want the absolute highest accuracy (use Random Forest instead) |

## Common mistakes

1. **Growing too Deep** — The tree keeps asking questions until it has a leaf for EVERY SINGLE person in the data. This is called **Overfitting**.
2. **Ignoring Pruning** — Failing to cut back the branches that are just following "noise" in the data.
3. **Instability** — A tiny change in the data can result in a completely different tree.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Training and Visualizing a Tree in Python |
| `notebook.ipynb` | Visualizing the Split Boundaries |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Decision Trees — Scikit-Learn Docs](https://scikit-learn.org/stable/modules/tree.html)
- [How Decision Trees Work — StatQuest](https://www.youtube.com/watch?v=7VeUPuFGJHk)

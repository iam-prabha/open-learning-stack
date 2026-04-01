# k-Nearest Neighbors (k-NN): Finding Similar Neighbors

## What is it?

**k-Nearest Neighbors (k-NN)** is a "Lazy Learner." Unlike other models that build a math formula during training, k-NN just remembers all your data. When it needs to make a prediction for a new point, it looks for the **k** most similar points (neighbors) in the training set and takes a majority vote.

## Real-world analogy

Think of k-NN like **asking for a movie recommendation from friends**:
- **Goal**: You want to know if you'll like a new movie.
- **Your History**: All the movies you've ever seen.
- **k-Neighbors**: Your 3 (k=3) friends whose movie tastes are most similar to yours.
- **Majority Vote**: If 2 friends liked it and 1 didn't, k-NN predicts you'll LIKE it.
- **Similarity**: Movies are "similar" if they share the same genre, director, or vibe.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Simple** | You want a model that is easy to understand and has zero "training" time | You need fast predictions (k-NN becomes very slow as data grows) |
| **Multimodal** | Your data clusters in many small, separate pockets | You have hundreds of features ("Curse of Dimensionality") |
| **Baseline** | You need a quick baseline to compare against more complex models | You have limited memory (you have to store the whole dataset!) |

## Common mistakes

1. **Forgetting to Scale** — Just like SVM, k-NN is based on distance. If "Income" is in thousands and "Age" is in double digits, the model will only care about Income.
2. **Choosing an Even 'k'** — If k=2, you can have a tie (1 vote for Cat, 1 for Dog). Always use an **ODD** number for binary classification.
3. **The Curse of Dimensionality** — In very high-dimensional space (1000+ features), every point starts to look far away from every other point, and "Nearest Neighbor" loses its meaning.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Training k-NN and choosing the best 'k' |
| `notebook.ipynb` | Visualizing k-NN boundaries and local pockets |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [k-NN — Scikit-Learn Docs](https://scikit-learn.org/stable/modules/neighbors.html)
- [k-NN Explained — StatQuest](https://www.youtube.com/watch?v=HVXime0nQeI)

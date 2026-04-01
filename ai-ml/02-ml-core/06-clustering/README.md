# Clustering: Finding Hidden Groups

## What is it?

**Clustering** is an **Unsupervised Learning** technique. In other algorithms, we already know the "answer" (e.g., this email is spam). In Clustering, the computer has no answers; it just looks at a pile of data and says, "These points look similar to each other, so they must belong to the same group."

## Real-world analogy

Think of Clustering like **sorting a mixed bag of LEGOs**:
- **Goal**: You want to group the pieces by type, but you don't have a manual.
- **K-Means**: You decide you want 3 piles (K=3). You pick 3 random pieces (Centroids) and start putting every other piece near the one it looks most like. Then you move the "center" of the pile to the middle of your new group and repeat until the piles stop moving.
- **DBSCAN**: You group pieces that are physically touching each other. If a piece is all by itself in the corner, it's marked as "Noise."

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **K-Means** | You have clear, circular-ish clusters (e.g., customer segments) | Your clusters are weirdly shaped (like two interlocked crescents) |
| **DBSCAN** | You have outliers/noise you want to ignore | Your data varies a lot in density (heavy clusters and light clusters) |
| **Hierarchical**| You want to see the "family tree" of how groups relate | You have a massive dataset (it's very slow) |

## Common mistakes

1. **Choosing the wrong 'K'** — Assuming there are 5 groups when there are actually 2.
2. **Ignoring Scaling** — (Again!) Since clustering is distance-based, features must be normalized.
3. **Circular Bias** — Using K-Means on data that is shaped like lines or long ovals. K-Means will try to "round off" the clusters, leading to poor results.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Implementation of K-Means and the Elbow Method |
| `notebook.ipynb` | Visualizing moving Centroids and Cluster boundaries |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Clustering — Scikit-Learn Docs](https://scikit-learn.org/stable/modules/clustering.html)
- [K-Means Clustering — StatQuest](https://www.youtube.com/watch?v=4b5d3muPQmA)

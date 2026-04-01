# Statistics: Understanding the Data

## What is it?

If Probability is about predicting the future, **Statistics** is about analyzing the past. It's the process of collecting, organizing, and interpreting data to find patterns. In AI, we use statistics to "clean" our data and to prove that our model's improvements are "real" and not just due to luck.

## Real-world analogy

Think of Statistics like **a sports commentator's recap**:
- **Descriptive Stats**: "Player X averaged 25 points per game (Mean) and usually scored around 20 (Median)."
- **Variance**: "He is inconsistent — sometimes 5 points, sometimes 50 (High Variance)."
- **Hypothesis Testing**: "Is he actually playing better this season, or was it just one lucky game? (Statistical Significance)."
- **P-value**: The tiny chance that his 'improvement' was actually just a fluke.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Mean/Median** | Summarizing the center of your data | The data is highly skewed (e.g., billionaire incomes in a poor town) — use Median instead |
| **Standard Dev** | Measuring how much your data "spreads out" from the average | You only care about the absolute total |
| **Hypothesis Test** | Comparing Two models to see which one is truly better | You are just visualizing the data for yourself |

## Common mistakes

1. **Correlation vs. Causation** — Just because ice cream sales and shark attacks both go up in summer (Correlation) doesn't mean eating ice cream *causes* shark attacks.
2. **Ignoring Sample Size** — Thinking a survey of 3 people represents the views of a whole country.
3. **Outlier Sensitivity** — Using the 'Mean' for data with extreme outliers. If 10 people earn $50k and 1 person earns $1M, the 'Mean' is $136k, which represents NO ONE correctly.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Descriptive Statistics and Hypothesis Testing in Python |
| `notebook.ipynb` | Visualizing Central Limit Theorem |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Introduction to Statistics — Khan Academy](https://www.khanacademy.org/math/statistics-probability)
- [P-values Explained — StatQuest](https://www.youtube.com/watch?v=vemZtEM63GY)

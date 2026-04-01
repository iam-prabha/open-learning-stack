# Linear Regression: Predicting a Number

## What is it?

**Linear Regression** is the simplest supervised learning algorithm. It's used to predict a continuous output (a number) based on one or more inputs. It works by finding the "Line of Best Fit" through your data points.

## Real-world analogy

Think of Linear Regression like **predicting the price of a house**:
- **Goal**: You want a formula to estimate `Price` based on `Square Footage`.
- **The Line**: You draw a straight line through the past sales data.
- **Weights**: The slope of the line (e.g., "$200 per square foot").
- **Intercept (Bias)**: The baseline price regardless of size (e.g., "$50,000 for the land").
- **Prediction**: If a house is 1,000 sqft, the model predicts: `50,000 + (200 * 1000) = $250,000`.

## When to use it

| Feature | Use when... | Avoid when... |
|---|---|---|
| **Simple Regression**| You have a clear linear relationship (e.g., salary vs. years of experience) | The data follows a curve (e.g., speed vs. fuel consumption) |
| **Multivariate** | You have multiple inputs (size, location, number of rooms) | You have thousands of inputs (deep learning is better) |

## Common mistakes

1. **Assuming Linearity** — Trying to fit a straight line to data that is clearly curved.
2. **Ignoring Outliers** — A single data point (like a $50M mansion) can pull the whole line away from the other data points, making it less accurate.
3. **Overfitting** — Adding too many features to a small dataset, which causes the model to "memorize" the noise instead of finding the real pattern.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Implementation using Scikit-Learn |
| `notebook.ipynb` | Visualizing the Best Fit line |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Linear Regression — Scikit-Learn Docs](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares)
- [Linear Regression Explained — StatQuest](https://www.youtube.com/watch?v=PaFPbb66DxQ)

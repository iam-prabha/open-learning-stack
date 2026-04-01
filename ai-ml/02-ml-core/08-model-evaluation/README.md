# Model Evaluation: Is Your AI Actually Good?

## What is it?

**Model Evaluation** is the process of measuring how well your AI model performs on data it has **never seen before**. A model that gets 100% on its training data but 50% on new data is "Overfitted" (it memorized the answers instead of learning the patterns). We use metrics like Accuracy, Precision, and Recall to get a complete picture of a model's health.

## Real-world analogy

Think of Model Evaluation like **a student taking a final exam**:
- **Training Data**: The textbook and practice homework.
- **Test Data**: The actual final exam (questions they've never seen).
- **Accuracy**: The final grade (e.g., 90%).
- **Precision vs. Recall**:
    - **Precision**: "When you say it's a Dog, how often is it actually a Dog?" (Avoiding false alarms).
    - **Recall**: "Out of all the Dogs in the world, how many did you find?" (Avoiding missing cases).
- **Confusion Matrix**: A chart showing exactly which animals the student is confusing with others (e.g., "Keeps calling cats 'dogs'").

## When to use it

| Metric | Use when... | Avoid when... |
|---|---|---|
| **Accuracy** | Your classes are balanced (50% cats, 50% dogs) | Your data is imbalanced (99% no cancer, 1% cancer) |
| **F1-Score** | You want a balance between Precision and Recall | You care way more about one than the other (e.g., in medical tests, Recall is usually more important) |
| **ROC/AUC** | You want to know how well the model separates classes regardless of the threshold | You have a very simple binary task with no probability outputs |

## Common mistakes

1. **Information Leakage** — Accidentally showing the model the "answers" (test data) during training.
2. **Ignoring Imbalance** — Getting "99% accuracy" on a fraud detection model by simply predicting "No Fraud" for everyone. 
3. **Overusing Accuracy** — Thinking a model is great because it has high accuracy, while it actually has 0% Recall for the most important class.

## Files in this folder

| File | Purpose |
|---|---|
| `example.py` | Implementation of Confusion Matrix and F1-Score |
| `notebook.ipynb` | Visualizing ROC Curves and Precision-Recall tradeoffs |
| `exercise.py` | 6 TODOs + 1 challenge |
| `solution.py` | Answers with WHY comments |

## Go deeper

- [Model Evaluation — Scikit-Learn Docs](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Precision and Recall — Wikipedia](https://en.wikipedia.org/wiki/Precision_and_recall)

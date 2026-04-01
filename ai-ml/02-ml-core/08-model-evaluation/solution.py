# solution.py - Model Evaluation answers

import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression

# TODO 1 & 2
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# TODO 3
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# TODO 4
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall: {recall_score(y_test, y_pred):.4f}")

# TODO 5
# Answer: A False Negative (Missed Case). Telling 
# someone they are healthy when they actually have 
# cancer is far more dangerous than the reverse.

# TODO 6
# Answer: Recall. High recall means you are finding 
# almost all the positive cases, even if you stay 
# slightly more cautious (lower precision).

# CHALLENGE ANSWER
tp = np.sum((y_test == 1) & (y_pred == 1))
tn = np.sum((y_test == 0) & (y_pred == 0))
fp = np.sum((y_test == 0) & (y_pred == 1))
fn = np.sum((y_test == 1) & (y_pred == 0))
print(f"\nManual Confusion Matrix:")
print(f"[{tn}, {fp}]")
print(f"[{fn}, {tp}]")

print("\n--- Why it works ---")
print("1. Holistic View: Accuracy alone is a lie. Evaluation metrics give you the multi-dimensional truth about your model's reliability.")
print("2. Trust: In critical fields like medicine or self-driving cars, 'Probability of Error' is the most important number the model produces.")
print("3. Iteration: You can't improve what you can't measure. Evaluation tells you EXACTLY where your model is struggling.")
print("4. Real-world Readiness: A model isn't finished when it works on your computer; it's finished when it proves it can handle the messiness of the real world.")

export {};

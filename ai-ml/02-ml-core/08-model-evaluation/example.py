# example.py - Model Evaluation Metrics

import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# 1. Create Imbalanced data (1000 samples, only 10% are positive)
X, y = make_classification(n_samples=1000, n_classes=2, weights=[0.9, 0.1], random_state=42)

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Model Training
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. Predictions
y_pred = model.predict(X_test)

# 5. Confusion Matrix
# [True Neg, False Pos]
# [False Neg, True Pos]
cm = confusion_matrix(y_test, y_pred)
print("--- Confusion Matrix ---")
print(cm)

# 6. Detailed Report
# Includes Precision, Recall, and F1
print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred))

# 7. Single F1 score
f1 = f1_score(y_test, y_pred)
print(f"F1 Score (Weighted Mean of Precision/Recall): {f1:.4f}")

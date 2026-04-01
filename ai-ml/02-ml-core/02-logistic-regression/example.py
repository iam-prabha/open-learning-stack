# example.py - Logistic Regression Classification

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Simulated Data (Hours Studied, Pass/Fail)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1]) # Pass = 1, Fail = 0

# 2. Training the Model
model = LogisticRegression()
model.fit(X, y)

# 3. Model Parameters
beta_0 = model.intercept_[0]
beta_1 = model.coef_[0][0]
print(f"Model: Log-Odds = {beta_1:.2f} * Hours + {beta_0:.2f}")

# 4. Predictions & Probabilities
new_students = np.array([[3.5], [4.5], [10]])
preds = model.predict(new_students)
probs = model.predict_proba(new_students)

for i, student in enumerate(new_students):
    print(f"Hours: {student[0]} -> Prediction: {preds[i]}, Prob(Pass): {probs[i][1]:.4f}")

# 5. Accuracy on training data
y_pred = model.predict(X)
print(f"\nTraining Accuracy: {accuracy_score(y, y_pred) * 100}%")

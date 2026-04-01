# solution.py - Decision Tree answers

from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# TODO 1 & 2
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TODO 3
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

# TODO 4
acc = model.score(X_test, y_test)
print(f"Test Accuracy: {acc * 100:.2f}%")

# TODO 5
# Answer: Gini Impurity or Information Gain (Entropy).

# TODO 6
# Answer: Pruning is the process of removing branches 
# that provide little power to classify instances. 
# It is done to reduce complexity and prevent OVERFITTING.

# CHALLENGE ANSWER
importances = model.feature_importances_
indices = np.argsort(importances)[::-1] # Sort descending
print(f"Top 3 Features:")
for i in range(3):
    idx = indices[i]
    print(f"{i+1}. {data.feature_names[idx]} ({importances[idx]:.4f})")

print("\n--- Why it works ---")
print("1. No Preprocessing: Unlike many models, trees don't care if your data is scaled correctly or has outliers. They just make 'cuts'.")
print("2. Human-Centric: You can literally print out the tree and follow it with a pen to see why it made a certain choice.")
print("3. Feature Selection: Trees automatically figure out which features are useless and which ones are critical, helping you understand your own data better.")
print("4. Foundation: Understanding single trees is the prerequisite for powerful 'Ensemble' models like Random Forest and XGBoost.")

export {};

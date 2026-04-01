# exercise.py - Practice with Model Evaluation

import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression

# TODO 1: Load 'breast_cancer' data.
data = load_breast_cancer()
X, y = data.data, data.target

# TODO 2: Split data (70% train, 30% test).

# TODO 3: Fit a LogisticRegression model. 
# (Set max_iter=2000 to ensure convergence)

# TODO 4: Calculate Accuracy, Precision, and Recall 
# on the test set.

# TODO 5: If you are building an AI to detect 
# 'Malignant' tumors, which is more dangerous: 
# a False Positive (False Alarm) or 
# a False Negative (Missed Case)?
# Answer: ...

# TODO 6: Which metric (Precision or Recall) 
# focus on minimizing THAT specific danger?
# Answer: ...

# CHALLENGE: Create a Confusion Matrix manually 
# using only the 'y_test' and 'y_pred' arrays.
# (Hint: TP = count where test==1 and pred==1)

# --- Verification ---
print("--- Results ---")
# Check your evaluation logic vs the solution!
